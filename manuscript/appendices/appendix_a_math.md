# Appendix A: Mathematical Prerequisites

This appendix provides the mathematical background needed to follow the formal arguments in the main text. It is self-contained for a reader with undergraduate linear algebra and basic real analysis. For complete proofs and deeper development, see *Geometric Methods in Computational Modeling* (Bond, 2026a) and *Geometric Reasoning: From Search to Manifolds* (Bond, 2026c).

---

## A.1 Riemannian Geometry

### Manifolds

A *manifold* $\mathcal{M}$ of dimension $d$ is a topological space that locally resembles $\mathbb{R}^d$. Formally, every point $p \in \mathcal{M}$ has a neighborhood that is homeomorphic to an open subset of $\mathbb{R}^d$. The homeomorphism provides *local coordinates* — a way to assign $d$ real numbers to each point near $p$.

The political preference manifold $\mathcal{P}$ of this book has dimension $d = 6$. Each point on $\mathcal{P}$ is a six-tuple $(d_1, d_2, d_3, d_4, d_5, d_6)$ representing a voter's position on the six policy dimensions. The manifold structure is important because it allows us to define geometric concepts — distance, curvature, geodesics — that would not be well-defined on an unstructured set of points.

### Riemannian Metric

A *Riemannian metric* $g$ on $\mathcal{M}$ is a smooth assignment of an inner product $g_p: T_p\mathcal{M} \times T_p\mathcal{M} \to \mathbb{R}$ to the tangent space at each point $p$. The metric determines the length of curves on $\mathcal{M}$:

$$\ell(\gamma) = \int_a^b \sqrt{g_{\gamma(t)}(\dot{\gamma}(t), \dot{\gamma}(t))} \, dt$$

The length of the shortest curve between two points is the *geodesic distance*:

$$d_\mathcal{M}(p, q) = \inf_\gamma \ell(\gamma)$$

In the political context, the metric $g_{ij}(p)$ encodes the cost of political movement: how much effort (in terms of persuasion, compromise, or value change) is required to move from one political position to a nearby one. The metric is anisotropic (different dimensions have different costs) and position-dependent (the cost varies across the manifold).

### Geodesics

A *geodesic* is a curve that locally minimizes length — the analog of a straight line in curved space. On the political manifold, a geodesic between two voter positions is the "path of least resistance" for political persuasion or compromise.

Geodesics satisfy the geodesic equation:

$$\ddot{\gamma}^k + \Gamma^k_{ij} \dot{\gamma}^i \dot{\gamma}^j = 0$$

where $\Gamma^k_{ij}$ are the Christoffel symbols, determined by the metric:

$$\Gamma^k_{ij} = \frac{1}{2} g^{kl}\left(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}\right)$$

### Curvature

The *Riemann curvature tensor* $R^l_{ijk}$ measures the failure of parallel transport to preserve vectors — the intrinsic curvature of the manifold. Positive curvature corresponds to geodesics converging; negative curvature corresponds to geodesics diverging.

In the political context, high positive curvature near sacred-value boundaries means that political positions on opposite sides of the boundary are much farther apart than they appear in coordinate distance. Two voters who differ by one point on the abortion scale, but on opposite sides of the pro-life/pro-choice boundary, are infinitely far apart in the political metric because the curvature is singular at the boundary.

## A.2 Social Choice Theory

### Arrow's Theorem

**Arrow's Impossibility Theorem (1951).** *For three or more alternatives and two or more voters, there is no social welfare function $f: \mathcal{L}^n \to \mathcal{L}$ (mapping individual orderings to a social ordering) that satisfies all three conditions: (1) Independence of Irrelevant Alternatives (IIA), (2) Unanimity, and (3) Non-dictatorship.*

The proof proceeds by showing that axioms (1) and (2) together imply the existence of a "decisive" voter for every pair of alternatives, and that the decisive voter must be the same for all pairs — i.e., a dictator.

Chapter 7 reinterprets this result as a statement about the impossibility of lossless dimensional contraction: the three axioms require preservation of topological, orientational, and symmetry structure that a 1D contraction cannot preserve.

### The Gibbard-Satterthwaite Theorem

**Gibbard-Satterthwaite Theorem (1973/1975).** *Any non-dictatorial voting function for three or more alternatives is susceptible to strategic manipulation: there exists a situation in which some voter can obtain a better outcome by misreporting their preferences.*

This result is the strategic counterpart to Arrow's theorem: not only is lossless contraction impossible, but any lossy contraction creates incentives for voters to misrepresent their preferences (report a distorted manifold position) to influence the outcome.

## A.3 Dimensionality Reduction

### Principal Component Analysis

*Principal Component Analysis* (PCA) finds the orthogonal axes of maximum variance in a dataset. For the $n \times d$ data matrix $X$ (voters $\times$ dimensions), PCA computes the eigendecomposition of the covariance matrix $\Sigma = X^T X / n$:

$$\Sigma = U \Lambda U^T$$

where $\Lambda = \text{diag}(\lambda_1, \ldots, \lambda_d)$ with $\lambda_1 \geq \cdots \geq \lambda_d \geq 0$. The eigenvectors in $U$ are the principal components; the eigenvalues $\lambda_i$ measure the variance along each component.

The eigenvalue distribution of $\Sigma$ determines the effective dimensionality of the data. If $\lambda_1 \gg \lambda_2 \gg \cdots$, the data is effectively low-dimensional; if the eigenvalues are comparable, the data is genuinely multi-dimensional.

### The Mahalanobis Distance

The *Mahalanobis distance* accounts for the covariance structure of the data:

$$d_M(x, y) = \sqrt{(x - y)^T \Sigma^{-1} (x - y)}$$

This is the manifold distance for a Gaussian distribution on a flat manifold. It serves as a useful approximation to the geodesic distance on the political preference manifold when the curvature is moderate.

## A.4 Gauge Theory

A *gauge transformation* is a change of description that should leave the observables unchanged. In physics, gauge transformations change the mathematical representation of a physical state without changing the physical state itself. In the Geometric Series, gauge transformations change the description of a normative situation without changing the normative content.

The *gauge group* $G$ is the group of all gauge transformations. An observable is *gauge-invariant* if it takes the same value under all gauge transformations. The *Bond Invariance Principle* (BIP) requires that domain-specific evaluations be gauge-invariant.

In politics, the democratic gauge group $G_D$ is generated by voter anonymity, option neutrality, and re-description invariance. The Political BIP requires that democratic evaluations be invariant under $G_D$.

## A.5 Topological Data Analysis

*Persistent homology* is a tool for extracting topological features (connected components, loops, voids) from point cloud data at multiple spatial scales. Applied to voter preference distributions, persistent homology identifies:

- **$H_0$ features:** Connected components — clusters of voters with similar preferences. Persistent $H_0$ features are stable communities of interest.
- **$H_1$ features:** Loops — cyclical patterns in preference structure. An $H_1$ feature in a voter preference distribution indicates a Condorcet-like cycle: a loop in the preference ordering that persists across scales.

The persistence of a feature — the range of scales over which it exists — distinguishes signal (persistent features) from noise (ephemeral features).
