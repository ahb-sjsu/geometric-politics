# Chapter 9: Gerrymandering as Manifold Surgery

> *"In most democracies, voters choose their representatives. In America, representatives choose their voters."*
> — Thomas Mann and Norman Ornstein

---

> **RUNNING EXAMPLE — DISTRICT 7**
>
> *The 2030 census triggers redistricting. District 7 must be redrawn. Three maps are proposed:*
>
> *Map A, drawn by a bipartisan commission, keeps the district's communities largely intact. Eastfield stays connected to the Route 9 corridor. The university enclave stays with the inner suburbs. The exurban belt is shared between District 7 and the neighboring District 8.*
>
> *Map B, drawn by the state legislature's partisan majority, makes a surgical incision. Eastfield — the historically Black urban neighborhood — is severed from the Route 9 corridor and attached to a distant, heavily Democratic urban district. The Route 9 corridor is attached to the exurban belt. The resulting District 7 is "competitive" on the 1D axis (it votes 49-51 rather than 50-50) but its manifold structure has been fundamentally altered: a natural community of interest (the urban progressive coalition) has been cracked, and the remaining district is geometrically gerrymandered.*
>
> *Map C, drawn by an algorithm optimizing for population equality and geographic compactness, produces a district that looks neutral on the map. But the algorithm is blind to the trust-identity dimension ($d_5$-$d_6$), and the resulting district splits the exurban populist community across two districts, diluting the anti-institutional voice.*
>
> *Three maps, three geometric operations on the preference manifold. Each produces a different District 7 with a different representational structure. The question is: which operation is surgery, and which is healing?*

---

## Redistricting as Topology

Redistricting is usually discussed in geographic terms: drawing lines on a map, ensuring population equality, maintaining compactness, respecting county and municipal boundaries. This geographic frame is natural — districts are geographic entities — but it obscures the deeper operation that redistricting performs.

Redistricting is a topological operation on the political preference manifold. It determines which voters share a connected component (a district), thereby altering the geodesic structure of representation. The geographic map is the input; the preference manifold is where the operation has its effects.

Consider the operation formally. Let $\mathcal{P}$ be the political preference manifold, and let each voter $v \in V$ have both a geographic position $g(v) \in \mathbb{R}^2$ (their location on the map) and a manifold position $\phi(v) \in \mathcal{P}$ (their position on the six-dimensional preference manifold). A districting function $D: V \to \{1, \ldots, k\}$ partitions voters into $k$ districts. Each district $D^{-1}(j)$ is a subset of voters that is connected in geographic space (the district is a contiguous region on the map).

But the image of each district on the preference manifold — the set $\{\phi(v) : v \in D^{-1}(j)\}$ — may or may not be connected. A geographically contiguous district whose voters occupy two separated clusters on the preference manifold is a district that has been drawn to unite voters who have nothing in common politically. A geographically non-compact district (an oddly shaped sliver connecting two distant neighborhoods) that is compact on the preference manifold (the voters in both neighborhoods share political positions) is a district of genuine community of interest — despite its geographic ungainliness.

The traditional redistricting criteria — population equality, geographic compactness, contiguity — are conditions on the geographic map, not on the preference manifold. The geometric approach adds a manifold criterion: a good districting function produces districts that are also compact on the preference manifold.

## The Gerrymandering Surgery Theorem

**Definition 4 (Gerrymandering Index).** *Let $D$ be a districting function partitioning $n$ voters into $k$ districts, and let $\mu_j$ be the Frechet mean of district $j$'s preference distribution on the manifold. The gerrymandering index is:*

$$GI(D) = \frac{1}{n} \sum_{j=1}^{k} \sum_{v \in D^{-1}(j)} d_\mathcal{P}(v, \mu_j)$$

*where $d_\mathcal{P}$ is the manifold distance. $GI(D)$ measures the average manifold distance between each voter and their district's center of mass.*

A low $GI$ indicates a districting that groups manifold-nearby voters together — districts of genuine community of interest. A high $GI$ indicates a districting that groups manifold-distant voters together — districts that are geographically contiguous but politically incoherent.

**Theorem 5 (Gerrymandering Surgery).** *A districting function $D$ is a gerrymander if and only if $GI(D) > GI(D_{\text{neutral}})$, where $D_{\text{neutral}}$ is the expected gerrymandering index over the ensemble of all compact, contiguous, population-equal districtings drawn uniformly at random. The excess $GI(D) - GI(D_{\text{neutral}})$ measures the degree of manifold distortion introduced by the gerrymander.*

*Moreover, a gerrymander increases total manifold distance between voters and their representatives while preserving or reducing 1D distance metrics (partisan vote share, population equality, compactness). This is the geometric signature of gerrymandering: improvement on scalar metrics accompanied by deterioration on the manifold.*

### Packing and Cracking, Geometrized

The two basic operations of partisan gerrymandering — packing and cracking — have precise geometric characterizations:

