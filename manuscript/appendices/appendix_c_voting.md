# Appendix C: Electoral System Comparison Protocol

This appendix specifies the full methodology for comparing electoral systems geometrically. The protocol is designed to be applied to any electorate with available multi-dimensional preference data.

---

## C.1 Preference Elicitation Instrument

The comparison requires voter positions on the political preference manifold. The recommended instrument elicits positions on each of the six dimensions using a battery of survey items.

### Economic Policy ($d_1$) — 5 items

1. "Government should guarantee a minimum standard of living for all citizens." (7-point scale: Strongly Disagree to Strongly Agree)
2. "The government regulates business too much." (7-point scale)
3. "Wealthy individuals should pay a substantially larger share of their income in taxes." (7-point scale)
4. "Free trade agreements benefit the American economy." (7-point scale)
5. "The government should provide healthcare for all citizens." (7-point scale)

### Social Values ($d_2$) — 5 items

1. "Traditional moral values should guide public policy." (7-point scale)
2. "Abortion should be legal in all or most cases." (7-point scale)
3. "Same-sex couples should have the same legal rights as heterosexual couples." (7-point scale)
4. "Marijuana should be legal for recreational use." (7-point scale)
5. "Religious organizations should have more influence in American life." (7-point scale)

### Environmental Priority ($d_3$) — 4 items

1. "Addressing climate change should take priority even if it slows economic growth." (7-point scale)
2. "The government should invest heavily in renewable energy." (7-point scale)
3. "Environmental regulations are worth the cost to businesses." (7-point scale)
4. "We have a moral obligation to protect the environment for future generations." (7-point scale)

### Foreign Policy ($d_4$) — 4 items

1. "The United States should reduce its military commitments abroad." (7-point scale)
2. "Immigration makes America stronger." (7-point scale)
3. "International cooperation is more important than national sovereignty." (7-point scale)
4. "The U.S. should increase defense spending." (7-point scale, reverse-coded)

### Institutional Trust ($d_5$) — 4 items

1. "The federal government can be trusted to do what is right most of the time." (7-point scale)
2. "The courts are generally fair and impartial." (7-point scale)
3. "The mainstream media provides accurate and reliable information." (7-point scale)
4. "Experts and scientists generally have the public's best interest at heart." (7-point scale)

### Identity ($d_6$) — 4 items

1. "My racial/ethnic/cultural identity is an important part of my political outlook." (7-point scale)
2. "America's national identity is threatened by increasing diversity." (7-point scale)
3. "Group-based inequalities require group-based solutions." (7-point scale)
4. "I feel a strong connection to people who share my cultural background." (7-point scale)

### Scoring

Each dimension score is the mean of its constituent items (after reverse-coding where indicated), standardized to mean 0 and standard deviation 1 across the sample. The resulting six-dimensional vector is the voter's position on the political preference manifold $\mathcal{P}$.

## C.2 Manifold Estimation

### Covariance Matrix

The $6 \times 6$ covariance matrix $\Sigma$ is estimated directly from the sample:

$$\hat{\Sigma}_{ij} = \frac{1}{n-1} \sum_{k=1}^n (x_k^{(i)} - \bar{x}^{(i)})(x_k^{(j)} - \bar{x}^{(j)})$$

### Effective Dimensionality

Compute the eigenvalues $\lambda_1 \geq \cdots \geq \lambda_6$ of $\hat{\Sigma}$. The effective dimensionality is the number of eigenvalues needed to explain 85% of the total variance:

$$d_{\text{eff}} = \min\left\{k : \frac{\sum_{i=1}^k \lambda_i}{\sum_{i=1}^6 \lambda_i} \geq 0.85\right\}$$

### Manifold Distance

The Mahalanobis distance serves as the manifold distance estimate:

$$d_\mathcal{P}(v_1, v_2) = \sqrt{(v_1 - v_2)^T \hat{\Sigma}^{-1} (v_1 - v_2)}$$

