# Chapter 13: Ranked Choice as Dimensional Recovery — The RCV Recovery Theorem

> *"The perfect is the enemy of the good — but the good is the friend of the manifold."*

---

> **RUNNING EXAMPLE — DISTRICT 7**
>
> *District 7's city council adopts ranked-choice voting for its next election. Under the old plurality system, Candidate A — a firebrand progressive with passionate support in the urban core but little appeal elsewhere — would have won with 28% of the first-choice vote in a five-candidate field. Under RCV, something different happens.*
>
> *In the first round, Candidate E (libertarian, 9%) is eliminated. E's voters' second choices go to Candidate C (moderate, 5%) and Candidate D (green populist, 3%), with 1% to A. In the second round, Candidate D (now 17%) is eliminated. D's voters go to A (8%), C (6%), and B (3%). In the third round, Candidate B (conservative, 34%) and Candidate C (moderate, 29%) face off against Candidate A (37%). C is eliminated. C's voters — the moderate suburban bloc — split: 60% go to A, 40% to B.*
>
> *Final result: Candidate A wins with 54%, defeating Candidate B's 46%. But note what happened: A won not because A was the most popular first choice but because A was an acceptable second or third choice for enough voters across the manifold. The RCV process recovered preference structure — the ordinal rankings beyond first choice — that plurality would have discarded.*
>
> *In an alternative scenario with slightly different candidate positions, Candidate C — the moderate whom nobody loved but everybody tolerated — could have won under RCV by accumulating second-choice votes from all directions. The manifold center of mass, invisible under plurality, becomes visible under RCV.*

---

## The Recovery Problem

The Democratic Irrecoverability Theorem (Chapter 5) proved that voting systems necessarily lose manifold information — the contraction from the six-dimensional preference manifold to a low-dimensional outcome is irreversible and lossy. The theorem sets a floor on information loss: at least $(d - \dim(\mathcal{O}))/d$ of the manifold information is destroyed.

But different voting systems hit different floors. Plurality voting, which uses only each voter's first-choice preference, sits at the bottom: it preserves the least manifold information. Ranked-choice voting, which uses the full ordinal ranking, recovers additional structure. The question is: how much?

The RCV Recovery Theorem, developed in this chapter, answers the question precisely.

## From First Choice to Full Ranking

Under plurality voting, each voter provides a single piece of information: the identity of their most-preferred candidate. This is equivalent to reporting which Voronoi cell of the candidate positions on the manifold the voter occupies — which candidate is nearest in manifold distance. The Voronoi cell carries no information about the voter's position within the cell, their distances to other candidates, or their relative preferences among non-favorite candidates.

Under RCV, each voter provides a complete ordinal ranking of all candidates. This is equivalent to reporting the ordering of all candidate distances from the voter's manifold position: which candidate is nearest, which is second-nearest, and so on. The ranking carries more information than the first-choice alone — it reveals the voter's relative position among all candidates, not just the nearest one.

## The RCV Recovery Theorem

**Theorem 7 (RCV Recovery).** *In a $k$-candidate election on a $d$-dimensional preference manifold, plurality voting uses only the rank-1 projection of each voter's position (the identity of the nearest candidate). RCV uses rank information up to $\min(d, k-1)$, because each successive elimination round reveals additional preference structure. Specifically:*

*(a) Plurality preserves ordinal information along exactly 1 manifold axis (the axis connecting the voter to their first-choice candidate).*

*(b) RCV preserves ordinal information along up to $k-1$ axes (one for each pairwise comparison implicit in the ranking), where the number of independent axes is $\min(d, k-1)$.*

*(c) The information recovery ratio — the fraction of ordinal manifold information preserved by RCV relative to full ordinal information — is:*

$$R_{\text{RCV}} = \frac{\min(d, k-1)}{d}$$

*compared to $R_{\text{plurality}} = 1/d$ for plurality.*

