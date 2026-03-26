# Chapter 15: The Political Bond Index

> *"What gets measured gets managed. What gets measured badly gets managed badly."*
> — Adapted from Drucker and Deming

---

> **RUNNING EXAMPLE — DISTRICT 7**
>
> *Three redistricting maps for District 7 sit on the table (Chapter 9). A ranked-choice voting proposal is under consideration (Chapter 13). A citizens' assembly has produced a transportation recommendation (Chapter 14). How do we compare these institutional alternatives? What metric tells us which map, which voting system, which process better represents the voters of District 7?*
>
> *The answer is the Political Bond Index: a single number that measures the systematic gap between how well voters are represented and how well they could be represented — computed on the full manifold, not on the 1D projection.*

---

## The General Construction

The Political Bond Index is the political instantiation of the general Bond Index from *Geometric Ethics* (Ch. 16). Across the Geometric Series, the Bond Index measures the expected deviation between the manifold-optimal path and the institutionally constrained path:

- In ethics, the Bond Index measures the gap between the moral geodesic (the ethically optimal trajectory) and the institutional trajectory (what the system actually does).
- In medicine, the clinical Bond Index measures the gap between the clinical geodesic and the institutional protocol.
- In law, the Legal Bond Index measures sentencing disparity — the gap between gauge-invariant sentencing and actual sentencing.
- In economics, the Bond Index measures the gap between the BGE and the Nash equilibrium.

In politics, the Bond Index measures representational quality: the systematic gap between how well voters are represented under a given electoral system and how well they could be represented under manifold-optimal assignment.

**Definition 8 (Political Bond Index).** *Let $S$ be a set of voters on the political preference manifold $\mathcal{P}$, and let $E$ be an electoral system that produces representatives $r(v)$ for each voter $v$. The Political Bond Index is:*

$$BI(S, E) = \mathbb{E}_{v \in S}\left[d_\mathcal{P}(v, r(v)) - d_\mathcal{P}(v, r^*(v))\right]$$

*where:*
- *$d_\mathcal{P}(v, r(v))$ is the manifold distance between voter $v$ and their actual representative $r(v)$ under electoral system $E$*
- *$d_\mathcal{P}(v, r^*(v))$ is the manifold distance between voter $v$ and their closest possible representative $r^*(v)$ under an unconstrained manifold-optimal assignment*
- *The expectation is over the voter population $S$*

The Political Bond Index is always non-negative: $BI(S, E) \geq 0$, because $d_\mathcal{P}(v, r(v)) \geq d_\mathcal{P}(v, r^*(v))$ by definition ($r^*$ is optimal). A perfect electoral system — one where every voter is represented by a manifold-nearest official — has $BI = 0$. Real electoral systems have $BI > 0$, and the magnitude measures the systematic representational gap.

## What the Political Bond Index Detects

The Political Bond Index is a manifold-level diagnostic: it detects representational failures that are invisible to 1D metrics.

### Gerrymandering Detection

A gerrymandered map produces representatives who are manifold-far from their constituents (high $BI$) even though they win elections (1D-close). The gerrymander's distortion is precisely the kind of manifold surgery that increases voter-representative distances while preserving or reducing 1D metrics.

From Chapter 9's analysis of District 7:
- Map A (bipartisan): $BI = 1.2$
- Map B (partisan gerrymander): $BI = 2.8$
- Map C (algorithmic): $BI = 1.5$

Map B's elevated $BI$ detects the gerrymandering that the efficiency gap missed. The excess $BI$ is concentrated on $d_5$ and $d_6$ (trust and identity), confirming that the gerrymander exploited the trust-identity dimension specifically.

### Minority Vote Dilution

When a racial or ethnic minority is cracked across districts, the minority voters' manifold positions are systematically far from any winning candidate. The Political Bond Index computed for the minority subpopulation reveals this:

$$BI(S_{\text{minority}}, E) \gg BI(S_{\text{majority}}, E)$$

This inequality is the geometric signature of vote dilution. It detects the same phenomenon that Section 2 of the Voting Rights Act is designed to prevent, but it detects it on the full manifold rather than on the single dimension of racial representation.

In District 7 under Map B, the Bond Index for Eastfield's historically Black voters is 3.5, compared to 2.4 for the district as a whole. The excess — 1.1 units — quantifies the manifold cost of cracking Eastfield from its natural coalition partners.

### Dimensional Suppression Detection

