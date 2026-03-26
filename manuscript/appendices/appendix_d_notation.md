# Appendix D: Notation and Conventions

This appendix collects the notation used throughout the book. Conventions are consistent with the Geometric Series.

---

## Manifolds and Spaces

| Symbol | Meaning | First Appearance |
|---|---|---|
| $\mathcal{P}$ | Political preference manifold (6-dimensional) | Ch. 4 |
| $d$ | Dimensionality of $\mathcal{P}$ ($d = 6$) | Ch. 4 |
| $d_1, \ldots, d_6$ | The six manifold dimensions: economic, social, environmental, foreign policy, trust, identity | Ch. 1 |
| $g_{ij}$ | Riemannian metric tensor on $\mathcal{P}$ | Ch. 4 |
| $\Sigma$ | Covariance matrix of voter distribution on $\mathcal{P}$ ($6 \times 6$) | Ch. 4 |
| $\Sigma_{ij}$ | Covariance between dimensions $d_i$ and $d_j$ | Ch. 4 |
| $\lambda_1, \ldots, \lambda_6$ | Eigenvalues of $\Sigma$ (in decreasing order) | Ch. 4 |
| $d_\mathcal{P}(v_1, v_2)$ | Geodesic distance between $v_1$ and $v_2$ on $\mathcal{P}$ | Ch. 4 |
| $d_M(v_1, v_2)$ | Mahalanobis distance (manifold distance approximation) | Ch. 4 |
| $T\mathcal{P}$ | Tangent bundle of $\mathcal{P}$ | Ch. 6 |
| $\mathcal{O}$ | Outcome space of a voting function | Ch. 5 |
| $W$ | Overton window (connected bounded subset of $\mathcal{P}$) | Ch. 10 |
| $\partial W$ | Boundary of the Overton window | Ch. 10 |

## Voters and Representatives

| Symbol | Meaning | First Appearance |
|---|---|---|
| $V$ | Set of voters | Ch. 5 |
| $n$ | Number of voters | Ch. 5 |
| $v, v_i$ | Individual voter (or voter's manifold position) | Ch. 4 |
| $\phi: V \to \mathcal{P}$ | Preference configuration (assigns manifold position to each voter) | Ch. 5 |
| $\mu$ | Mean of voter distribution on $\mathcal{P}$ | Ch. 4 |
| $\bar{v}$ | Frechet mean of the voter distribution | Ch. 4 |
| $r(v)$ | Representative of voter $v$ under electoral system $E$ | Ch. 15 |
| $r^*(v)$ | Manifold-optimal representative for voter $v$ | Ch. 15 |
| $x_C, x_{C_i}$ | Candidate's position on $\mathcal{P}$ | Ch. 5 |

## Voting and Elections

| Symbol | Meaning | First Appearance |
|---|---|---|
| $\mathcal{V}$ | Voting function ($\mathcal{P}^n \to \mathcal{O}$) | Ch. 5 |
| $E$ | Electoral system | Ch. 15 |
| $C_1, \ldots, C_m$ | Candidates | Ch. 5 |
| $m$ | Number of candidates | Ch. 5 |
| $k$ | Number of districts | Ch. 9 |
| $D$ | Districting function ($V \to \{1, \ldots, k\}$) | Ch. 9 |
| $D^{-1}(j)$ | Voters assigned to district $j$ | Ch. 9 |

## Indices and Measures

| Symbol | Meaning | First Appearance |
|---|---|---|
| $BI(S, E)$ | Political Bond Index for population $S$ under system $E$ | Ch. 15 |
| $BI_i(S, E)$ | Dimension-specific Bond Index on dimension $d_i$ | Ch. 15 |
| $GI(D)$ | Gerrymandering Index for districting $D$ | Ch. 9 |
| $GI_{d_i}(D)$ | Dimension-specific gerrymandering index | Ch. 9 |
| $R$ | Information preservation ratio | Ch. 5, 13 |

## Campaign and Media

| Symbol | Meaning | First Appearance |
|---|---|---|
| $\mathbf{F}_C$ | Campaign heuristic field (vector field on $\mathcal{P}$) | Ch. 6 |
| $\mathbf{e}$ | Projection axis (unit vector in $\mathbb{R}^d$) | Ch. 6 |
| $\mathbf{e}^*$ | Optimal campaign projection axis | Ch. 6 |
| $\mathbf{h}$ | Political heuristic field (superposition of all sources) | Ch. 6 |
| $\alpha_k(v)$ | Influence weight of information source $k$ at voter $v$ | Ch. 6 |
| $\beta_O$ | Overton window boundary penalty coefficient | Ch. 10 |

## Symmetry and Gauge Theory

| Symbol | Meaning | First Appearance |
|---|---|---|
| $G_D$ | Democratic gauge group | Ch. 5 |
| $\tau_A$ | Voter anonymity transformation | Ch. 5 |
| $\tau_N$ | Option neutrality transformation | Ch. 5 |
| $\tau_R$ | Re-description invariance transformation | Ch. 5 |
| $D_4$ | Dihedral group of order 8 (Hohfeldian symmetry) | Ch. 17 |

## Coalition Analysis

| Symbol | Meaning | First Appearance |
|---|---|---|
| $C$ | Coalition (subset of voters or agents) | Ch. 12 |
| $A_C$ | Agreement submanifold of coalition $C$ | Ch. 12 |
| $F(C)$ | Fragility index of coalition $C$ | Ch. 12 |
| $\epsilon$ | Agreement tolerance threshold | Ch. 12 |

## Conventions

- **Indices:** Latin indices $i, j, k$ range over manifold dimensions (1 to 6). Subscripts on voter variables ($v_1, v_2$) index individuals.
- **Vectors:** Boldface ($\mathbf{e}, \mathbf{h}, \mathbf{F}$) for vectors and vector fields. Italic ($v, p$) for points on the manifold.
- **Tensors:** Component notation $g_{ij}$, $\Sigma_{ij}$ with Einstein summation convention where applicable.
- **Expectations:** $\mathbb{E}[\cdot]$ for expectations over the voter population; $\mathbb{E}_v[\cdot]$ when the variable of integration is specified.
- **Series references:** GR = *Geometric Reasoning*. GE = *Geometric Ethics*. GComm = *Geometric Communication*. GEcon = *Geometric Economics*. GMed = *Geometric Medicine*. GL = *Geometric Law*.