*(d) The recovery is partial: RCV compresses cardinal intensity (how much a voter prefers A over B) to ordinal ranking (A is ranked above B). The Democratic Irrecoverability Theorem still applies, but the information loss under RCV is strictly less than under plurality.*

*Proof.*

*(a) Under plurality, a voter reports only their first choice — candidate $C_1$. This is equivalent to reporting that the voter lies in the Voronoi cell of $C_1$: the region of the manifold closer to $C_1$ than to any other candidate. The Voronoi cell boundary is a set of hyperplanes perpendicular to the axes connecting $C_1$ to each other candidate. The first-choice report determines which side of each hyperplane the voter is on, but only the hyperplane closest to the voter's position (the one separating $C_1$ from the second-choice $C_2$) carries independent information. This is 1 axis.*

*(b) Under RCV, a voter's ranking $C_1 > C_2 > \cdots > C_k$ determines the voter's position relative to all $\binom{k}{2}$ pairwise comparison hyperplanes. Of these, at most $k-1$ are linearly independent (the ranking is a linear order, which can be represented by $k-1$ pairwise comparisons). On a $d$-dimensional manifold, at most $d$ of these are geometrically independent. Thus, the ranking provides ordinal information along $\min(d, k-1)$ independent axes.*

*(c) The ratio follows directly from (a) and (b): $R_{\text{plurality}} = 1/d$ and $R_{\text{RCV}} = \min(d, k-1)/d$.*

*(d) The information preserved by RCV is ordinal, not cardinal. The ranking $A > B$ does not tell us whether the voter slightly prefers $A$ or overwhelmingly prefers $A$. Cardinal information would provide exact manifold distances; ordinal information provides only their ordering. The Scalar Irrecoverability Theorem applies to the ordinal-to-cardinal compression, which is an additional information loss beyond the manifold-to-outcome compression. $\square$*

### What RCV Recovers

The RCV Recovery Theorem identifies three specific pathologies of plurality voting that RCV prevents by recovering additional manifold structure:

**Spoiler effects.** Under plurality, a third candidate $C_3$ who is close to $C_1$ on the manifold can "split the vote" with $C_1$, causing the election of $C_2$ even though a majority prefers $C_1$ to $C_2$. The spoiler effect occurs because plurality does not see the manifold proximity of $C_1$ and $C_3$ — it sees only that $C_3$ received some first-choice votes that would have gone to $C_1$. RCV sees the proximity: voters who ranked $C_3$ first and $C_1$ second transfer their support to $C_1$ when $C_3$ is eliminated. The manifold proximity is recovered.

**Center squeeze.** A centrist candidate — close to the manifold center of mass — can be eliminated first under plurality because they are few voters' top choice (they are too far from the extremes to be anyone's nearest candidate, even though they are everyone's second or third nearest). RCV recovers the second-choice information: as extremes are eliminated, their voters' second choices (often the centrist) accumulate, allowing the centrist to survive the elimination rounds. The centrist, who is the Frechet mean of the electorate, is penalized by plurality and rewarded by RCV.

**Strategic voting.** Under plurality, a voter whose true preference is $C_3$ but who perceives $C_3$ as unviable may strategically vote for $C_1$ (the "lesser evil") to prevent $C_2$ from winning. This strategic misrepresentation corrupts the manifold signal: the voter's reported preference ($C_1$) differs from their actual preference ($C_3$). RCV reduces this incentive: the voter can rank $C_3$ first without fearing the wasted-vote effect, because if $C_3$ is eliminated, the vote transfers to $C_1$. The voter's manifold position is reported more accurately.

### What RCV Does Not Recover

RCV is still a contraction. The information it loses includes:

- **Cardinal intensity.** The voter who ranks A first and B second may slightly prefer A or overwhelmingly prefer A. RCV cannot distinguish these cases.
- **Full manifold structure.** The ranking is an ordinal projection, not a manifold reconstruction. A voter's position on dimensions that do not influence any candidate ranking is invisible to RCV, just as it is invisible to plurality.
- **Cross-dimensional trade-offs.** A voter who would trade two positions on their ranked list for a candidate who matches them on a dimension not represented by any candidate cannot express this trade-off through the ranking.