**Packing** concentrates opposition voters into a few districts where they win by overwhelming margins. On the preference manifold, a packed district has very low internal manifold distance: the voters are homogeneous, clustered tightly on the manifold. The surrounding districts, stripped of these voters, have artificially elevated manifold distance — the remaining voters are more spread out because the concentrating force (the packed voters) has been removed.

Packing creates districts with small $GI_j = \frac{1}{|D^{-1}(j)|} \sum_{v \in D^{-1}(j)} d_\mathcal{P}(v, \mu_j)$ for the packed district and large $GI_j$ for the surrounding districts. The overall $GI(D)$ increases because the surrounding districts' manifold distances are inflated more than the packed district's distances are deflated.

**Cracking** splits a community of interest across multiple districts, diluting its influence in each. On the preference manifold, a cracked community is a connected cluster that has been bisected by the district boundary. Each resulting district contains half the cluster plus voters from a different region of the manifold. The two halves of the cluster, now in different districts, are represented by different officials who may not share the cluster's manifold position at all.

Cracking creates districts whose preference manifold images are bimodal: two clusters in preference space forced into the same geographic district. The $GI$ for each such district is elevated because the Frechet mean is between the two clusters, far from both.

### The Efficiency Gap and Its Geometric Limitation

The efficiency gap, proposed by Eric McGhee in 2014 and litigated in *Gill v. Whitford* (2018), measures the asymmetry in "wasted votes" between parties. A wasted vote is one that does not contribute to electing a candidate — either because the voter supported a losing candidate (wasted by loss) or because the voter supported a winning candidate by a margin beyond what was needed to win (wasted by excess). A large efficiency gap indicates that one party wastes far more votes than the other — the hallmark of gerrymandering.

The efficiency gap is a 1D metric. It captures packing and cracking on the partisan dimension but ignores higher-dimensional distortion. A gerrymander that optimizes on the 1D partisan axis while distorting $d_3$ through $d_6$ can have a low efficiency gap and a high gerrymandering index. The efficiency gap detects 1D gerrymandering; the $GI$ detects manifold gerrymandering.

Consider a concrete example: a district map that achieves perfect partisan fairness (efficiency gap = 0) by creating districts that are exactly balanced on the $d_1$-$d_2$ diagonal (the left-right axis). But the same map cracks the environmental coalition — voters who agree on $d_3$ across party lines — by distributing them across four districts where they are a minority in each. The map passes the efficiency gap test but fails the manifold test: $GI(D)$ is elevated because voters who are manifold-close on $d_3$ have been placed in different districts, increasing the average manifold distance between voters and their district centers.

The geometric approach detects what the scalar approach misses.

## Computational Redistricting and the Manifold

The ensemble approach to redistricting, pioneered by Moon Duchin and colleagues, generates thousands of randomly drawn compact, contiguous, population-equal district maps and compares the actual map to the ensemble distribution. If the actual map is an outlier in the ensemble — producing a partisan distribution that very few random maps produce — it is evidence of intentional manipulation.

The geometric contribution to the ensemble approach is straightforward: the comparison should be conducted on the full manifold, not just on 1D partisan vote share. A map that looks normal in the 1D ensemble distribution can be an outlier in the manifold ensemble — evidence of multi-dimensional gerrymandering designed to pass 1D tests.

The manifold ensemble comparison works as follows:

1. Generate $N$ random maps from the ensemble of compact, contiguous, population-equal districtings (using Markov chain Monte Carlo on the space of valid districtings).
2. For each random map $D_i$, compute $GI(D_i)$ using the six-dimensional manifold distance.
3. Compute $GI(D_{\text{actual}})$ for the actual map.
4. The percentile rank of $GI(D_{\text{actual}})$ in the ensemble distribution is the manifold gerrymandering score. If $GI(D_{\text{actual}})$ is in the 95th percentile or higher, the actual map is a manifold outlier — evidence of multi-dimensional gerrymandering.

## Communities of Interest: The Geometric Criterion

The legal concept of "community of interest" — a group of people with shared political concerns who should be kept together in a single district — has long been invoked in redistricting litigation but has resisted precise definition. Different courts have used different criteria: shared demographics, shared economic interests, shared geographic features, or simply the judgment of the redistricting authority.

The geometric framework provides a precise definition:

**Definition (Community of Interest).** *A community of interest is a connected subset of voters whose image on the preference manifold $\mathcal{P}$ is also connected and compact — that is, the voters share a region of the manifold, not just a region of geographic space.*

This definition captures the intuition that a community of interest is defined by shared political preferences, not by shared geography. Two neighborhoods that are geographically adjacent but politically disparate (one is a progressive university district, the other is a conservative retirement community) are not a community of interest — they share geography but not manifold position. Two neighborhoods that are geographically distant but politically similar (two working-class communities, one urban and one exurban, both with strong economic progressive positions and high institutional distrust) are a community of interest — they share manifold position even though they do not share geography.

The geometric definition also provides a test for whether a redistricting has respected communities of interest. If a district's voters form a single connected cluster on the manifold, the district is a community of interest. If the voters form two or more separated clusters — a bimodal distribution on the manifold — the district has been drawn to combine incompatible communities, likely to dilute the political voice of at least one.

