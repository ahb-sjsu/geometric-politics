# Appendix B: The District 7 Model — Code Walkthrough

This appendix provides a Python implementation of the core computational constructions used throughout the book. The code is designed for reproducibility: all computational results in the main text can be verified using these implementations.

---

## B.1 Preference Manifold Construction

```python
import numpy as np
from scipy.spatial.distance import mahalanobis
from scipy.linalg import inv

class PoliticalManifold:
    """
    Six-dimensional political preference manifold.

    Dimensions:
        d1: Economic policy
        d2: Social values
        d3: Environmental priority
        d4: Foreign policy
        d5: Institutional trust
        d6: Identity
    """

    def __init__(self, voters: np.ndarray):
        """
        Args:
            voters: (n, 6) array of voter positions on the manifold
        """
        assert voters.shape[1] == 6, "Manifold requires 6 dimensions"
        self.voters = voters
        self.n = voters.shape[0]
        self.d = 6
        self.mean = np.mean(voters, axis=0)
        self.cov = np.cov(voters.T)
        self.cov_inv = inv(self.cov)

        # Eigendecomposition for dimensionality analysis
        eigenvalues, eigenvectors = np.linalg.eigh(self.cov)
        idx = np.argsort(eigenvalues)[::-1]
        self.eigenvalues = eigenvalues[idx]
        self.eigenvectors = eigenvectors[:, idx]

    def manifold_distance(self, v1: np.ndarray, v2: np.ndarray) -> float:
        """Mahalanobis distance as manifold distance approximation."""
        diff = v1 - v2
        return np.sqrt(diff @ self.cov_inv @ diff)

    def frechet_mean(self) -> np.ndarray:
        """
        Frechet mean of the voter distribution.
        For Mahalanobis metric, this is the arithmetic mean.
        """
        return self.mean

    def effective_dimensionality(self, threshold: float = 0.85) -> int:
        """Number of dimensions needed to explain threshold of variance."""
        total = np.sum(self.eigenvalues)
        cumulative = np.cumsum(self.eigenvalues) / total
        return int(np.searchsorted(cumulative, threshold)) + 1

    def project_1d(self, axis: np.ndarray) -> np.ndarray:
        """Project all voters onto a 1D axis."""
        axis = axis / np.linalg.norm(axis)
        return self.voters @ axis
```

## B.2 Voting System Contractions

```python
class VotingSystem:
    """Base class for voting system contractions."""

    def __init__(self, manifold: PoliticalManifold,
                 candidates: np.ndarray):
        """
        Args:
            manifold: The political preference manifold
            candidates: (m, 6) array of candidate positions
        """
        self.manifold = manifold
        self.candidates = candidates
        self.m = candidates.shape[0]

    def voter_distances(self) -> np.ndarray:
        """(n, m) matrix of manifold distances voter -> candidate."""
        distances = np.zeros((self.manifold.n, self.m))
        for i in range(self.manifold.n):
            for j in range(self.m):
                distances[i, j] = self.manifold.manifold_distance(
                    self.manifold.voters[i], self.candidates[j]
                )
        return distances


class PluralityVoting(VotingSystem):
    """Plurality (first-past-the-post) voting."""

    def run(self) -> int:
        """Returns index of winning candidate."""
        distances = self.voter_distances()
        first_choices = np.argmin(distances, axis=1)
        vote_counts = np.bincount(first_choices, minlength=self.m)
        return int(np.argmax(vote_counts))

    def information_preserved(self) -> float:
        """Fraction of manifold information preserved."""
        return 1.0 / self.manifold.d


class RankedChoiceVoting(VotingSystem):
    """Ranked-choice voting (instant runoff)."""

    def run(self) -> int:
        """Returns index of winning candidate via IRV elimination."""
        distances = self.voter_distances()
        rankings = np.argsort(distances, axis=1)
        active = np.ones(self.m, dtype=bool)

        while np.sum(active) > 1:
            # Count first-choice votes among active candidates
            first_choices = np.zeros(self.m, dtype=int)
            for voter_ranking in rankings:
                for cand in voter_ranking:
                    if active[cand]:
                        first_choices[cand] += 1
                        break

            total = np.sum(first_choices[active])
            # Check for majority
            if np.max(first_choices) > total / 2:
                return int(np.argmax(first_choices))

            # Eliminate lowest
            active_counts = first_choices.copy()
            active_counts[~active] = total + 1
            eliminate = np.argmin(active_counts)
            active[eliminate] = False

        return int(np.where(active)[0][0])

    def information_preserved(self) -> float:
        """Fraction of manifold information preserved."""
        return min(self.manifold.d, self.m - 1) / self.manifold.d
```

## B.3 Gerrymandering Index

