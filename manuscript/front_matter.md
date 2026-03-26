# Front Matter

---

## Title Page

**Geometric Politics: Representation, Polarization, and the Topology of Democratic Choice**

Andrew H. Bond
Senior Member, IEEE
Department of Computer Science
San Jose State University

Book 10 of the Geometric Series

*San Jose, 2026*

---

## Series Foreword

This is the tenth and final volume in the Geometric Series.

The series began with a simple observation: across domains --- ethics, law, economics, cognition, medicine, communication, education, aesthetics --- the standard methodology compresses multi-dimensional structure into scalar numbers and then wonders why the numbers behave badly. GDP does not capture economic wellbeing. IQ does not capture intelligence. BLEU does not capture translation quality. QALYs do not capture patient health. Binary verdicts do not capture legal reasoning. The pattern is universal and the diagnosis is the same: scalar reduction destroys geometric structure, and the destruction is irreversible.

*Geometric Methods in Computational Modeling* (Book 1) assembled the mathematical toolkit: Riemannian geometry, hyperbolic embeddings, persistent homology, SPD manifolds, gauge theory. *Geometric Reasoning: From Search to Manifolds* (Book 2) developed the parent framework --- the heuristic field formalism, geodesic deviation, the four failure modes, gauge invariance, and the Scalar Irrecoverability Theorem that unifies them. *Geometric Ethics* (Book 3) was the first domain instantiation, demonstrating the framework on the 9-dimensional stratified moral manifold with its $D_4 \times U(1)_H$ symmetry group. Books 4 through 9 --- *Geometric Economics*, *Geometric Law*, *Geometric Cognition*, *Geometric Communication*, *Geometric Medicine*, *Geometric Education*, and *Geometric Aesthetics* --- extended the instantiation to markets, courts, minds, signals, clinics, classrooms, and the experience of beauty.

This book turns to politics. In some ways, it is the domain the series has been building toward from the beginning. Every domain book has asked: *what structure does scalar reduction destroy, and what does geometry recover?* In politics, the scalar reduction is the most visible and the most consequential. The left-right axis --- a single dimension, inherited from the seating arrangements of the French National Assembly in 1789 --- compresses the multi-dimensional reality of political preference into a line. The consequences are not academic. They are elections decided by projection artifacts. They are electorates that appear polarized on the axis but are not polarized on the manifold. They are voters who are "represented" by officials who share their 1D projection but differ from them on five of six political dimensions. They are the systematic failure of democratic institutions to translate what citizens actually want into what government actually does.

The circle closes here. *Geometric Ethics* began with the individual moral agent navigating a 9-dimensional moral manifold. *Geometric Politics* ends with the collective --- millions of agents on a shared political manifold, whose individual positions must be aggregated into collective decisions. The aggregation is a contraction. Arrow's impossibility theorem, reinterpreted geometrically, tells us that the contraction must be lossy. The question is not whether democratic institutions lose information --- they must --- but which information they lose, and whether they can be redesigned to lose less.

From the moral manifold to the democratic manifold, from individual judgment to collective choice: the geometry is the same, the stakes are higher, and the scalar trap is the deepest it has ever been.

---

## Preface

### The Left-Right Trap

In the spring of 2025, I was sitting in a conference room at San Jose State University, staring at a scatter plot that should not have existed. The plot showed voter positions in a mid-sized congressional district --- call it District 7 --- on two dimensions extracted from survey data: economic policy preferences on the horizontal axis, institutional trust on the vertical axis. The two-party split was clear on the horizontal axis: Democrats clustered left, Republicans clustered right, with a modest gap between the centroids. The standard story.

But on the vertical axis, the story collapsed. Both clusters were smeared across the full range of institutional trust. Within the Democratic cluster, there were high-trust progressives who believed in government as an instrument of justice and low-trust populists who viewed the entire system as captured by corporate interests. Within the Republican cluster, there were high-trust traditionalists who revered institutional authority and low-trust libertarians who wanted the institutions dismantled. The left-right axis put these voters into two tidy groups. The second dimension revealed that each group contained factions with fundamentally incompatible views about the legitimacy of the institutions they were competing to control.

And this was only two dimensions. When I added a third --- environmental priority --- the clusters fragmented further. When I added a fourth --- foreign policy orientation --- they fragmented again. By the time I had estimated positions on six dimensions from the full survey instrument, the neat two-party division had dissolved into a continuous, anisotropic cloud on a six-dimensional manifold. The "polarization" that dominated every cable news segment and every newspaper editorial was a projection artifact. The electorate was not divided into two hostile camps. It was distributed across a multi-dimensional space that the one-dimensional left-right axis was never built to represent.

I had spent the previous three years building the Geometric Series --- developing the mathematical framework for analyzing what scalar reduction destroys across domains from ethics to medicine. The Scalar Irrecoverability Theorem, proved in *Geometric Reasoning*, states the diagnosis precisely: when a multi-dimensional object is contracted to a scalar, the lost information is irrecoverable. No function, no matter how clever, can reconstruct the original from the contraction. The theorem is abstract. Its consequences are not.

In politics, the contraction is the vote. A voter holds a position on a six-dimensional preference manifold. The voting system reduces that position to a mark on a ballot --- a scalar. The election aggregates the scalars and declares a winner. The winner "represents" the district. But the representation is a fiction: the elected official is a point in one-dimensional outcome space, while the district they represent is a distribution on a six-dimensional manifold. The official represents the district's projection, not its position. And the projection is lossy. The Democratic Irrecoverability Theorem, which this book proves in Chapter 5, quantifies the loss: in a plurality election on a six-dimensional preference manifold, at least five-sixths of the manifold information is destroyed by the act of voting.

