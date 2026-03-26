# Chapter 7: Arrow's Theorem, Geometrized

> *"If we exclude the possibility of interpersonal comparisons of utility, then the only methods of passing from individual tastes to social preferences which will be satisfactory and which will be defined for a wide range of sets of individual orderings are either imposed or dictatorial."*
> — Kenneth J. Arrow, *Social Choice and Individual Values* (1951)

---

> **RUNNING EXAMPLE — DISTRICT 7**
>
> *Three voter blocs in District 7 — the university enclave, the inner suburbs, and the exurban belt — face a choice among three candidates for a local office. Their preferences cycle:*
>
> *The university enclave (35% of voters) prefers A > B > C.*
> *The inner suburbs (33% of voters) prefers B > C > A.*
> *The exurban belt (32% of voters) prefers C > A > B.*
>
> *Under majority rule: A beats B (67-33), B beats C (68-32), C beats A (65-35). The majority preference cycles: A > B > C > A. There is no Condorcet winner. No matter which candidate is chosen, a majority prefers someone else.*
>
> *Arrow's theorem says this is inevitable: no social welfare function can always avoid such cycles while satisfying three reasonable axioms. The geometric interpretation says something different: the cycle exists on the 1D projection but may not exist on the full manifold. On the six-dimensional preference manifold of District 7, the three blocs' positions may admit a Condorcet winner that the ordinal ranking — which discards all information except order — cannot see.*

---

## Arrow's Theorem: The Standard Statement

Kenneth Arrow's impossibility theorem, published in 1951, is the most important result in social choice theory and one of the most cited theorems in the social sciences. It states that no social welfare function — no systematic procedure for aggregating individual preference orderings into a social preference ordering — can simultaneously satisfy three axioms:

**Axiom 1: Independence of Irrelevant Alternatives (IIA).** The social ranking of alternatives $A$ and $B$ depends only on individuals' rankings of $A$ and $B$, not on their rankings of any other alternative $C$. Adding or removing irrelevant alternatives should not change the relative ranking of A and B.

**Axiom 2: Unanimity (Pareto).** If every individual prefers $A$ to $B$, then the social ranking must prefer $A$ to $B$. The social welfare function respects unanimous agreement.

**Axiom 3: Non-Dictatorship.** There is no individual whose preferences automatically become the social preference regardless of everyone else's preferences. The social welfare function is not a dictatorship.

Arrow proved that for three or more alternatives, no social welfare function defined on the unrestricted domain of preference orderings satisfies all three axioms. The proof is by contradiction: assuming all three axioms, Arrow derived the existence of a dictator, violating Axiom 3.

The standard interpretation of Arrow's theorem is that the three axioms are too demanding — that any aggregation procedure must violate at least one of them, and the choice of voting system is a choice of which axiom to sacrifice. This interpretation treats the result as a counsel of despair: perfect democracy is impossible, and all voting systems are flawed.

The geometric interpretation, developed in this chapter, offers a different reading. The three axioms are not too demanding. The *output space* is too small. Arrow's theorem is a statement about the impossibility of losslessly contracting a multi-dimensional object to a one-dimensional ranking.

## Arrow's Axioms as Geometric Conditions

Each of Arrow's three axioms has a precise geometric interpretation as a condition on the contraction from the preference manifold to the outcome space.

### IIA as Topology Preservation

Independence of Irrelevant Alternatives requires that the social ranking of $A$ versus $B$ depend only on individual rankings of $A$ versus $B$. Geometrically, this is a statement about the projection of the manifold onto the axis connecting $A$ and $B$.

Consider the preference manifold $\mathcal{P}$ with voters distributed across it. The pairwise comparison of $A$ and $B$ is a projection onto the $A$-$B$ axis: the hyperplane bisecting $A$ and $B$ divides the manifold into the region closer to $A$ and the region closer to $B$. IIA requires that this division — the topology of the $A$-$B$ partition — be independent of where $C$ is positioned on the manifold.

But the presence of $C$ affects the topology. If $C$ is close to $A$ on the manifold, then some voters who are between $A$ and $B$ (and prefer $A$ to $B$) may be closer to $C$ than to $A$. The introduction of $C$ changes the partition structure of the manifold — not the $A$-$B$ partition specifically, but the overall partition that determines how voters are aggregated. IIA demands that the $A$-$B$ partition be independent of this global topological change.

