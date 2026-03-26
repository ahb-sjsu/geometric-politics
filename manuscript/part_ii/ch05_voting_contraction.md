# Chapter 5: Voting as Forced Contraction — The Democratic Irrecoverability Theorem

> *"Democracy is the worst form of government, except for all those other forms that have been tried."*
> — Winston Churchill

---

> **RUNNING EXAMPLE — DISTRICT 7**
>
> *District 7 holds an election. Five candidates compete. 200,000 voters cast ballots. The voting system — plurality — asks each voter a single question: "Which candidate do you prefer?" The voter, who holds a position on the six-dimensional preference manifold, must project that position onto the set of five candidates and select the one whose manifold position is closest to their own. Then the system counts the first-choice votes and declares a winner.*
>
> *The process takes a six-dimensional distribution of 200,000 points, compresses each point to a label from a five-element set, aggregates the labels by counting, and outputs a single name. The information flow is: $\mathbb{R}^6 \times 200{,}000 \to \{C_1, \ldots, C_5\}^{200{,}000} \to \mathbb{N}^5 \to \{C_1, \ldots, C_5\}$. At each stage, information is destroyed. At the final stage, a single winner emerges from a process that has discarded essentially everything about the electorate except which candidate was most frequently ranked first.*
>
> *This chapter asks: how much information does the process destroy? The answer is the Democratic Irrecoverability Theorem.*

---

## The Voting Function

A vote is a function. Let us formalize it.

**Definition 1 (Preference Configuration).** A *preference configuration* is a function $\phi: V \to \mathcal{P}$ that assigns to each voter $v \in V$ a position $\phi(v) \in \mathcal{P}$ on the $d$-dimensional political preference manifold.

**Definition 2 (Voting Function).** A *voting function* is a map $\mathcal{V}: \mathcal{P}^n \to \mathcal{O}$ that takes the preference positions of $n$ voters and produces an outcome in the outcome space $\mathcal{O}$.

The outcome space depends on the type of election:
- **Plurality election:** $\mathcal{O} = \{C_1, \ldots, C_m\}$ (the set of candidates); $\mathcal{V}$ selects the candidate with the most first-choice votes.
- **Referendum:** $\mathcal{O} = \{\text{yes}, \text{no}\}$; $\mathcal{V}$ is majority rule.
- **Ranked-choice election:** $\mathcal{O} = \{C_1, \ldots, C_m\}$; $\mathcal{V}$ uses iterative elimination.
- **Approval voting:** $\mathcal{O} = \{C_1, \ldots, C_m\}$; $\mathcal{V}$ selects the candidate approved by the most voters.
- **Proportional representation:** $\mathcal{O} = \Delta^{m-1}$ (the simplex of seat allocations); $\mathcal{V}$ assigns seats proportionally.

In every case, $\dim(\mathcal{O}) \ll \dim(\mathcal{P}^n) = n \cdot d$. The voting function is a contraction — a dimensionality-reducing map — and the dimensionality reduction is extreme. For District 7 with $n = 200{,}000$ and $d = 6$, the input space has dimension 1,200,000. The output space has dimension 1 (a single winner). The contraction ratio is 1:1,200,000.

## Non-Injectivity: The Core Problem

A contraction with such extreme dimensionality reduction is necessarily non-injective: many different preference configurations produce the same outcome.

**Lemma 1 (Non-Injectivity of Voting).** For any voting function $\mathcal{V}: \mathcal{P}^n \to \mathcal{O}$ with $\dim(\mathcal{O}) < n \cdot d$, there exist distinct preference configurations $\phi_1 \neq \phi_2$ such that $\mathcal{V}(\phi_1) = \mathcal{V}(\phi_2)$.

*Proof.* The map $\mathcal{V}$ is a function from a space of dimension $n \cdot d$ to a space of dimension $\dim(\mathcal{O})$. If $\dim(\mathcal{O}) < n \cdot d$, then by the rank theorem, the fibers $\mathcal{V}^{-1}(o)$ for each outcome $o \in \mathcal{O}$ have dimension at least $n \cdot d - \dim(\mathcal{O}) > 0$. Each fiber contains infinitely many preference configurations, all producing the same outcome. $\square$

