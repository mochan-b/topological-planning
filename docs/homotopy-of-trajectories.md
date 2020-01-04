
# Homotopy of Trajectories


## Basic Mathematical Definitions (Topology)

A __topological space__ is a set $X$ and a collection of subsets of $X$ that are called open such that

- $X$ and $\varnothing$ are open sets
- intersection of two open sets is open
- union of any number of open sets is open

Let $X$ and $Y$ be topological spaces and let $f : X \rightarrow X$ be a function. The function is __continuous__ if for every open set in $S \subset Y$, $f^{-1}(S)$ is also open.

A continuous function is a __map__.

Let $X$ and $Y$ be topological spaces. Two maps $f_0$ and $f_1$ are said to be __homotopic__ if $\exists$ a map $F: X \times [0,1] \rightarrow Y$ such that $F(x,0) = f_0(x)$ and $F(x,1) = f_1(x)$, $\forall x \in X$. The homotopy relationship forms an equivalence relation and the class that the function $f$ belongs to is called a __homotopy__.

## Homotopy of Trajectories

A trajectory $\tau$ is a function from time $t$ to $\mathbb{R}^2$ or points $(x,y)$. Or, formally $\tau : [0, \infty) \rightarrow \mathbb{R}^2$.

We define the homotopy as a collection of trajectories such that there exists a map $g : [0,\infty) \times [0,1] \rightarrow \mathbb{R}^2$. 

When we want to find a homotopy of trajectories, the intent is that taking any trajectory in the homotopy is good as another.

##

 