RCV loses less information than plurality but still loses information. The Democratic Irrecoverability Theorem still applies: any system that maps a multi-dimensional preference to a single winner must lose most of the manifold's structure.

## Approval Voting, Score Voting, and the Dimensional Spectrum

RCV is not the only alternative to plurality. The geometric framework allows comparison across the full spectrum of proposed voting systems:

**Approval voting** allows each voter to approve (vote for) as many candidates as they want. The winner is the candidate with the most approvals. Geometrically, approval voting asks each voter to report which candidates are within a threshold distance on the manifold: "approve" means "this candidate is close enough." The approval threshold is voter-specific (some voters are more permissive, others more selective), which introduces noise into the manifold signal. But approval voting preserves more information than plurality: instead of reporting only the nearest candidate, the voter reports all candidates within their threshold. The manifold proximity structure is partially recovered.

**Score voting** (also called range voting) allows each voter to assign a numerical score (e.g., 0-5) to each candidate. The winner is the candidate with the highest average score. Geometrically, score voting asks each voter to report cardinal distance information: the score for each candidate is an estimate of the voter's manifold distance to that candidate (with closer candidates receiving higher scores). This is the most informationally rich single-winner voting system — it preserves both ordinal and cardinal manifold information. The Democratic Irrecoverability Theorem still applies (the output is a single winner, not the full manifold), but the information available to the contraction is maximized.

**STAR voting** (Score Then Automatic Runoff) combines score voting with a runoff: voters score all candidates, the top two scorers advance to an automatic runoff where the one preferred by more voters wins. STAR adds an ordinal check to the cardinal information, preventing a scenario where a candidate with high scores from a minority but low scores from the majority wins.

**Quadratic voting** assigns each voter a budget of "voice credits" that they can allocate across options, with the cost of additional votes on the same option increasing quadratically. This system is designed for multi-issue decisions (budgets, referenda) rather than candidate elections. It recovers intensity information: a voter who cares deeply about one issue can concentrate their credits on that issue, while a voter who cares moderately about many issues can spread their credits. The quadratic cost function prevents plutocratic domination while allowing intensity expression.

The geometric ranking of these systems, from least to most manifold-preserving:

| System | Information Preserved | Type |
|---|---|---|
| Plurality | Rank-1 only | Ordinal, single |
| Approval | Threshold proximity | Ordinal, binary |
| RCV | Full ordinal ranking | Ordinal, complete |
| Score voting | Cardinal distances | Cardinal |
| Condorcet | All pairwise ordinal | Ordinal, pairwise |
| Multi-member proportional | Multiple winners | Multiple output dimensions |

The progression from plurality to proportional representation is a progression from severe manifold contraction to mild manifold contraction. Each step preserves more dimensional structure, at the cost of greater complexity in the voting process and the counting procedure. The trade-off between simplicity and geometric fidelity is the central design question for electoral reform.

## Empirical Evidence

### Alaska 2022

The Alaska special election of August 2022 is the most dramatic empirical illustration of the RCV Recovery Theorem in American electoral history. Under the new top-four primary and RCV general election system, Democrat Mary Peltola won a congressional seat in a state that had voted Republican in every presidential election since 1964.

The geometric interpretation: Alaska's electorate was multi-dimensional in ways that the 1D Republican label could not capture. The two Republican candidates — Nick Begich III (establishment conservative) and Sarah Palin (populist conservative) — occupied different regions of the manifold: Begich was moderate on $d_5$ (trust) and $d_6$ (identity), while Palin was extreme on both. Peltola occupied a position that was progressive on $d_1$ but moderate on $d_2$ and close to the Alaska electorate's mean on $d_3$ (the environment-resource axis, crucial in Alaska) and $d_4$ (strongly state-sovereignty, which reads as moderate on the national foreign policy axis).