The non-injectivity means that the election outcome does not determine the preference configuration. Two different electorates — with different manifold structures, different preference distributions, different internal disagreements — can produce identical election results. The election does not reveal the electorate. It reveals a shadow.

## The Democratic Irrecoverability Theorem

The non-injectivity established by Lemma 1 is the shadow of a deeper result: the information destroyed by the voting function is not merely lost but *irrecoverable*.

**Theorem 1 (Democratic Irrecoverability).** *Let $\mathcal{V}: \mathcal{P}^n \to \mathcal{O}$ be any voting function with $\dim(\mathcal{O}) < \dim(\mathcal{P}) = d$. Then:*

*(a) $\mathcal{V}$ is non-injective: distinct preference configurations can produce identical outcomes.*

*(b) The information destroyed by $\mathcal{V}$ is irrecoverable: there exists no function $\psi: \mathcal{O} \to \mathcal{P}^n$ such that $\psi \circ \mathcal{V} = \text{id}$.*

*(c) The degree of irrecoverability — the fraction of manifold information destroyed — is bounded below by $\frac{d - \dim(\mathcal{O})}{d}$, where $d$ is the effective dimensionality of the preference manifold.*

*Proof.*

*(a) This is Lemma 1.*

*(b) Suppose for contradiction that $\psi: \mathcal{O} \to \mathcal{P}^n$ exists with $\psi \circ \mathcal{V} = \text{id}$. Then $\mathcal{V}$ has a left inverse, which requires $\mathcal{V}$ to be injective. But part (a) shows $\mathcal{V}$ is non-injective. Contradiction. $\square$*

*(c) The mutual information $I(\Phi; \mathcal{V}(\Phi))$ between the preference configuration $\Phi$ (treated as a random variable on $\mathcal{P}^n$) and the election outcome $\mathcal{V}(\Phi)$ is bounded above by the entropy of the outcome: $I(\Phi; \mathcal{V}(\Phi)) \leq H(\mathcal{V}(\Phi)) \leq \log|\mathcal{O}|$. The entropy of the full preference configuration is $H(\Phi) \geq d \cdot H_{\text{per-dim}}$, where $H_{\text{per-dim}}$ is the per-dimension entropy. The fraction of information preserved is at most:*

$$\frac{I(\Phi; \mathcal{V}(\Phi))}{H(\Phi)} \leq \frac{\log|\mathcal{O}|}{d \cdot H_{\text{per-dim}}} \leq \frac{\dim(\mathcal{O})}{d}$$

*The fraction destroyed is at least $1 - \dim(\mathcal{O})/d = (d - \dim(\mathcal{O}))/d$. $\square$*

### What the Theorem Means

For a plurality election ($\dim(\mathcal{O}) \approx 1$ in an information-theoretic sense — the outcome is a single candidate from a small set) on a six-dimensional preference manifold ($d = 6$), the theorem guarantees that at least $5/6 \approx 83\%$ of the manifold information is destroyed.

This is not a pessimistic estimate. It is a lower bound. The actual information loss may be higher, depending on the structure of the preference distribution and the candidates' positions. In District 7, where the preference distribution is anisotropic and the candidates cluster on the $d_1$-$d_2$ plane, the effective information loss exceeds 83% because the candidates do not sample the full manifold — they offer voters a choice along one or two dimensions and are silent on the rest.

The theorem is a political instantiation of the Scalar Irrecoverability Theorem from *Geometric Reasoning* (Ch. 13). The parent theorem states that scalar contractions of manifolds are lossy and the loss is irrecoverable. The Democratic Irrecoverability Theorem instantiates this for the specific contraction that is voting: a map from a multi-dimensional preference space to a low-dimensional outcome space.

## The Representation Paradox

The Democratic Irrecoverability Theorem has an immediate corollary that challenges the concept of political representation.

**Corollary 1 (Representation Paradox).** *An elected representative is a point in outcome space, not in preference space. Two districts with identical election outcomes can have radically different manifold structures. The representative cannot represent what the election cannot measure.*

Consider two versions of District 7:

