# Chapter 10: The Overton Window as Geodesic Constraint

> *"The smart way to keep people passive and obedient is to strictly limit the spectrum of acceptable opinion, but allow very lively debate within that spectrum."*
> — Noam Chomsky

---

> **RUNNING EXAMPLE — DISTRICT 7**
>
> *In 1995, a candidate for District 7's city council proposed single-payer healthcare. She was laughed out of the race. In 2015, a candidate proposed the same policy and finished third. In 2025, a candidate proposed it and won.*
>
> *The policy had not changed. The Overton window had moved.*
>
> *In the same period, a candidate who proposed abolishing the local police department in 1995 would have been regarded as a crank. In 2020, after a summer of racial justice protests, the proposal briefly entered mainstream discourse. By 2025, it had receded again, now considered too radical for serious candidacy.*
>
> *The Overton window is not a fixed boundary. It is a dynamic region of the political manifold, and its shape — which positions are "acceptable" and which are "extreme" — constrains the geodesics available to politicians, parties, and movements. This chapter gives the window a geometry.*

---

## The Window on the Manifold

The concept of the Overton window, developed by Joseph Overton at the Mackinac Center for Public Policy, is familiar in political discourse: the range of policies considered politically acceptable at a given time. Positions within the window are "mainstream"; positions outside it are "radical" or "unthinkable." The window can shift — positions that were radical become mainstream, and positions that were mainstream become radical.

The standard account treats the Overton window as a one-dimensional interval on the left-right axis: a range $[a, b]$ on the political spectrum, with $a$ representing the leftmost acceptable position and $b$ the rightmost. This 1D account captures the intuition but, like everything else in politics, it suffers from dimensional compression.

The geometric account treats the Overton window as a connected, bounded subset $W \subset \mathcal{P}$ of the six-dimensional preference manifold. A political position $p$ is within the Overton window if $p \in W$. A position outside the window — $p \notin W$ — is "extreme," "radical," or "unthinkable," depending on its manifold distance from $W$.

The boundary $\partial W$ is not a hard wall but a gradient: positions just outside the window incur modest social costs (raised eyebrows, editorial criticism), while positions far outside incur severe costs (ridicule, marginalization, electoral oblivion). Formally, the boundary acts as a penalty function:

$$\text{cost}_O(p) = \beta_O \cdot d_\mathcal{P}(p, W)^2$$

where $d_\mathcal{P}(p, W) = \inf_{w \in W} d_\mathcal{P}(p, w)$ is the manifold distance from $p$ to the nearest point in $W$, and $\beta_O$ is the penalty coefficient. Positions inside $W$ have zero Overton cost. Positions outside $W$ incur cost proportional to the square of their distance from the window.

## Window Geometry

The Overton window has geometric structure:

**Shape.** The window is not a hypersphere — it is not equally wide in all dimensions. In 2020s American politics, the window is wide on $d_2$ (social values — a broader range of social positions is now considered acceptable than at any time in the past century) and narrow on $d_1$ (economics — the range of "acceptable" economic positions has contracted, with both parties supporting broadly market-oriented policies). The window is irregularly shaped on $d_5$ (trust — anti-institutional positions that were once marginal have entered the mainstream) and asymmetric on $d_6$ (identity — some forms of identity politics are within the window, others are outside).

**Orientation.** The window's principal axis — the direction of greatest width — is not aligned with the left-right axis. In the current American political environment, the principal axis of the Overton window runs approximately along the $d_2$-$d_5$ diagonal: the greatest range of "acceptable" positions spans from socially progressive, institutionally trusting positions to socially conservative, institutionally skeptical positions. This is the axis along which American politics allows the most variation.

**Position.** The window's center is not at the manifold's center of mass. In many Western democracies, the window is offset in the $d_1$ direction: economic positions that are mainstream in Scandinavian countries (comprehensive social democracy) are outside the American Overton window, while positions that are mainstream in America (limited public healthcare, minimal worker protections) are outside the Scandinavian window. The windows of different countries occupy different regions of the same universal preference manifold.

## The Geodesic Constraint

A politician navigating the preference manifold is constrained to Overton-admissible trajectories: paths that remain within $W$. This constraint has profound geometric consequences.

**Definition 5 (Overton-Admissible Trajectory).** *A political trajectory $\gamma: [0,T] \to \mathcal{P}$ (a sequence of positions over time, such as a party platform's evolution or a politician's career arc) is Overton-admissible if $\gamma(t) \in W(t)$ for all $t$, where $W(t)$ is the Overton window at time $t$.*

The geodesic — the shortest path between two positions on the manifold — may pass through regions outside the window. In that case, the politician must take a longer path that stays within $W$, detouring around the forbidden region. The excess path length — the difference between the geodesic and the shortest Overton-admissible path — measures the political cost of the window constraint:

$$\text{Overton cost}(\gamma^*_{\text{admissible}}) = \ell(\gamma^*_{\text{admissible}}) - \ell(\gamma^*_{\text{geodesic}})$$

