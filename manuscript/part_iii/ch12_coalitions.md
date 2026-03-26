# Chapter 12: Coalition Building as Pareto Optimization

> *"Politics is the art of the possible, the attainable — the art of the next best."*
> — Otto von Bismarck

---

> **RUNNING EXAMPLE — DISTRICT 7**
>
> *An environmental bond measure is proposed in District 7. The measure would fund a regional solar installation, expand public transit, and create a conservation easement on farmland at the district's exurban fringe. The price tag: a modest property tax increase.*
>
> *On the left-right axis, the coalition for this measure should be obvious: progressives support environmental spending. But the measure needs 60% to pass, and District 7's progressives are only about 40% of the electorate. The measure needs cross-partisan support.*
>
> *On the manifold, the coalition exists. Progressive urban voters support the measure on $d_3$ (environmental priority) and $d_1$ (public investment). Libertarian exurban voters — nominally conservative — support the conservation easement because it protects property values and prevents dense development near their homes. Moderate suburban parents support the transit expansion because it would reduce their commute and improve air quality near the school. A retired engineer in Meadow Pines supports the solar installation as a sensible infrastructure investment.*
>
> *The coalition is incoherent on the left-right axis — it spans the full spectrum. On the manifold, it occupies a connected subregion of $d_3$ space. The agreement on environment unites voters who disagree on economics, social values, and institutional trust. The manifold sees the coalition. The 1D axis cannot.*

---

## The Geometry of Coalition

If voting collapses the manifold to a scalar, coalition building partially preserves it. A coalition is a subset of voters or political actors who agree to coordinate despite disagreeing on some dimensions. They share a connected submanifold on which their positions are close, even if their positions on other dimensions are far apart.

Coalition building is the search for this shared submanifold — the process of identifying which dimensions unite potential partners and which dimensions divide them, then constructing a political program that emphasizes the uniting dimensions and brackets the dividing ones.

**Definition 6 (Agreement Submanifold).** *For a coalition $C = \{v_1, \ldots, v_k\}$ of $k$ agents on the preference manifold $\mathcal{P}$, the agreement submanifold $A_C$ is the subspace of $\mathcal{P}$ on which all coalition members' positions are within $\epsilon$ of each other:*

$$A_C = \{d_i : \max_{v_a, v_b \in C} |v_a^{(i)} - v_b^{(i)}| \leq \epsilon\}$$

*The dimensionality of $A_C$ measures the depth of the coalition: a coalition that agrees on one dimension ($\dim(A_C) = 1$) is fragile; a coalition that agrees on four dimensions ($\dim(A_C) = 4$) is robust.*