**Version A:** The district is homogeneous on dimensions $d_2$ through $d_6$ — all voters agree on social values, environmental priority, foreign policy, institutional trust, and identity — but divided on $d_1$ (economic policy). The 50-50 split is an economic split, and the winning candidate's economic position faithfully represents the district's median economic preference.

**Version B:** The district is heterogeneous on all six dimensions, with the 50-50 split arising from a complex interaction of positions across multiple dimensions. The winning candidate shares the district median on $d_1$ but is far from the district's Frechet mean on $d_2$ through $d_6$.

Both versions produce the same election outcome — the same winner, the same margin. The voting function cannot distinguish them. Yet the representative who is a faithful reflection of Version A's preferences is a poor representative of Version B's, because in Version B, the election outcome was determined by one dimension while the district's actual preferences span six.

The representative, having won, claims a mandate. But the mandate extends only to the dimension on which the election was fought. On the other five dimensions — the five-sixths of the manifold that the election could not measure — the representative has no information and no mandate. Their positions on these dimensions are, from the electorate's perspective, random: the election provided no signal about voter preferences on these dimensions, so the representative's alignment with voters on these dimensions is a matter of chance.

## The Democratic Gauge Group

The formal analysis of voting fairness benefits from the machinery of gauge invariance developed in the parent framework.

**Definition 3 (Democratic Gauge Group).** The *democratic gauge group* $G_D$ is the group of transformations on the input of the voting function that should leave the output unchanged. It is generated by:

1. **Voter anonymity ($\tau_A$):** Permuting voter identities should not change the outcome. If voter $v_1$ and voter $v_2$ swap positions on the manifold, the election result should change only insofar as the preference distribution has changed — the identity of who holds which position should be irrelevant.

2. **Option neutrality ($\tau_N$):** Relabeling the candidates should permute the output correspondingly. If candidates $C_1$ and $C_2$ swap labels, the winner should swap accordingly. No candidate has an inherent advantage from their position on the ballot, their name, or their party label — only from their position on the manifold.

3. **Re-description invariance ($\tau_R$):** If the same preferences are expressed in a different format — a different survey instrument, a different ballot design, a different language — the outcome should be unchanged. The voting function should depend on the preferences, not on how they are described.

A voting function that satisfies gauge invariance under $G_D$ is *democratically well-posed*: its outputs depend only on the geometric structure of the preference distribution, not on arbitrary features of the description.

