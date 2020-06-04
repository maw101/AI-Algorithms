# Artificial Intelligence Algorithms
A Collection of Artificial Intelligence Algorithm Implementations

## [Particle Swarm Optimisation](https://en.wikipedia.org/wiki/Particle_swarm_optimization)
**[Python Implementation](src/pso-python/particle_swarm_optimisation.py)**

Initially all particles in the search space are given a random X-Y position ([-50,+50], [-50,+50]). Our initial global best position is also given a random X-Y position in this range.

During each iteration for each Particle we calculate a new velocity and move the Particle in this direction. Velocities are calculated by weighting by a random portion in the direction of the particle's best position, then by weighting a random porition in the direction of the global best position and then adding this to the particle's current velocity.
Each of these values are multiplied by their own compensation value to give each an influence in the updated velocity - i.e. Global Best has the highest share, followed by the particle's personal best, followed by the current velocity of the particle.

### Example

This example uses 30 particles over a maximum of 50 iterations to find the best solution to the problem at hand.

Our boundary condition for exit is that the absolute difference between our target value (2) and our current best fitness value be less than or equal to 1e-10.

The red diamond represents the current best global position. We can see in later iterations that the swarm comes in much closer to this value as we start to reach our solution.

![](README_ASSETS/pso_demo.gif)

Example Output:
```text
Enter the boundary either side of the target to allow exit at: 1e-10

Enter the number of particles: 30

Enter the maximum number of iterations: 50
<Figure size 432x288 with 0 Axes>
...
<Figure size 432x288 with 0 Axes>
Iterations: 36
Best Solution: [ 1.02369730e-06 -9.40186064e-06] with value 2.000000000089443
<Figure size 432x288 with 0 Axes>
```

## [K-Means](https://en.wikipedia.org/wiki/K-means_clustering)
**[Java Implementation](src/kmeans)**

### Example
#### One-Dimensional Example
Example utilises integers along a 1-D number line.

Value Set: `{6, 8, 18, 26, 13, 32, 24}`

Initial Centroid Values: `{11, 20}`

K Value: 2

Example Final Output:
```text
Centroid (value=25.0) Record Identifiers: [18.0, 26.0, 32.0, 24.0]
Centroid (value=9.0) Record Identifiers: [6.0, 8.0, 13.0]
```

#### Two-Dimensional Example
Example utilises integer points on a 2-D space. Each value represents a coordinate `{X, Y}`.

Value Set: `{{185, 72}, {170, 56}, {168, 60}, {179, 68}, {182, 72}, {188, 77}}`

Initial Centroid Values: `{{185, 72}, {170, 56}}`

K Value: 2

Example Final Output:
```text
Centroid (X=169.0, Y=58.0) Record Identifiers: [2, 3]
Centroid (X=183.5, Y=72.25) Record Identifiers: [1, 4, 5, 6]
```

## Discrete Fuzzy Logic Model
**[Python Implementation](src/fuzzy-set-logic/FuzzySet.py)**

Provides a set of functions to manipulate discrete fuzzy logic sets represented in a vector notation.

Each element is: `<membership value>/<element>`, this is converted into a tuple of: `(<membership value>, <element>)`.

Provides methods for: INVERT, OR, AND, MAX, chop, determining a sets Centre of Gravity, getting an elements membership, and printing of the fuzzy set's data members.

### Examples

Examples are provided at the bottom of the script.

#### Example 1

Made up of two Fuzzy Sets (`A` and `B`).

`A = {0.0/1, 0.4/2, 0.8/3, 1.0/4}`

`B = {0.2/1, 0.2/2, 0.4/3, 0.5/4}`


a) performs an AND operation on `A` and `B`
b) performs the NOT operation on `A`
c) performs the AND operation on the result of (b) and set `B`
d) performs the OR operation on the result of (a) and the result of performing the AND operation on the result of (c)


Example 1 Final Output:
```text
a) A AND B = [(0.0, 1), (0.2, 2), (0.4, 3), (0.5, 4)]
b) NOT A = [(1.0, 1), (0.6, 2), (0.2, 3), (0.0, 4)]
c) (NOT A) AND B = [(0.2, 1), (0.2, 2), (0.2, 3), (0.0, 4)]
d) (A AND B) OR ((NOT A) AND B) = [(0.2, 1), (0.2, 2), (0.4, 3), (0.5, 4)]
```