## C.3 Contraction Analysis

For each electoral system $E$ to be compared:

1. **Simulate the election.** Using the voter positions and candidate positions, simulate the election under system $E$. For plurality, count first-choice votes. For RCV, perform iterative elimination. For approval voting, use a threshold rule (voters approve all candidates within $\tau$ manifold distance units). For Condorcet, compute all pairwise comparisons.

2. **Compute information preservation.** Using the formulas from Chapter 5 and Chapter 13:
   - Plurality: $R = 1/d$
   - RCV: $R = \min(d, k-1)/d$
   - Approval: $R \approx (d-1)/d \cdot (1 - e^{-\tau^2/2})$ (depends on threshold)
   - Condorcet: $R = \min(d, \binom{k}{2})/d \cdot \text{(ordinal correction)}$

3. **Compute the Political Bond Index.** $BI(S, E) = \mathbb{E}[d_\mathcal{P}(v, r(v)) - d_\mathcal{P}(v, r^*(v))]$, where $r(v)$ is the voter's representative under system $E$ and $r^*(v)$ is the manifold-optimal representative.

4. **Compute dimension-specific BI.** For each dimension $i$: $BI_i(S, E) = \mathbb{E}[|v^{(i)} - r(v)^{(i)}| - |v^{(i)} - r^*(v)^{(i)}|]$.

## C.4 Comparison Metrics

The electoral system comparison produces:

| Metric | Definition | Interpretation |
|---|---|---|
| $R$ | Information preservation ratio | Fraction of manifold information surviving the contraction |
| $BI$ | Political Bond Index | Average excess manifold distance between voter and representative |
| $BI_i$ | Dimension-specific BI | Which dimensions the system serves and which it ignores |
| $GI$ | Gerrymandering index | Manifold coherence of districts (for district-based systems) |
| Condorcet efficiency | Probability of electing the Condorcet winner | How often the system selects the manifold-optimal candidate |
| Representativeness | $1 - BI / d_{\max}$ | Normalized representation quality |

## C.5 Statistical Considerations

### Sample Size

For reliable manifold estimation on a 6D space, a sample of at least $n = 500$ voters is recommended (approximately 80 per dimension). For precise metric estimation (including off-diagonal covariance terms), $n = 2{,}000$ or more is needed.

### Confidence Intervals

The Political Bond Index is a sample mean, so its standard error is:

$$SE(BI) = \frac{s_{BI}}{\sqrt{n}}$$

where $s_{BI}$ is the sample standard deviation of the individual Bond Index contributions $d_\mathcal{P}(v, r(v)) - d_\mathcal{P}(v, r^*(v))$. A 95% confidence interval is $BI \pm 1.96 \cdot SE(BI)$.

### Ensemble Comparison for Gerrymandering

For gerrymandering detection, generate $N = 10{,}000$ random compact, contiguous, population-equal district maps using Markov chain Monte Carlo on the space of valid districtings. Compute $GI(D_i)$ for each random map. The actual map's $GI$ percentile rank in this distribution is the gerrymandering score. A score above the 95th percentile is evidence of manifold gerrymandering.

## C.6 Application Checklist

To apply the comparison protocol to a specific electorate:

1. Administer the 26-item preference elicitation instrument to a representative sample ($n \geq 500$).
2. Compute dimension scores and standardize.
3. Estimate the covariance matrix and effective dimensionality.
4. Locate the candidates on the manifold (from platform analysis, roll-call votes, or candidate survey).
5. Simulate each electoral system on the empirical preference distribution.
6. Compute $R$, $BI$, $BI_i$, and other comparison metrics for each system.
7. Report the results with confidence intervals and ensemble comparisons.

The protocol is designed for reproducibility: given the same input data (voter positions and candidate positions), the comparison metrics are deterministic (for deterministic systems like plurality and RCV) or converge to stable values (for stochastic systems like ensemble gerrymandering analysis).