The bimodality test is computationally straightforward: apply a clustering algorithm (e.g., Gaussian mixture models) to the manifold positions of each district's voters. If the optimal number of clusters is 1, the district respects the community of interest criterion. If the optimal number is 2 or more, the district contains manifold-separated communities that a gerrymander may have combined.

In District 7, the bimodality test under each proposed map:

- **Map A (bipartisan):** Optimal clusters = 1 (with some elongation along the $d_5$-$d_6$ axis). The district is a single community of interest on the manifold.
- **Map B (partisan):** Optimal clusters = 2. The Route 9 corridor voters ($d_1$ progressive, $d_5$ moderate) and the exurban voters ($d_1$ conservative, $d_5$ very low) form two separated clusters, forced into the same district by the gerrymandered geography. The district is not a community of interest — it is two communities sutured together by a geographic incision.
- **Map C (algorithmic):** Optimal clusters = 1 (but with high variance on $d_5$-$d_6$). The district is approximately a single community, though the trust-identity dimension shows more spread than under Map A.

## District 7: Three Maps

We now analyze the three proposed maps for District 7 using the geometric framework.

**Map A (bipartisan commission).** This map keeps communities of interest together: Eastfield with the Route 9 corridor, the university enclave with the inner suburbs, the exurban belt shared with District 8. The manifold gerrymandering index: $GI(D_A) = 1.8$. This is near the ensemble median of 1.9 — a normal map that neither concentrates nor disperses any community beyond what compact geography produces.

**Map B (partisan legislature).** This map severs Eastfield from the Route 9 corridor, attaching Eastfield to a distant urban district and the Route 9 corridor to the exurban belt. The effect on the manifold is dramatic:
- Eastfield's voters (centroid: $(-1.5, -0.3, 0.8, 0.0, -1.2, 1.5)$) are now in a heavily Democratic district where their specific manifold position — high identity, low trust — is drowned out by the district's median position, which is dominated by a different urban community with higher trust and lower identity salience.
- The Route 9 corridor's voters (centroid: $(-1.0, -0.5, 0.5, 0.2, -0.8, 1.0)$) are now in a district with the exurban belt (centroid: $(1.5, 1.2, -1.0, 1.0, -2.0, 1.0)$). The manifold distance between these two subcommunities is 4.2 — they are far apart on every dimension except $d_5$ (both distrust institutions).

The gerrymandering index: $GI(D_B) = 3.1$, in the 97th percentile of the ensemble distribution. The map is a manifold outlier. The partisan efficiency gap of Map B, however, is only slightly elevated: 0.04, within the range that courts have accepted as non-extreme. The scalar test passes; the manifold test fails.

**Map C (algorithmic).** The algorithm optimizes for population equality (within 1%), geographic compactness (minimizing the ratio of perimeter to area), and preservation of county boundaries. The resulting map is neat, symmetric, and defensible on traditional criteria. The gerrymandering index: $GI(D_C) = 2.0$, below the ensemble median. On 1D metrics, Map C is excellent.

But the algorithm was blind to the $d_5$-$d_6$ dimension. The exurban populist community — united by deep institutional distrust ($d_5$ very low) and strong identity salience ($d_6$ high) — straddles a county boundary. The algorithm, respecting the county line, splits this community across Districts 7 and 8. In neither district do the populist voters constitute a majority. Their voice — the $d_5$-$d_6$ voice — is diluted.

The dimension-specific gerrymandering index tells the story: $GI_{d5-d6}(D_C) = 2.8$, in the 91st percentile. The map is neutral on most dimensions but distortionary on the trust-identity dimension. The algorithm did not intend to gerrymander. But by optimizing on geographic criteria while ignoring manifold criteria, it performed manifold surgery on a dimension it could not see.

The lesson: even "neutral" algorithmic redistricting can produce manifold distortion on dimensions the algorithm does not model. The geometry of preferences is not reducible to the geography of neighborhoods. A redistricting process that respects the manifold must incorporate manifold information, not just geographic information.

---

> **DISTRICT 7 — CHAPTER SUMMARY**
>
> *We have formalized redistricting as manifold surgery — a topological operation that alters the geodesic structure of representation. The Gerrymandering Surgery Theorem provides a geometric criterion for distinguishing partisan surgery from neutral boundary adjustment: a gerrymander increases total manifold distance between voters and their district centers while preserving or improving 1D metrics.*
>
> *Three maps for District 7 illustrate the framework: the bipartisan map (normal $GI$, near the ensemble median), the partisan map (outlier $GI$, cracking the Eastfield community), and the algorithmic map (normal overall $GI$ but elevated on the trust-identity dimension, inadvertently splitting the populist community). The geometric approach detects both intentional gerrymandering and unintentional manifold distortion that scalar metrics miss.*
>
> *In Chapter 10, we turn to the Overton window: the region of the political manifold within which positions are considered "acceptable," and the geodesic constraint it imposes on political trajectories.*