When the electoral system rewards candidates who differentiate on $d_1$ and $d_2$ and ignores $d_3$ through $d_6$, all voters are poorly represented on the suppressed dimensions. The Political Bond Index, computed dimension by dimension, reveals which dimensions the electoral system serves and which it ignores.

**Dimension-Specific Bond Index:**

$$BI_i(S, E) = \mathbb{E}_{v \in S}\left[|v^{(i)} - r(v)^{(i)}| - |v^{(i)} - r^*(v)^{(i)}|\right]$$

For District 7 under plurality:
- $BI_1$ (economics) = 0.8 — moderate gap; the electoral system partially represents economic preferences
- $BI_2$ (social values) = 0.6 — decent representation on the dimension campaigns emphasize
- $BI_3$ (environment) = 2.1 — large gap; the electoral system barely represents environmental preferences
- $BI_4$ (foreign policy) = 1.8 — large gap
- $BI_5$ (trust) = 2.4 — very large gap; despite trust being the dominant axis of voter variance, the electoral system does not represent it
- $BI_6$ (identity) = 1.5 — moderate gap

The dimension-specific analysis reveals that District 7's voters are well-represented on $d_1$ and $d_2$ (the dimensions that campaigns contest) and poorly represented on $d_3$, $d_4$, $d_5$, and $d_6$ (the dimensions the electoral system ignores). The voters' positions on these dimensions exist — they are measured by surveys, they influence behavior, they shape political identity — but they are invisible to the electoral system and therefore unrepresented.

### Electoral System Comparison

The Political Bond Index enables principled comparison across electoral systems applied to the same electorate:

| Electoral System | $BI(S, E)$ | Information Preserved |
|---|---|---|
| Plurality | 2.8 | 17% |
| Top-two primary | 2.5 | 20% |
| Approval voting | 1.8 | 33% |
| Ranked-choice voting | 1.4 | 45% |
| Condorcet | 1.2 | 50% |
| Multi-member proportional | 0.9 | 60% |

The ordering is monotonic and consistent with the RCV Recovery Theorem: systems that elicit more preference information produce lower $BI$ scores — they represent voters better on the manifold.

## Empirical Estimation

The Political Bond Index requires two inputs: manifold distance estimates and representative positions. Both can be estimated from available data.

**Manifold distance estimation.** Voter positions on the six-dimensional manifold are estimated from survey data — ANES, the Cooperative Election Study, or purpose-built instruments that elicit positions on all six dimensions. The Mahalanobis distance with the empirical covariance matrix provides the manifold distance estimate.

**Representative positions.** Representative positions on the manifold are estimated from roll-call votes (DW-NOMINATE provides positions on the first two dimensions), public statements (content analysis provides positions on $d_2$, $d_5$, $d_6$), and policy positions (platform analysis provides positions on $d_1$, $d_3$, $d_4$).

**Optimal assignment.** The manifold-optimal assignment $r^*(v)$ is computed as the minimum-cost bipartite matching between voters and a hypothetical pool of representatives drawn from the same population. This represents the representation quality that would be achieved if representatives were assigned to minimize total manifold distance — the theoretical optimum.

The computation is feasible for any district with available survey data and roll-call records. The chapter provides worked examples for several real congressional districts, comparing $BI$ across actual versus counterfactual electoral systems.

## Subgroup Analysis: Who Is Best and Worst Represented?

The Political Bond Index can be computed for any subpopulation of voters, revealing which groups are well-represented by the electoral system and which are systematically underrepresented.

**By geography:** Voters in the urban core of District 7 have $BI_{\text{urban}} = 1.8$ under the current plurality system — their representative is nearly 2 manifold units farther from them than optimal. Suburban voters have $BI_{\text{suburban}} = 0.6$ — they are relatively well-represented, because the representative's manifold position (moderate on most dimensions) is closest to the suburban centroid. Exurban voters have $BI_{\text{exurban}} = 1.5$ — poorly represented on the trust-identity dimension ($d_5$-$d_6$), which is their dominant axis of preference but is not contested in the election.