IIA is, in essence, a demand for topological locality: the relationship between $A$ and $B$ should depend only on the local structure of the manifold near the $A$-$B$ axis, not on the global structure induced by other alternatives. This is a strong constraint, because on a multi-dimensional manifold, the topology is inherently global — the shape of the manifold in one region affects the geodesic structure in other regions.

### Unanimity as Orientation Preservation

Unanimity requires that if all voters prefer $A$ to $B$, the social preference ranks $A$ above $B$. Geometrically, this is orientation preservation: if all individual projections onto the $A$-$B$ axis point from $B$ toward $A$ (i.e., all voters are on $A$'s side of the $A$-$B$ bisector), then the social projection must point the same way.

Orientation preservation is a natural condition on any contraction. A map that reverses the direction of unanimous agreement is perverse — it takes a manifold where every point is on one side of a hyperplane and produces an output that says the opposite. No reasonable contraction violates orientation preservation.

### Non-Dictatorship as Symmetry Preservation

Non-dictatorship requires that no single voter determines the social preference. Geometrically, this is a symmetry condition: the contraction must respect the gauge group of voter anonymity ($\tau_A$ from Chapter 5). The social preference should be determined by the distribution of voters on the manifold, not by any individual voter's position.

A dictatorship is a contraction that ignores all but one voter: the social preference is the dictator's preference, regardless of everyone else's positions. Geometrically, this is a projection onto a single point's position — the contraction $\mathcal{V}(\phi) = \phi(v_{\text{dictator}})$. The dictatorial contraction preserves topological locality (IIA) and orientation (unanimity) trivially, because it reduces the multi-dimensional input to a single voter's preference. But it violates the gauge symmetry of anonymity: the output depends on which voter is the dictator, not on the geometric structure of the preference distribution.

## The Geometric Impossibility

With the axioms reinterpreted geometrically, the impossibility theorem takes on a new form:

**Theorem 3 (Arrow's Theorem, Geometrized).** *Let $\mathcal{P}$ be a political preference manifold of effective dimension $d \geq 3$. No contraction $\mathcal{V}: \mathcal{P}^n \to \mathcal{R}$ from the manifold to a 1-dimensional social ranking $\mathcal{R}$ can simultaneously preserve:*

*(a) Topology (IIA): the contraction's behavior on any pairwise comparison is independent of alternatives not involved in that comparison.*

*(b) Orientation (Unanimity): the contraction preserves the direction of unanimous agreement.*

*(c) Symmetry (Non-dictatorship): the contraction respects voter anonymity — no single voter's position determines the output.*

*The impossibility is dimensional: a 1D contraction of a $d$-dimensional manifold ($d \geq 3$) must lose $(d-1)$ dimensions of information, and the three conditions together require that no information be lost — an impossible demand.*

### Proof Sketch

The full proof follows Arrow's original argument, reinterpreted geometrically. The key insight is that the three conditions jointly require the contraction to be a homeomorphism from $\mathcal{P}^n$ to $\mathcal{R}$ on the relevant fiber — a smooth, invertible map that preserves topological structure. But a contraction from $d$ dimensions to 1 dimension cannot be a homeomorphism (it is not injective — see Lemma 1 from Chapter 5). The only way to satisfy all three conditions is to make the contraction depend on a single voter's full preference (a dictatorship), which trivially achieves injectivity on the relevant fiber by ignoring all other voters. This is the unique escape from the dimensional constraint, and it violates condition (c). $\square$

### The Resolution Is Dimensional

The standard resolution of Arrow's theorem — accept that one axiom must be violated and choose which one — is correct but incomplete. The geometric resolution is more informative: the problem is not that the axioms are too strong but that the output space is too small.

Consider what happens when the output space is expanded:

- **Output space: ordinal ranking ($\dim \approx 1$).** Arrow's theorem applies. Impossibility.
- **Output space: cardinal scoring ($\dim = m$, where $m$ is the number of candidates).** The Gibbard-Satterthwaite theorem still imposes constraints (strategic voting is possible), but the richer output allows more manifold structure to survive. Cardinal voting systems (range voting, quadratic voting) can satisfy IIA and unanimity simultaneously — they escape the Arrovian impossibility by working in a higher-dimensional output space.
- **Output space: proportional representation ($\dim = m-1$, the simplex of seat shares).** The multi-member output further relaxes the dimensional constraint. Many of the pathologies of single-winner systems — spoiler effects, center squeeze, majority tyranny — are ameliorated.
- **Output space: the full manifold ($\dim = d$).** In principle, a direct-democracy system that preserves the full manifold structure — where the collective decision is a point on the manifold, not a single winner — escapes the Arrovian constraint entirely. The challenge is practical: how do you compute the manifold center of mass of a million voters?

The geometric perspective reframes the question from "which axiom should we sacrifice?" to "how much dimensional expansion can we give the output space?" Chapter 13 will show that ranked-choice voting partially answers this question: by eliciting rank information rather than first-choice-only information, RCV expands the effective output dimension and recovers manifold structure that plurality discards.

## McKelvey's Chaos Theorem, Geometrized

Richard McKelvey's general impossibility result (1976) extends Arrow's theorem to show that in multi-dimensional voting, the majority-rule core is generically empty. For any policy position $p$, there exists another position $q$ such that a majority prefers $q$ to $p$. This means that majority rule can cycle through the entire policy space — any position can be reached from any other position through a sequence of majority-preferred moves.

The geometric interpretation is illuminating: McKelvey's chaos is the manifold's revenge on dimensional collapse.

When a multi-dimensional preference distribution is aggregated by majority rule, each dimension contributes a different majority. On $d_1$, the economic majority may favor policy $p$. On $d_2$, the social majority may favor a different policy $q$. On $d_3$, the environmental majority may favor yet another policy $r$. The "majority" is not a fixed group — it is a different coalition on each dimension. As the agenda moves through different dimensions, the winning coalition shifts, and the resulting trajectory through policy space can visit every region.

The chaos is not a failure of voters' rationality. It is a failure of the aggregation mechanism. Each voter has a consistent position on the manifold — a single point in six-dimensional space. The inconsistency arises when the multi-dimensional positions are aggregated dimension by dimension through binary majority votes. The aggregation creates a "social preference" that cycles, even though no individual preference cycles.

Geometrically, the chaos is a consequence of the non-transitivity of majority rule on multi-dimensional manifolds. On a 1D manifold, majority rule is transitive and the median voter's position is a stable equilibrium (the Condorcet winner). On a manifold with $d \geq 2$, majority rule generically has no stable equilibrium — the median on one dimension is different from the median on another, and the intersection of dimension-specific medians is generically empty.

The resolution, again, is dimensional: expand the output space. Instead of asking "which point on the manifold does the majority prefer?" (a question that may have no answer), ask "what region of the manifold is Pareto-undominated?" (a question that always has an answer, and the answer is the Pareto frontier — a subset of the manifold, not a single point).

## The Gibbard-Satterthwaite Connection

Arrow's theorem addresses the problem of aggregation: can individual preferences be combined into a coherent social preference? The Gibbard-Satterthwaite theorem (1973/1975) addresses the complementary problem of incentives: do voters have incentive to report their true preferences?

The Gibbard-Satterthwaite theorem states that any non-dictatorial voting function for three or more alternatives is susceptible to strategic manipulation: there exists a situation in which some voter can obtain a better outcome by voting for someone other than their true first choice. This is the theoretical foundation for "strategic voting" — the practice of voting for the "lesser evil" rather than the preferred candidate.

The geometric interpretation extends the dimensional analysis. Strategic voting is a distortion of the manifold signal: the voter's reported position differs from their actual position. The voter who truly prefers candidate $C_3$ but strategically votes for $C_1$ (to prevent $C_2$ from winning) is reporting a manifold position near $C_1$ when their actual position is near $C_3$. The election outcome is determined by the reported positions, not the actual positions — so the preference manifold that the election "measures" is systematically distorted by strategic behavior.

The distortion is worst under plurality voting, where the incentive for strategic voting is strongest (the wasted-vote problem), and weakest under Condorcet-consistent methods, where the incentive is minimal (voting for your true preference is always weakly dominant in Condorcet comparisons). RCV falls between these extremes: it reduces the strategic incentive relative to plurality (you can rank your true preference first without the wasted-vote risk) but does not eliminate it entirely (there exist scenarios where ranking a candidate lower can help them win under RCV — the non-monotonicity pathology).

The geometric lesson: the Gibbard-Satterthwaite theorem is not just about strategic incentives. It is about the reliability of the manifold signal. A voting system that incentivizes strategic voting corrupts the signal — the reported preference distribution diverges from the actual preference distribution, and the election outcome reflects the distorted signal rather than the true manifold structure. Systems that reduce strategic incentives (RCV, Condorcet methods) produce more faithful manifold signals — another dimension of the information recovery that Chapter 13 will analyze.

## Sen's Capability Approach and the Manifold

Amartya Sen's capability approach, developed in *Collective Choice and Social Welfare* (1970) and *Development as Freedom* (1999), provides a philosophical foundation for the multi-dimensional treatment of political preference. Sen argued that welfare should be measured not by a single scalar (utility, income) but by a vector of capabilities — the freedoms that a person has to achieve valued functionings. The capability approach is, in essence, a manifold approach: each capability is a dimension of human welfare, and the welfare state is a point on the capability manifold.

The political preference manifold of this book is a Sen-inspired construction. Each of the six dimensions represents a domain of political concern — a capability area in Sen's terms. The voter's position on each dimension reflects their priorities for collective action in that domain. The left-right axis, which compresses all capability domains into a single index, is the political equivalent of the utilitarian welfare function that Sen critiqued: it sacrifices multi-dimensional structure for scalar simplicity, and the sacrifice is irrecoverable.

Sen's critique of utilitarianism — that a single welfare number cannot capture the multi-dimensional nature of human flourishing — is the same critique this book directs at the left-right axis. And Sen's proposed remedy — evaluate welfare on the full capability vector, not on a scalar contraction — is the same remedy this book proposes for political analysis: evaluate preferences on the full manifold, not on a 1D projection.

## District 7: The Cycle That Isn't

Return to the cycling preferences of District 7's three blocs.

On the one-dimensional projection:
- University enclave: $A > B > C$
- Inner suburbs: $B > C > A$
- Exurban belt: $C > A > B$

This is a Condorcet cycle: $A$ beats $B$ (67-33), $B$ beats $C$ (68-32), $C$ beats $A$ (65-35). No Condorcet winner exists.

But now examine the candidates' positions on the full manifold:

- Candidate A: $(-1.5, -1.0, 1.0, 0.0, 0.5, -0.5)$ — progressive, environmentally committed, institutionally moderate
- Candidate B: $(0.0, 0.0, 0.5, 0.0, 0.5, 0.0)$ — centrist, the manifold center of mass
- Candidate C: $(1.5, 1.0, -0.5, 0.5, -1.0, 1.0)$ — conservative, populist

The manifold distances between each bloc's centroid and each candidate:

| | Dist to A | Dist to B | Dist to C |
|---|---|---|---|
| University | 1.2 | 2.5 | 4.8 |
| Suburbs | 2.8 | 0.3 | 2.5 |
| Exurban | 5.1 | 2.2 | 1.4 |

On the full manifold, Candidate B is the nearest candidate to the inner suburbs (distance 0.3) and the second-nearest to both other blocs. The mean manifold distance across the electorate: A = 3.0, B = 1.7, C = 2.9. Candidate B has the lowest mean manifold distance — it is the manifold Condorcet winner, even though the ordinal cycle says no Condorcet winner exists.

The cycle arises because the ordinal ranking discards manifold distance information. The university enclave ranks $A > B > C$ because $A$ is closest on the projection axis that the ranking captures. But the ranking does not record that $B$ is a close second — manifold distance 2.5 versus 1.2, a ratio of 2.1. The exurban belt ranks $C > A > B$ because $C$ is closest on the ranking's projection axis, but $B$ is manifold-close at 2.2 versus $C$'s 1.4, a ratio of 1.6. The ordinal ranking, by discarding these distance ratios, creates a cycle that the cardinal manifold structure does not support.

Arrow's impossibility is real — but its practical severity depends on how much manifold information the voting system discards. Systems that preserve more information (cardinal, ranked, multi-member) are less susceptible to Arrovian pathologies than systems that preserve less (plurality, binary). The impossibility is a feature of the 1D output, not of the preference structure.

---

> **DISTRICT 7 — CHAPTER SUMMARY**
>
> *We have reinterpreted Arrow's impossibility theorem as a statement about the geometry of dimensional collapse. The three axioms — IIA, unanimity, non-dictatorship — are conditions on the contraction from a multi-dimensional preference manifold to a one-dimensional social ranking. The impossibility arises because the contraction is too severe: a 1D output cannot preserve the topology, orientation, and symmetry of a multi-dimensional input simultaneously.*
>
> *In District 7, a Condorcet cycle in ordinal preferences dissolves on the full manifold: Candidate B, the manifold center-of-mass, has the lowest mean distance to the electorate and is the manifold Condorcet winner. The cycle is an artifact of the ordinal projection, not of the preferences.*
>
> *Part III turns from theory to application: polarization (Chapter 8), gerrymandering (Chapter 9), the Overton window (Chapter 10), media (Chapter 11), and coalitions (Chapter 12) — all analyzed through the geometric lens that the first seven chapters have constructed.*