**Definition 7 (Pareto-Optimal Coalition).** *A coalition $C$ is Pareto-optimal on the manifold if there is no alternative coalition $C'$ of the same size that is strictly better for all members — closer to each member's ideal point on the manifold. Formally, $C$ is Pareto-optimal if there is no $C'$ with $|C'| = |C|$ such that $d_\mathcal{P}(v, \mu_{C'}) \leq d_\mathcal{P}(v, \mu_C)$ for all $v \in C$ and strictly less for at least one $v$.*

## The Coalition Geometry of American Politics

The two major American party coalitions, analyzed geometrically, have surprisingly thin agreement submanifolds.

### The Democratic Coalition (circa 2024)

The Democratic coalition's agreement submanifold $A_D$ spans primarily:
- $d_1$ (economic progressivism): broad agreement on the direction, disagreement on the extent
- $d_3$ (environmental priority): broad agreement on urgency, disagreement on policy instruments

The internal disagreement dimensions include:
- $d_2$ (social values): progressive urban voters vs. moderate suburban voters vs. socially conservative rural Democrats
- $d_4$ (foreign policy): interventionist hawks vs. non-interventionist progressives
- $d_5$ (trust): high-trust institutionalists vs. low-trust left-populists
- $d_6$ (identity): identity-centered activists vs. universalist moderates

The effective dimensionality of $A_D$ is approximately 2. The Democratic coalition is built on a two-dimensional foundation (economics + environment) and held together by shared opposition to the Republican coalition on $d_2$ — not by shared agreement on $d_2$ but by a shared perception that the Republican position on $d_2$ is unacceptable.

### The Republican Coalition (circa 2024)

The Republican coalition's agreement submanifold $A_R$ spans primarily:
- $d_2$ (social conservatism): broad agreement on traditional values, religious liberty, law and order
- $d_5$-$d_6$ (institutional distrust + identity): the populist synthesis that holds the coalition together

The internal disagreement dimensions include:
- $d_1$ (economics): free-market libertarians vs. economic populists (the defining tension since 2015)
- $d_3$ (environment): climate skeptics vs. conservation-minded traditionalists
- $d_4$ (foreign policy): hawks vs. isolationists (the defining tension since 2016)

The effective dimensionality of $A_R$ is also approximately 2. The Republican coalition is built on social conservatism and the trust-identity nexus, with deep internal disagreements on economics and foreign policy that the coalition manages by emphasizing $d_2$ and $d_5$-$d_6$ at the expense of $d_1$ and $d_4$.

Both coalitions have $\dim(A) \approx 2$ — both are built on thin geometric foundations. Both manage their internal disagreements by emphasizing the agreement dimensions and suppressing the disagreement dimensions. Both are vulnerable to events or politicians that activate the disagreement dimensions: the Republican trade debate (2015-2020) activated $d_1$ disagreement, nearly fracturing the coalition; the Democratic policing debate (2020) activated $d_2$ and $d_5$ disagreement.

## Coalition Fragility and the Manifold

A coalition fractures when external events or internal dynamics increase the variance of members' positions on a dimension that was previously within $A_C$.

**Theorem 6 (Coalition Fragility).** *A coalition $C$ with agreement submanifold $A_C$ of dimension $\dim(A_C) = k$ is vulnerable to fracture on any dimension $d_i \notin A_C$ for which the within-coalition variance $\sigma_i^2(C)$ exceeds the tolerance threshold $\epsilon^2$. The fragility index of the coalition is:*

$$F(C) = \frac{d - \dim(A_C)}{d} \cdot \max_{d_i \notin A_C} \frac{\sigma_i^2(C)}{\epsilon^2}$$

*A coalition with $F(C) > 1$ is geometrically fragile: it contains more disagreement energy on its worst dimension than its agreement structure can contain.*

For the American party coalitions with $\dim(A) \approx 2$ and $d = 6$, the fragility coefficient $(d - \dim(A))/d = 4/6 \approx 0.67$, meaning that the fragility index reaches 1 (the fracture threshold) when the within-coalition variance on the worst disagreement dimension exceeds $1.5 \cdot \epsilon^2$. Both coalitions are operating near this threshold, explaining the persistent anxiety within both parties about coalition stability.

## Cross-Partisan Coalitions on the Manifold

The most geometrically interesting coalitions are cross-partisan: they unite voters from opposing parties who agree on a suppressed dimension.

In the 1D party system, cross-partisan agreement is invisible. Voters who agree on $d_3$ (environment) but disagree on $d_1$ (economics) are placed on opposite sides of the left-right axis. Their agreement on $d_3$ cannot be expressed through the voting system, because the voting system projects onto $d_1$ (or the $d_1$-$d_2$ diagonal), and the $d_3$ agreement is orthogonal to this projection.

On the manifold, the cross-partisan coalition is visible. Voters from both parties who share a region of $d_3$ space form a connected submanifold on the environmental dimension. The coalition exists; the voting system simply cannot see it.

### When Cross-Partisan Coalitions Succeed

Cross-partisan coalitions succeed when the suppressed dimension is activated — when the electoral or legislative process projects onto the agreement dimension rather than the disagreement dimension. This happens most often in:

- **Ballot initiatives and referenda:** These project onto a specific policy dimension ($d_3$ for an environmental measure, $d_1$ for a tax measure), bypassing the party system's dimensional bundling. The environmental bond measure in District 7 is an example.

- **Local politics:** Local issues (infrastructure, schools, zoning) often activate dimensions ($d_1$, $d_3$) that are independent of the national partisan axis ($d_1$-$d_2$ diagonal). Cross-partisan coalitions are more common and more successful at the local level because the projection axis is local rather than national.

- **Issue-specific legislative coalitions:** In legislatures, cross-partisan coalitions form on specific votes that activate suppressed dimensions. The bipartisan infrastructure bill (2021) activated $d_1$ (economic investment) in a way that cross-cut the partisan $d_1$-$d_2$ diagonal, allowing center-right Republicans to vote with Democrats on a $d_1$ position without conceding anything on $d_2$.

## The Bond Geodesic Equilibrium for Coalitions

Coalition formation has the structure of a multi-agent equilibrium problem, connecting to the Bond Geodesic Equilibrium from *Geometric Economics* (Ch. 7).

Each potential coalition member faces a decision: join the coalition (and compromise their position to the coalition's agreement region) or stay independent (and maintain their ideal position but forfeit the coalition's collective benefits). The BGE for coalition formation is the stable partition of the electorate into coalitions where no voter can improve their representation by switching coalitions.

Formally, let $\{C_1, \ldots, C_m\}$ be a partition of voters into $m$ coalitions (including the possibility of single-member "coalitions" for independent voters). The partition is a coalition BGE if no voter $v$ has a lower behavioral friction in any alternative coalition $C_j$ than in their current coalition $C_i$:

$$\text{BF}(v, C_i) \leq \text{BF}(v, C_j) \quad \forall v \in C_i, \forall j \neq i$$

where $\text{BF}(v, C)$ is the cost to voter $v$ of membership in coalition $C$ — the manifold distance between $v$'s ideal position and the coalition's agreed-upon position on the agreement submanifold.

The coalition BGE predicts that voters will sort into coalitions that minimize their representational cost on the manifold — not on the 1D axis. The two-party system is a stable equilibrium only if the two-party partition is the BGE — which requires that no voter can achieve lower manifold-distance representation by switching parties or joining a third party. When the manifold structure changes (new dimensions become salient, old correlations weaken), the two-party equilibrium can become unstable, and realignment — the formation of new coalitions around new agreement submanifolds — becomes possible.

## District 7: The Bond Measure Coalition

The environmental bond measure in District 7 assembles a cross-partisan coalition:

- **Progressive urban voters** (30% of district): Support on $d_3$ (environmental priority) and $d_1$ (public investment). Manifold distance to the bond measure's position: 0.8.
- **Moderate suburban parents** (25%): Support on $d_3$ (clean air for children, reduced commute) and $d_1$ (infrastructure investment). Manifold distance: 1.2.
- **Libertarian exurban voters** (10%): Support on $d_3$ (conservation easement protects property values). Oppose the tax increase ($d_1$) but accept it as the price of development restriction. Manifold distance: 2.0.
- **Retired pragmatists** (8%): Support on $d_1$ (infrastructure as sensible investment) and moderate $d_3$. Manifold distance: 1.5.

Total support: approximately 73% — well above the 60% threshold, if the coalition holds.

On the left-right axis, this coalition is incoherent: it includes voters from every point on the spectrum. The political consultant, analyzing the district through the 1D lens, advises that the measure "can't pass because it doesn't have a partisan base." The consultant is thinking one-dimensionally.

On the manifold, the coalition occupies a connected region of $d_3$ space. The agreement submanifold $A_C$ has dimension 1 (agreement on environmental priority) with supplementary agreement on $d_1$ for most members. The coalition is fragile on $d_2$ (social values divide the urban progressives from the exurban libertarians) and $d_5$ (institutional trust divides the suburban moderates from the exurban populists). A campaign that reframes the bond measure as a social issue ($d_2$) or an institutional issue ($d_5$) could fracture the coalition by activating the disagreement dimensions.

The bond measure's advocates, intuitively understanding the manifold geometry, keep the campaign focused on $d_3$: clean energy, clean air, open space, property values. They avoid $d_2$ (no social commentary) and $d_5$ (no institutional arguments — no "trust the government" messaging). The campaign holds the coalition together by holding the projection axis on the agreement dimension.

The measure passes with 62% support.

---

> **DISTRICT 7 — CHAPTER SUMMARY**
>
> *We have analyzed coalition building as a search for shared submanifolds on the political preference manifold. A coalition's depth is measured by the dimensionality of its agreement submanifold; its fragility is measured by the variance of its members on disagreement dimensions. Both major American party coalitions have agreement submanifolds of dimension approximately 2, making them geometrically fragile.*
>
> *Cross-partisan coalitions — united on suppressed dimensions that the 1D axis cannot see — are visible on the manifold and can succeed when the electoral process activates the agreement dimension. In District 7, a cross-partisan environmental coalition spanning the full left-right spectrum passes a bond measure by holding the campaign's projection axis on the shared environmental dimension.*
>
> *Part IV turns to democratic design: how can voting systems be redesigned to preserve more manifold structure? Chapter 13 begins with ranked-choice voting and the RCV Recovery Theorem.*