```python
class GerrymanderingAnalysis:
    """Gerrymandering index computation on the manifold."""

    def __init__(self, manifold: PoliticalManifold,
                 geography: np.ndarray):
        """
        Args:
            manifold: Political preference manifold
            geography: (n, 2) array of voter geographic positions
        """
        self.manifold = manifold
        self.geography = geography

    def gerrymandering_index(self,
                              assignment: np.ndarray) -> float:
        """
        Compute GI(D) for a district assignment.

        Args:
            assignment: (n,) array of district labels for each voter

        Returns:
            Average manifold distance from voter to district mean.
        """
        districts = np.unique(assignment)
        total_dist = 0.0

        for d in districts:
            mask = assignment == d
            district_voters = self.manifold.voters[mask]
            district_mean = np.mean(district_voters, axis=0)

            for voter in district_voters:
                total_dist += self.manifold.manifold_distance(
                    voter, district_mean
                )

        return total_dist / self.manifold.n

    def dimension_specific_gi(self, assignment: np.ndarray,
                               dim: int) -> float:
        """GI computed on a single dimension."""
        districts = np.unique(assignment)
        total_dist = 0.0

        for d in districts:
            mask = assignment == d
            positions = self.manifold.voters[mask, dim]
            mean_pos = np.mean(positions)
            total_dist += np.sum(np.abs(positions - mean_pos))

        return total_dist / self.manifold.n
```

## B.4 Political Bond Index

```python
class PoliticalBondIndex:
    """Compute the Political Bond Index."""

    def __init__(self, manifold: PoliticalManifold,
                 representatives: np.ndarray,
                 voter_rep_assignment: np.ndarray):
        """
        Args:
            manifold: Political preference manifold
            representatives: (k, 6) representative positions
            voter_rep_assignment: (n,) which rep represents each voter
        """
        self.manifold = manifold
        self.representatives = representatives
        self.assignment = voter_rep_assignment

    def compute(self) -> float:
        """
        BI(S, E) = E[d(v, r(v)) - d(v, r*(v))]
        """
        actual_distances = np.zeros(self.manifold.n)
        optimal_distances = np.zeros(self.manifold.n)

        for i in range(self.manifold.n):
            v = self.manifold.voters[i]
            r = self.representatives[self.assignment[i]]
            actual_distances[i] = self.manifold.manifold_distance(v, r)

            # Optimal: closest representative
            min_dist = np.inf
            for rep in self.representatives:
                d = self.manifold.manifold_distance(v, rep)
                min_dist = min(min_dist, d)
            optimal_distances[i] = min_dist

        return np.mean(actual_distances - optimal_distances)

    def compute_by_dimension(self) -> np.ndarray:
        """Dimension-specific Bond Index."""
        bi_dims = np.zeros(self.manifold.d)

        for dim in range(self.manifold.d):
            actual = np.zeros(self.manifold.n)
            optimal = np.zeros(self.manifold.n)

            for i in range(self.manifold.n):
                v_pos = self.manifold.voters[i, dim]
                r_pos = self.representatives[
                    self.assignment[i], dim
                ]
                actual[i] = abs(v_pos - r_pos)

                min_dist = min(
                    abs(v_pos - rep[dim])
                    for rep in self.representatives
                )
                optimal[i] = min_dist

            bi_dims[dim] = np.mean(actual - optimal)

        return bi_dims
```

## B.5 Campaign Gradient Optimization

```python
def campaign_gradient(manifold: PoliticalManifold,
                      candidate_position: np.ndarray) -> np.ndarray:
    """
    Find the optimal projection axis for a campaign.

    Implements the Campaign Gradient Theorem:
    e* = argmax_e |<x_C - mu, e>|^2 / (e^T Sigma e)

    Returns the optimal projection axis (unit vector).
    """
    diff = candidate_position - manifold.mean

    # Solve generalized eigenvalue problem
    # Maximize (diff^T e)^2 / (e^T Sigma e)
    # This is equivalent to finding the eigenvector of
    # Sigma^{-1} (diff diff^T) with largest eigenvalue

    M = manifold.cov_inv @ np.outer(diff, diff)
    eigenvalues, eigenvectors = np.linalg.eig(M)
    idx = np.argmax(np.real(eigenvalues))

    optimal_axis = np.real(eigenvectors[:, idx])
    return optimal_axis / np.linalg.norm(optimal_axis)
```

## B.6 Usage Example: District 7

```python
# Generate District 7 synthetic electorate
np.random.seed(42)

# Five subcommunities
urban_core = np.random.multivariate_normal(
    [-1.5, -0.3, 0.8, 0.0, -1.2, 1.5],
    np.eye(6) * 0.5, size=600
)
university = np.random.multivariate_normal(
    [-1.8, -2.0, 2.0, -1.0, 0.5, -1.5],
    np.eye(6) * 0.4, size=300
)
suburbs = np.random.multivariate_normal(
    [0.2, 0.0, 0.3, -0.2, 0.3, 0.0],
    np.eye(6) * 0.6, size=500
)
exurban = np.random.multivariate_normal(
    [1.5, 1.2, -1.0, 1.0, -2.0, 1.0],
    np.eye(6) * 0.5, size=400
)
meadow_pines = np.random.multivariate_normal(
    [0.8, 1.0, -0.5, -1.5, 0.8, 0.5],
    np.eye(6) * 0.4, size=200
)

voters = np.vstack([urban_core, university, suburbs,
                     exurban, meadow_pines])

# Build manifold
manifold = PoliticalManifold(voters)

print(f"Effective dimensionality (85%): "
      f"{manifold.effective_dimensionality()}")
print(f"Eigenvalue distribution: "
      f"{manifold.eigenvalues / manifold.eigenvalues.sum()}")
```

All code in this appendix is available at the book's companion repository. The implementations are intentionally simple — production use would require optimization for large electorates and more sophisticated manifold distance estimation.