Five-sixths. Eighty-three percent.

This number changed how I thought about democracy. Not because democracy is broken --- it remains the best system we have --- but because its scalar architecture ensures that it operates on a fraction of the information it would need to represent its citizens faithfully. The apparatus of democratic life --- polls, campaigns, elections, representation --- is a sequence of contractions, each discarding dimensional structure, each irreversible. The result is not a malfunction. It is the predictable consequence of compressing a manifold to a line.

The book you hold is the geometric analysis of that compression. It asks: What structure does the left-right axis destroy? What would we see if we looked at politics on the full manifold? And can democratic institutions be redesigned to preserve more of the structure they currently discard?

The answers are, respectively: nearly everything, a world that looks very different from the one our projections suggest, and yes --- but only if we understand the geometry.

### Who This Book Is For

This book is written for three audiences, and it asks something different of each.

For **political scientists, election researchers, and democratic theorists**, the book offers a mathematical framework that unifies results from social choice theory (Arrow, Gibbard-Satterthwaite, McKelvey), spatial voting models (Downs, Poole-Rosenthal), and deliberative democratic theory (Fishkin, Dryzek) under a single geometric roof. The framework does not replace these literatures --- it reinterprets them as statements about the geometry of preference manifolds and the contractions that voting systems impose. The payoff is new theorems (Democratic Irrecoverability, Polarization Illusion, Gerrymandering Surgery) and a new measurement tool (the Political Bond Index) that detects representational failures invisible to existing metrics.

For **mathematicians and physicists** curious about applications of differential geometry, gauge theory, and algebraic topology to democratic institutions, the book provides a rigorous worked example. The political preference manifold is a six-dimensional Riemannian manifold with a non-trivial metric, curvature structure, and gauge group. Arrow's theorem is a statement about the impossibility of lossless contraction. Gerrymandering is manifold surgery. The Overton window is a geodesic constraint. These are not metaphors. They are precise mathematical claims, stated as theorems and proved in the appendices.

For **citizens** who sense that the left-right axis does not capture what they actually believe, the book provides the mathematical language for that intuition. You are not moderate. You are not a centrist. You are not confused. You are multi-dimensional, and the political system is measuring you with a ruler that has one mark on it. The mismatch between what you think and what the system sees is not a failure of your thinking. It is a failure of the system's geometry.

The book assumes basic linear algebra and probability. It does not assume differential geometry, topology, or gauge theory --- these are developed from first principles in Chapter 4 and Appendix A. It does assume intellectual seriousness: the reader should be prepared to follow a mathematical argument across several pages and a political argument across several centuries.

### A Note on District 7

A single thread runs through every chapter of this book: the political life of District 7, a fictional but realistic congressional district in a mid-sized American metropolitan area. District 7 spans a dense urban core, inner-ring suburbs, and an exurban rural fringe. Its population is demographically diverse: a historically Black urban neighborhood, a Latino-majority suburban corridor, a white working-class exurban belt, a college-educated professional enclave near the university, and a retirement community. The district is competitive in the one-dimensional sense --- it votes roughly 50-50 in presidential elections.

But this one-dimensional characterization is, as I hope to show, a lie.

District 7 is fictional because any real district would bring partisan baggage that obscures the geometric point. It is realistic because every feature of the district --- its demographics, its voting patterns, its media ecosystem, its redistricting history --- is drawn from composites of real American districts. The reader who recognizes their own district in District 7 is seeing the geometry, not the fiction.

---

## Acknowledgments

A book that stands at the end of a ten-volume series accumulates debts that no acknowledgments section can discharge. The attempt is nonetheless obligatory.

The geometric framework that underpins this book --- and the entire series --- was developed in conversation with the Geometric Reasoning research group at San Jose State University. I am grateful to the group members who contributed to the political instantiation of the framework, particularly those who challenged my early conviction that politics was "just ethics with more voters" and forced me to confront the distinctive geometry of collective choice. The discrete-continuous tension that Chapter 17 identifies as politics' unique contribution to the parent theory emerged from those challenges.

The political science literature that grounds this book was brought to my attention by colleagues in the Department of Political Science at SJSU, who endured a mathematician's invasion of their domain with generosity and only occasional exasperation. I am particularly indebted to conversations about DW-NOMINATE and spatial voting models that helped me understand what political scientists already know about the multi-dimensionality of preferences --- and what the geometric framework adds to that understanding.

The redistricting analysis in Chapter 9 builds on the pioneering work of Moon Duchin and the Metric Geometry and Gerrymandering Group at Tufts University, whose computational redistricting methods inspired the manifold-geometric extension. The ranked-choice voting analysis in Chapter 13 benefited from data generously provided by FairVote and from conversations with election administrators in Alaska, Maine, and New York City who shared their practical experience with RCV implementation.

James Fishkin's work on deliberative democracy, particularly the Deliberative Polling methodology and its remarkable empirical results, is foundational to Chapter 14. His demonstrations that informed deliberation systematically reduces apparent polarization and activates suppressed preference dimensions are, I believe, among the most important findings in modern political science --- and they find a natural explanation in the geometric framework.

The series editors, early readers of the manuscript, and anonymous reviewers of the component papers improved the book through their criticism. The errors that remain are, as always, proof that I did not always listen.

This is the final volume in a series that has occupied four years of my professional life. The debts accumulated across ten books are impossible to enumerate --- to co-authors, to students, to referees, to editors, to the institutions that supported the work. But the deepest debt is to the readers who followed the argument from the moral manifold to the democratic manifold, from the first page of *Geometric Methods* to the last page of this book. The circle closes. The geometry, I hope, speaks for itself.

Andrew H. Bond
San Jose, California
March 2026