where $\ell(\cdot)$ is path length on the manifold.

Politicians who successfully shift the window are creating geodesic shortcuts: by expanding $W$, they make previously costly trajectories feasible. The politician who makes single-payer healthcare "thinkable" has expanded the window on $d_1$, creating a shorter path from the current center-left position to the single-payer position. Before the expansion, the path from center-left to single-payer passed through "radical" territory — outside $W$ — and any politician who traveled it incurred severe Overton penalties. After the expansion, the path stays within $W$, and the Overton cost is zero.

## Window Dynamics

The Overton window is not static. It shifts in response to four forces:

### Elite Adoption

When prominent political figures adopt positions outside $W$, the boundary extends to include them. The mechanism is social proof: a position held by a respected, visible figure is harder to dismiss as "extreme." The window expansion is proportional to the figure's prominence and the distance of their position from the window's boundary.

This explains the political strategy of "making the extreme respectable." A figure who deliberately stakes out a position just outside $W$ — far enough to be noticed, close enough to be taken seriously — can shift the window by demonstrating that the position does not produce the social consequences (ridicule, marginalization) that the boundary is supposed to enforce. Each successful transgression of the boundary weakens the boundary.

### Crisis Events

Crises — pandemics, wars, financial crashes, natural disasters — rapidly expand $W$ in crisis-relevant dimensions while contracting it in others. During a pandemic, public health interventions that were previously "unthinkable" (lockdowns, mandatory vaccination, contact tracing) enter the window rapidly. Simultaneously, the window may contract on other dimensions: civil libertarian positions ($d_2$) that were mainstream in peacetime become "irresponsible" during a crisis.

The crisis expansion is often temporary: as the crisis recedes, the window contracts toward its pre-crisis shape. But some crisis-induced expansions are permanent — the position that was "unthinkable" before the crisis and "necessary" during the crisis becomes "normal" after the crisis. The New Deal expanded the Overton window on $d_1$ permanently; positions that were considered socialist in the 1920s (Social Security, unemployment insurance, bank regulation) became permanent fixtures of the window.

### Generational Replacement

As older cohorts exit the electorate and younger cohorts enter, the distribution of "acceptable" positions shifts. Positions that were "extreme" to the older cohort may be "obvious" to the younger one. The window shifts not through persuasion but through demographic replacement.

Generational replacement is the slowest of the four forces but the most durable. A window shift driven by elite adoption or crisis can be reversed; a shift driven by generational replacement cannot, because the older cohort whose norms defined the previous window is no longer present to enforce them.

### Media Amplification

Media coverage of "extreme" positions can either expand the window (by normalizing the position through repeated exposure) or contract it (by triggering backlash that reinforces the boundary). The direction of the effect depends on the framing: sympathetic coverage normalizes; hostile coverage reinforces the boundary.

Algorithmic media amplification, discussed in Chapter 11, complicates this dynamic. Algorithms optimize for engagement, which favors content at or just beyond the window's boundary — the most provocative content that is still engaging rather than alienating. The algorithm pushes the window outward on engagement-maximizing dimensions ($d_2$, $d_6$) and leaves it unchanged on engagement-neutral dimensions ($d_3$, $d_4$). The result is selective window expansion: the window grows in the directions that generate clicks.

## The Overton Window Across Countries

The Overton window is not universal — different democracies have different windows, occupying different regions of the same universal preference manifold. Comparing windows across countries reveals systematic differences that illuminate the relationship between institutional structure and political possibility.

**The American window** is wide on $d_2$ (social values — a broad range from progressive to traditional is considered "mainstream") but narrow on $d_1$ (economics — the range of "acceptable" economic positions excludes full social democracy on the left and laissez-faire absolutism on the right, with a narrower center than many other Western democracies). The window has a distinctive shape: elongated along the $d_2$-$d_5$-$d_6$ diagonal, reflecting the dominance of social-identity-trust issues in American political discourse.

**The Scandinavian window** is shifted on $d_1$: positions that are center-left in Scandinavia (comprehensive public healthcare, universal childcare, strong labor protections) are left-of-center or even outside the window in the United States. Conversely, Scandinavian countries have a narrower window on $d_2$ (social values consensus is stronger, with less variation in acceptable positions on issues like gender equality and LGBTQ+ rights) and $d_4$ (foreign policy — NATO membership and internationalism are near-consensus positions).

**The question of window mobility:** Some political strategies explicitly aim to shift the Overton window — to make previously "unthinkable" positions "thinkable" and eventually "mainstream." The strategy can be deployed from either end of the manifold. Progressive activists who advocate for policies outside the current window (e.g., universal basic income, abolishing prisons) aim to expand the window leftward. Nationalist movements that advocate for positions outside the current window (e.g., withdrawing from international institutions, restricting immigration by ethnicity) aim to expand the window rightward.