Under plurality, Palin's name recognition would have carried the race. Under RCV, Begich's voters — forced to express second preferences — split between Peltola (manifold-closer on $d_5$ and general temperament) and Palin (manifold-closer on $d_1$ and $d_2$). Enough Begich voters ranked Peltola second to give her the victory.

The RCV system recovered manifold structure that plurality would have discarded: the fact that Begich voters were manifold-closer to Peltola than to Palin on key dimensions, and that their opposition to Peltola on $d_1$ was outweighed by their preference for her on $d_5$.

### New York City 2021

The NYC Democratic mayoral primary — the first major RCV election in New York City — produced Eric Adams as the winner. Under plurality, Adams might also have won (he led in first-choice votes). But the dynamics were different: candidates campaigned not just for first-choice support but for second and third-choice support, encouraging cross-district and cross-demographic appeal. The campaign incentive shifted from "mobilize your base" (a 1D strategy that rewards extremism on the projection axis) to "be everyone's acceptable second choice" (a manifold strategy that rewards proximity to the center of mass).

### Maine 2018 and Beyond

Maine adopted RCV for federal elections in 2018. The most notable effect was the defeat of incumbent Republican Bruce Poliquin by Democrat Jared Golden in the Second Congressional District — a result that would not have occurred under plurality (Poliquin led in first-choice votes). The RCV result reflected the manifold structure: Golden was closer to the district's Frechet mean on the full manifold, even though Poliquin was the plurality leader.

## District 7: The First RCV Election

District 7 holds its first RCV election for city council. Five candidates compete.

Under plurality, Candidate A (strong first-choice support from the urban core, 28%) would have won in a fragmented field. Under RCV:

- Round 1: E (9%) eliminated. Transfers: C gets 5%, D gets 3%, A gets 1%.
- Round 2: D (17%) eliminated. Transfers: A gets 8%, C gets 6%, B gets 3%.
- Round 3: C (29%) vs. A (37%) vs. B (34%). C eliminated. C's transfers: A gets 17%, B gets 12%.
- Final: A (54%) defeats B (46%).

But consider a slight variation: if Candidate C had positioned slightly closer to the manifold center, attracting more first-choice votes from the suburbs, the elimination order changes:

- Round 1: E (9%) eliminated.
- Round 2: D (14%) eliminated.
- Round 3: A (35%) eliminated — A is now lowest. A's transfers: C gets 22%, B gets 13%.
- Final: C (57%) defeats B (43%).

In this scenario, Candidate C — the moderate whom nobody loved but everybody accepted — wins. C is the Frechet mean of the electorate: the candidate closest to the most voters on the full manifold. Under plurality, C would have finished third or fourth. Under RCV, C wins by accumulating second-choice support from across the manifold.

The result surprises the pundits, who expected the race to be "A versus B." The manifold is unsurprised: C was always the central point. The voting system finally saw it.

---

> **DISTRICT 7 — CHAPTER SUMMARY**
>
> *We have proved the RCV Recovery Theorem: ranked-choice voting recovers strictly more manifold information than plurality voting, preserving ordinal information along $\min(d, k-1)$ independent axes compared to plurality's single axis. RCV prevents three specific pathologies of plurality — spoiler effects, center squeeze, and strategic voting — by recovering the second-choice and lower-choice information that plurality discards.*
>
> *In District 7's first RCV election, the system recovered manifold structure that plurality would have destroyed: the moderate candidate, closest to the manifold center of mass, was able to accumulate cross-district second-choice support and win — a result impossible under plurality, where only first-choice intensity counts.*
>
> *Chapter 14 extends the analysis to deliberative democracy: citizens' assemblies and deliberative polls as institutional mechanisms for exploring the manifold directly, rather than contracting it through voting.*
