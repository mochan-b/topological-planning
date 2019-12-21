
# Homotopy

## Homotopy Definition

A topological space is a set $X$ and a collection of subsets of $X$ that are called open such that

- $X$ and $\varnothing$ are open sets
- intersection of two open sets is open
- union of any number of open sets is open

Let $X$ and $Y$ be topological spaces and let $f : X \rightarrow X$ be a function. The function is continuous if for every open set in $S \subset Y$, $f^{-1}(S)$ is also open.

A continuous function is a map.

Given topological spaces $X$ and $Y$, a homotopy is a collection of maps such that there exists a map $g : X \times [0,1] \rightarrow Y$ where $I = [0,1]$.

## Trajectories and Homotopies 

A trajectory $\tau$ is a function from time $t$ to $\mathbb{R}^2$ or points $(x,y)$. Or, formally $\tau : [0, \infty) \rightarrow \mathbb{R}^2$. Note that the trajectory must have a starting point as the current point and the goal.

We define the homotopy as a collection of trajectories such that there exists a map $g : [0,\infty) \times [0,1] \rightarrow \mathbb{R}^2$. 

When we want to find a homotopy of trajectories, the intent is that taking any trajectory in the homotopy is good as another.

### Goal Region without Time

We can arrive at the goal at any time. Thus, our trajectory is from a $(0,x,y)$ position to an end position within a zone at any time. Thus, our goal is pillar in the $H$-space. Touching any part of the pillar constitutes reaching the goal and thus, our homotopies have to defined so that reaching any pillar is adequate.

## Defining Homotopies by the Environment

### Stationary Obstacle

Suppose have a stationary obstacle in the environment. We can either go left to the obstacle or right of the obstacle. Thus, we have two homotopy classes, one going left of the obstacle and another going right of the obstacle.

Let us consider the 3d space of $H = t \times \mathbb{R}^2$. Suppose that $t$ goes up in the $z$ direction. Then, the obstacle creates a pillar in the $H$-space. Given a trajectory where we go left of the obstacle, our trajectory goes through the left of the obstacle. A trajectory that goes through the right of the pillar cannot be continuously deformed so that it goes to the left of the pillar to the goal.

#### Donuts

Another homotopy is doing donuts around the obstacle before proceeding to the goal. Every time we do another donut we have another homotopy.

### Moving Obstacle

A moving obstacle creates a rope like structure in $H$-space.

Suppose we are following a car. We can either choose to overtake from the left, overtake from the right or choose to follow behind in the car. 

If we choose to follow the car, we will be taking the trajectory above the rope to hit the goal pillar. We can go left and right as well and hit our goal pillar. 

If we overtake and then the obstacle overtakes us gain and then we can have infinite number of homotopies. 

### Lanes

Lane boundaries do not change over time and thus act like stationary obstacles but with a very long thing segment in $xy$-space. However unlike obstacles, we consider a new homotopy every time we cross the lane boundary. 

Do we have entirely cross the boundary does partially crossing the boundary also make sense?

## Kinematically Feasible Region in $H$-space

Most of the trajectories in the homotopy are not kinematically feasible. We want to describe a region in $H$-space that is kinematically feasible and a subset of a homotopy. 