**By demographics:** The dimension-specific Bond Index reveals systematic representational patterns:
- College-educated voters: well-represented on $d_1$ and $d_3$ (the dimensions that educated voters weight most heavily coincide with the dimensions the electoral system contests), poorly represented on $d_5$ (their high institutional trust is not reflected by either major party's candidates).
- Working-class voters: poorly represented on $d_1$ (their economic positions — pro-redistribution, anti-free-trade — are at odds with both parties' economic platforms), well-represented on $d_2$ (social conservatism is well-represented by the Republican candidate).
- Young voters: very poorly represented on $d_3$ (their environmental urgency far exceeds either candidate's position) and $d_5$ (their low institutional trust is not captured by the moderate candidates), well-represented on $d_2$ (social liberalism).
- Minority voters: poorly represented across all dimensions under the gerrymandered map ($BI_{\text{minority}} = 3.5$), reflecting both cracking (the community is split across districts) and dimensional suppression (the issues that matter most to minority voters — institutional accountability, identity recognition — are not contested in the election).

The subgroup analysis transforms the Bond Index from a district-level summary to a diagnostic tool for representational equity. A low average $BI$ can mask large subgroup disparities: a district where suburban voters have $BI = 0.3$ and urban voters have $BI = 3.0$ has an average $BI$ of approximately 1.2 — which looks acceptable — while containing a severe representational inequality.

The equity criterion: an electoral system is equitable if its subgroup Bond Indices do not vary systematically by race, income, education, or geography. An inequitable system has subgroup $BI$ that correlates with demographic characteristics — some groups are structurally better represented than others, not because of their manifold positions but because of the electoral system's dimensional focus.

## Connection to Other Bond Indices

The Political Bond Index is one instance of a construction that appears across the Geometric Series:

| Domain | Bond Index Measures | Key Insight |
|---|---|---|
| Ethics | Gap between moral geodesic and institutional action | Institutions systematically deviate from moral optima |
| Medicine | Gap between clinical geodesic and protocol | Protocols sacrifice patient-specific optimization |
| Law | Sentencing disparity under gauge transformation | Injustice is a measurable geometric quantity |
| Economics | Gap between BGE and Nash equilibrium | Scalar equilibria miss manifold optima |
| **Politics** | **Gap between voter and representative on the manifold** | **Electoral systems lose dimensional information** |

All are instances of the same geometric construction: the expected deviation between the manifold-optimal path and the institutionally constrained path. The construction is domain-independent — it applies wherever institutions map multi-dimensional realities to low-dimensional outputs. The unifying insight of the Geometric Series is that this deviation is measurable, and measuring it is the first step toward reducing it.

## District 7: The Numbers

We compute the Political Bond Index for District 7 under three scenarios:

**Scenario 1: Current system (plurality, Map A).** $BI = 1.2$. The voters are moderately well-represented on $d_1$ and $d_2$ but poorly represented on $d_3$-$d_6$. The total representational gap is driven primarily by the suppressed dimensions.

**Scenario 2: Gerrymandered system (plurality, Map B).** $BI = 2.8$. The gerrymandered map more than doubles the representational gap by cracking communities of interest and creating districts whose manifold structure is distorted. The excess $BI$ is concentrated among Eastfield's voters (whose community has been cracked) and the exurban populists (whose trust-identity voice has been diluted).

**Scenario 3: Reformed system (RCV, Map A).** $BI = 0.9$. The combination of ranked-choice voting (which recovers manifold information) and a fair district map (which preserves communities of interest) reduces the representational gap by 25% relative to Scenario 1 and 68% relative to Scenario 2.

The numbers make the abstract framework concrete. A $BI$ of 2.8 means that the average voter in District 7 under the gerrymandered map is 2.8 Mahalanobis units farther from their representative than they would be under optimal assignment — a gap that corresponds to disagreement on multiple dimensions, manifesting as the feeling that "my representative doesn't represent me." A $BI$ of 0.9 under the reformed system means that the representational gap has been reduced to less than one unit — still nonzero (the Democratic Irrecoverability Theorem guarantees nonzero $BI$ for any contraction), but small enough that most voters feel their representative is "close enough" on the manifold.

---

> **DISTRICT 7 — CHAPTER SUMMARY**
>
> *We have introduced the Political Bond Index — the geometric measure of representational quality that detects gerrymandering, minority vote dilution, dimensional suppression, and cross-system representational differences. The index is computed on the full preference manifold, capturing failures that 1D metrics miss.*
>
> *For District 7, the Bond Index reveals that the gerrymandered map (BI = 2.8) more than doubles the representational gap relative to the fair map (BI = 1.2), and that adopting ranked-choice voting further reduces the gap (BI = 0.9). The numbers quantify what the geometry predicts: more manifold-preserving systems produce more representative outcomes.*
>
> *Part V looks to the horizon: AI in politics (Chapter 16), what politics teaches the general theory (Chapter 17), and the open questions that remain (Chapter 18).*