The geometric framework clarifies the difference between two strategies for window expansion:

1. **Persuasion:** Moving voters' manifold positions toward the desired policy, so that the window — which is anchored in the population's preference distribution — naturally expands to include the position. This is slow but durable.

2. **Normalization:** Making the position visible and discussed in mainstream discourse, even without moving voters' positions. The window can expand even if voters do not change their minds, because the boundary is defined not by what voters believe but by what is considered "acceptable to discuss." This is faster but more fragile — the window can snap back if the normalization campaign fails.

Both strategies operate on the manifold, but they operate on different objects: persuasion shifts the preference distribution, while normalization shifts the window boundary without shifting preferences. The geometric framework distinguishes them cleanly, while the 1D account conflates them.

## Overton as Political Curvature

Near the center of $W$, the political metric is approximately flat. Positions are easily reached from nearby positions; the cost of movement is low. A politician at the center of the window has maximum freedom of movement — they can shift their position on any dimension without incurring significant Overton cost.

Near the boundary of $W$, the metric has high positive curvature. The boundary penalty makes positions expensive to maintain: a politician at the edge of the window must invest significant political capital in defending their position from the charge of "extremism." Small perturbations can push them outside the window, incurring sudden and steep costs. The curvature is asymmetric: approaching the boundary from inside is a gradual increase in cost, while crossing the boundary produces a discontinuous jump in social penalty.

This curvature structure creates a centripetal force in politics: the geodesic cost of positions near the window's center is lower than the cost of positions near the boundary, creating an energetic preference for centrism — not because centrist positions are better but because they are cheaper. The politician who adopts a centrist position minimizes their Overton cost, freeing up political capital for other uses. The politician who adopts a position near the boundary must spend capital defending the position itself, leaving less for policy achievement.

The curvature structure also explains why political change is often discontinuous rather than gradual. The window's boundary is a potential barrier: a politician who wants to move the discourse from inside the window to a position outside it must overcome the boundary penalty. If the penalty is high, the barrier is insurmountable for any individual politician. But if multiple politicians adopt positions near the boundary simultaneously, the social proof effect weakens the boundary, reducing the penalty. At some threshold, the barrier collapses, and the window shifts discontinuously — a phase transition in the Overton dynamics.

## District 7: The Window in Motion

We trace District 7's Overton window over three decades, analyzing its shape, position, and dynamics on the six-dimensional manifold.

**1990s:** The window is wide on $d_1$ (economic policy spans from moderate progressive to moderate conservative — a broad range of economic positions is debatable). The window is narrow on $d_2$ (social consensus around traditional values; LGBTQ+ rights are outside the window; marijuana legalization is outside the window). The window is narrow on $d_5$ (institutional trust is high across both parties; anti-institutional positions are marginal). The window's principal axis is aligned with $d_1$: the main political variation is economic.

**2010s:** The window has rotated. On $d_1$, it has narrowed (the "Third Way" consensus has reduced the range of debatable economic positions). On $d_2$, it has expanded dramatically (same-sex marriage has moved from outside the window to inside; marijuana legalization has moved from "radical" to "mainstream"). On $d_5$, the window has expanded downward (anti-institutional positions, driven by the Tea Party and then Trump, have entered the mainstream). The window's principal axis has rotated from $d_1$ to the $d_2$-$d_5$ diagonal: the main political variation is now social values and institutional trust.

**2020s:** The window continues to rotate. On $d_3$ (environment), it has expanded (climate change denial has moved from inside the window to the window's boundary; aggressive climate policy has moved from the boundary to inside). On $d_6$ (identity), the window has become highly asymmetric: some forms of identity politics are well inside the window, while others are at or beyond the boundary, depending on which end of the $d_6$ spectrum is involved.

The shift is anisotropic — the window has rotated on the manifold, not merely translated. A voter in 1995 and the same voter in 2025 may occupy the same position on the manifold, but the window has moved around them: positions that were mainstream in 1995 are now "extreme," and positions that were "extreme" in 1995 are now mainstream. The voter has not moved. The window has.

---

> **DISTRICT 7 — CHAPTER SUMMARY**
>
> *We have formalized the Overton window as a connected, bounded region of the political preference manifold, and the geodesic constraint it imposes on political trajectories. The window has shape (wide on some dimensions, narrow on others), position (different in different electorates), and dynamics (shifting in response to elite adoption, crises, generational replacement, and media amplification). Near the window's center, the political metric is flat and movement is cheap; near the boundary, curvature is high and positions are expensive to maintain.*
>
> *In District 7, the Overton window has rotated over three decades: from a $d_1$-aligned window (economic policy is the main axis of variation) to a $d_2$-$d_5$-aligned window (social values and institutional trust define the acceptable range). Voters have not moved; the window has moved around them.*
>
> *In Chapter 11, we turn to the force that most powerfully shapes the voter's perception of the manifold: the media ecosystem as a heuristic field, and its corruption.*