Arrow's fairness axioms — independence of irrelevant alternatives, unanimity, and non-dictatorship — are gauge-invariance conditions. IIA is a form of re-description invariance (the ranking of A vs. B should not depend on C's presence). Unanimity is orientation preservation (if all voters prefer A to B, the social preference should agree). Non-dictatorship is anonymity (no voter's preference should unilaterally determine the outcome).

Arrow's impossibility theorem, which Chapter 7 will analyze in detail, states that no voting function from a multi-dimensional preference space to a one-dimensional ranking can satisfy all three gauge conditions simultaneously. The impossibility is dimensional: the gauge conditions require lossless contraction, and lossless contraction from multiple dimensions to one is impossible. The gauge conditions are not too demanding — the output space is too small.

## District 7: Five Voting Systems, Five Outcomes

We now demonstrate the Democratic Irrecoverability Theorem empirically by applying five voting systems to the same preference configuration of District 7.

The five candidates are positioned on the manifold as follows:

- **Candidate A (progressive):** $(-2.0, -1.5, 1.5, -0.5, 0.0, 0.5)$. Strong progressive on economics and social values, environmentally committed, moderately internationalist.
- **Candidate B (conservative):** $(2.0, 1.5, -1.0, 1.0, -1.5, 1.0)$. Strong conservative on economics and social values, skeptical of environmentalism, isolationist, populist.
- **Candidate C (moderate):** $(0.0, 0.0, 0.5, 0.0, 0.5, 0.0)$. Centrist on all dimensions. Near the manifold center of mass.
- **Candidate D (green populist):** $(-0.5, 0.0, 2.5, 0.5, -1.0, 0.5)$. Moderate on economics, centrist on social values, extremely environmentally committed, mildly isolationist, low-trust.
- **Candidate E (libertarian):** $(1.0, -2.0, 0.0, 1.5, -2.0, -1.0)$. Fiscally conservative, socially very liberal, environmentally indifferent, isolationist, very low trust, cosmopolitan.

The five voting systems produce five different winners:

**1. Plurality:** Each voter selects their closest candidate on the manifold. Candidate A receives 28% (the urban core and university enclave), Candidate B receives 31% (the exurban belt and half of Meadow Pines), Candidate C receives 18% (the inner suburbs), Candidate D receives 14% (environmentally committed voters across the district), and Candidate E receives 9% (libertarian-leaning voters). **Winner: Candidate B (31%).**

**2. Top-two primary:** The top two candidates (A and B) advance to a general election. In the head-to-head, voters who preferred C, D, or E must choose between A and B. Most C voters choose A (closer on the manifold due to $d_2$ and $d_3$). Most D voters choose A (closest on $d_3$). E voters split. **Winner: Candidate A (52%).**

**3. Ranked-choice voting:** Voters rank all five candidates. In the first round, E (9%) is eliminated. E's voters' second choices go primarily to C (libertarians who value centrism) and D (low-trust voters who value environmental action). In the next round, D (now 17%) is still lowest — eliminated. D's votes transfer primarily to A (environmentalists) and C (moderates). C is now at 28%. In the next round, C (28%) is eliminated. C's voters transfer primarily to A (52%). **Winner: Candidate A (52%), but through a different path than the top-two primary.**

**4. Approval voting:** Voters can approve of as many candidates as they want. Most voters approve 2-3 candidates. Candidate C, who is close to many voters on the manifold (near the Frechet mean), is approved by 61% of voters — far more than any other candidate. Candidate A is approved by 47%, Candidate B by 44%, Candidate D by 38%, Candidate E by 22%. **Winner: Candidate C (61% approval).**

**5. Condorcet:** The Condorcet winner is the candidate who beats every other candidate in a pairwise comparison. Candidate C beats A (51-49, winning moderates and some conservatives), beats B (54-46, winning moderates and progressives), beats D (58-42, winning everyone except strong environmentalists), and beats E (65-35, winning almost everyone). **Winner: Candidate C (Condorcet winner).**

Five voting systems. Five outcomes. Two different winners (A, B, or C, depending on the system). The same voters, the same manifold, the same preferences. The outcomes differ because each voting system is a different contraction of the manifold, and each contraction discards different information.

### Information Preservation Ranking

We can compute the Democratic Irrecoverability index for each system:

- **Plurality:** Information preserved $\approx 17\%$. The system uses only first-choice information — a single label per voter.
- **Top-two primary:** Information preserved $\approx 20\%$. Slightly more than plurality because the two-stage process reveals second-choice information for a subset of voters.
- **Ranked-choice voting:** Information preserved $\approx 45\%$. The full ranking reveals ordinal preference along multiple manifold axes.
- **Approval voting:** Information preserved $\approx 33\%$. The approval threshold reveals information about manifold proximity to each candidate but discards cardinal intensity.
- **Condorcet:** Information preserved $\approx 50\%$. Pairwise comparisons across all candidate pairs extract the maximum ordinal information about the manifold.

The ordering is monotonic: systems that elicit more preference information from each voter preserve more manifold structure. The information preserved is never 100% — even the Condorcet method compresses the continuous manifold to ordinal rankings. But the gap between 17% (plurality) and 50% (Condorcet) is enormous. The choice of voting system determines how much of the electorate's geometric structure survives to influence the outcome.

## The Information-Theoretic Perspective

The Democratic Irrecoverability Theorem can be restated in information-theoretic terms, which provides additional intuition.

Consider the preference configuration $\Phi$ as a random variable — a draw from the distribution of possible electorates. The election outcome $\mathcal{V}(\Phi)$ is a function of $\Phi$. The mutual information $I(\Phi; \mathcal{V}(\Phi))$ measures how much the election outcome tells us about the preference configuration:

$$I(\Phi; \mathcal{V}(\Phi)) = H(\Phi) - H(\Phi \mid \mathcal{V}(\Phi))$$

where $H(\Phi)$ is the entropy of the preference configuration (a measure of its total information content) and $H(\Phi \mid \mathcal{V}(\Phi))$ is the conditional entropy — the information about $\Phi$ that remains unknown after observing the election outcome.

For a plurality election with $m$ candidates, the outcome is a single element from a finite set, so $H(\mathcal{V}(\Phi)) \leq \log_2 m$. For a typical election with 2-5 candidates, this is at most $\log_2 5 \approx 2.3$ bits. The entropy of the preference configuration — for 200,000 voters, each with a position on a 6-dimensional continuum — is enormous, bounded below by $n \times d \times h_{\text{per-dim}}$ bits, where $h_{\text{per-dim}}$ is the per-dimension differential entropy. The mutual information is bounded above by $\log_2 m$ bits, so the fraction of information transmitted through the election is:

$$\frac{I(\Phi; \mathcal{V}(\Phi))}{H(\Phi)} \leq \frac{\log_2 m}{n \cdot d \cdot h_{\text{per-dim}}} \approx 0$$

The election transmits essentially zero information about the electorate's preference structure. It reveals the winner — and nothing else. The electorate's distribution, its dimensionality, its covariance structure, its clusters, its cross-partisan agreements, its sacred-value boundaries — all are invisible in the election outcome.

This is not a criticism of elections. It is a mathematical fact about the information capacity of the voting channel. An election with $m$ candidates can transmit at most $\log_2 m$ bits of information. The electorate contains vastly more information than $\log_2 m$ bits. The election cannot transmit what it cannot carry.

The RCV Recovery Theorem (Chapter 13) will show that ranked-choice voting expands the channel capacity: instead of transmitting only the identity of the winner ($\log_2 m$ bits), it transmits the full ranking ($\log_2(m!)$ bits), which is $\log_2(m!) \approx m \log_2 m$ bits — a factor of $m$ improvement. But even this expanded channel is a tiny fraction of the electorate's total information content. The fundamental asymmetry between the richness of the preference manifold and the poverty of the voting channel is the Democratic Irrecoverability Theorem in information-theoretic dress.

## The Political BIP

The democratic gauge group $G_D$ defines the Political Bond Invariance Principle:

**Axiom (Political BIP).** A democratic evaluation — an election, a poll, a representation assessment — is *epistemically well-posed* if and only if it is invariant under all democratic gauge transformations: voter anonymity, option neutrality, and re-description invariance.

The Political BIP is the political instantiation of the Bond Invariance Principle from *Geometric Ethics* (Ch. 11). It requires that democratic outcomes depend on the geometric structure of the preference distribution — the positions voters hold on the manifold — and not on arbitrary features of the description: which voter holds which position, what the candidates are named, or how the preferences are elicited.

Violations of the Political BIP are systematic democratic failures:

- **Voter suppression** violates anonymity: it makes the outcome depend on *which* voters participate, not just on what preferences are represented.
- **Ballot order effects** violate neutrality: the candidate listed first receives a small but measurable advantage that has nothing to do with manifold position.
- **Framing effects in ballot language** violate re-description invariance: the same policy question, framed differently, produces different outcomes, as established by the 8.9$\sigma$ framing effect from *Geometric Communication*.

The Political Bond Index, introduced in Chapter 15, will measure the magnitude of these violations — the distance between the actual democratic outcome and the gauge-invariant outcome that the manifold structure would produce under a well-posed system.

---

> **DISTRICT 7 — CHAPTER SUMMARY**
>
> *We have formalized voting as a contraction of the political preference manifold and proved the Democratic Irrecoverability Theorem: any voting function that maps a multi-dimensional preference space to a lower-dimensional outcome destroys information irreversibly, with at least $(d - \dim(\mathcal{O}))/d$ of the manifold information lost. For District 7 under plurality voting, this means at least 83% of the electorate's preference structure is destroyed by the act of voting.*
>
> *We have demonstrated this empirically: five voting systems applied to the same preference configuration of District 7 produce five different outcomes, with different winners and different representational qualities. Plurality preserves the least information; Condorcet preserves the most. The choice of voting system is not a technicality — it is a geometric decision about how much of the manifold to discard.*
>
> *In Chapter 6, we turn to the role of campaigns: the heuristic fields that guide voters' attention, shape the projection axis, and determine which dimension of the manifold becomes salient in the election.*
