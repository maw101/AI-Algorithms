"""Particle Swarm Optimisation Visualisation.

This module provides a set of functions to generate a random set of particles
and perform PSO on this set until either the maximum number of iterations
are ran or we get an acceptable answer.

Example:
    $ python3 particle_swarm_optimisation.py

Requirements:
    numpy
    matplotlib (pyplot)

"""

import random
import numpy as np
import matplotlib.pyplot as plt

CURRENT_COMPENSATION = 0.5
PERSONAL_BEST_COMPENSATION = 0.65
GLOBAL_BEST_COMPENSATION = 1.0


def get_particle_fitness(particle):
    """Determines a fitness value for a given particle.

    Args:
        particle (Particle): the particle to measure fitness for

    Returns:
        (int): a fitness value

    """
    return (particle.position[0] ** 2) + (particle.position[1] ** 2) + 2

class Particle():
    """Represents a particle within the swarm.

    Attributes:
        position (numpy array): stores the Particle's X-Y positions
        best_position (numpy array): stores the Particle's current best X-Y
            positions
        best_position_value (float): stores the Particle's current best
            positions fitness value
        velocity (numpy array): stores the Particle's Velocity

    """

    def __init__(self):
        """Initialises a new Particle.

        Assigns it to a random position and initialises other members."""
        rand_x = ((-1) ** (random.random() >= 0.5)) * random.random() * 50 # range +-50
        rand_y = ((-1) ** (random.random() >= 0.5)) * random.random() * 50 # range +-50
        self.position = np.array([rand_x, rand_y])
        self.best_position = self.position # starts being our original position
        self.best_position_value = float('inf') # infinite, must be improved upon
        self.velocity = np.array([0, 0]) # intially zero

    def move(self):
        """Moves the Particle in the direction of the Particle's Velocity."""
        self.position += self.velocity

    def __str__(self):
        """Prints the Particle's Data Members."""
        print("Particle: Position", self.position, "Velocity", \
              self.velocity, "Best Position", self.best_position, \
              "Best Position Value", self.best_position_value)


class SearchSpace():
    """Represents a Particle Swarm Optimisations Search Space.

    Attributes:
        num_particles (int): the number of particles to be used
        particles (list): the particle objects
        target (float): the target value
        target_exit_boundary (float): the allowable +- value around the target
            at which to allow a break in the iteration
        global_best_position (numpy array): stores the Search Space's current
            best X-Y position
        global_best_value (float): stores the Search Space's current best
            positions fitness value

    """

    def __init__(self, target, target_exit_boundary, number_particles=50):
        """Initialises a new Search Space.

        Intialises particles and sets a random global best position along with
        initialising data members to provided values.

        Args:
            target (float): the target value
            target_exit_boundary (float): the allowable +- value around the
                target at which to allow a break in the iteration
            number_particles (int): the number of particles to be used
        """
        self.num_particles = number_particles
        # initialise particles
        self.particles = [Particle() for _ in range(self.num_particles)]

        self.target = target
        self.target_exit_boundary = target_exit_boundary

        rand_x = ((-1) ** (random.random() >= 0.5)) * random.random() * 50 # range +-50
        rand_y = ((-1) ** (random.random() >= 0.5)) * random.random() * 50 # range +-50
        self.global_best_position = np.array([rand_x, rand_y])

        self.global_best_value = float('inf')

    def output_particles(self):
        """Prints each Particle in turn."""
        for particle in self.particles:
            particle.__str__()

    def update_particle_best(self):
        """Iterates over all particles and updates the particles personal best."""
        for particle in self.particles:
            candidate = get_particle_fitness(particle)
            # check if this candidate fitness is better than current particle
            #   best
            if candidate < particle.best_position_value:
                particle.best_position = np.copy(particle.position)
                particle.best_position_value = candidate

    def update_global_best(self):
        """Checks all particles to see if a new global best exists."""
        for particle in self.particles:
            candidate = get_particle_fitness(particle)
            # check if this candidate fitness is better than current global
            #   best
            if candidate < self.global_best_value:
                self.global_best_position = np.copy(particle.position)
                self.global_best_value = candidate

    def iterate_particles(self):
        """Iterates each particle in turn, updating and moving each particle."""
        # update the velocity for each particle
        for particle in self.particles:
            # weighted random portion in direction of particles best
            personal_adjustment = (PERSONAL_BEST_COMPENSATION * \
                random.random()) * (particle.best_position - particle.position)

            # weighted random portion in direction of global best
            global_adjustment = (GLOBAL_BEST_COMPENSATION * \
                random.random()) * (self.global_best_position - \
                                    particle.position)

            # calculate new velocity
            updated_velocity = (CURRENT_COMPENSATION * particle.velocity) + \
                personal_adjustment + global_adjustment

            # update particles velocity and move
            particle.velocity = updated_velocity
            particle.move()


if __name__ == "__main__":
    # code to run when not imported
    TARGET = 2

    TARGET_EXIT_BOUNDARY = float(input("Enter the boundary either side of the"\
                                      " target to allow exit at: "))
    NUM_PARTICLES = int(input("Enter the number of particles: "))

    SEARCH_SPACE = SearchSpace(TARGET, TARGET_EXIT_BOUNDARY, \
                               NUM_PARTICLES)

    #SEARCH_SPACE.output_particles() # for debug

    MAX_ITERATIONS = int(input("Enter the maximum number of iterations: "))

    I = 0
    FITNESS_RECORD = []
    while I < MAX_ITERATIONS:
        # update all particles
        SEARCH_SPACE.update_particle_best()
        SEARCH_SPACE.update_global_best()

        # check if we have satisfied our termination condition
        if abs(SEARCH_SPACE.target - SEARCH_SPACE.global_best_value) <= \
            SEARCH_SPACE.target_exit_boundary:
            break

        SEARCH_SPACE.iterate_particles()
        FITNESS_RECORD.append(SEARCH_SPACE.global_best_value)

        # plot the current state of the search space
        plt.clf()
        plt.figure(dpi=150)
        PLOT_TITLE = "PSO Visualisation - Iteration #" + str(I)
        plt.title(PLOT_TITLE)
        plt.scatter(SEARCH_SPACE.global_best_position[0], \
                    SEARCH_SPACE.global_best_position[1], marker='D', c='r')
        # iterate over each particle, adding them to the scatter graph
        for particle_index in range(SEARCH_SPACE.num_particles):
            plt.scatter(SEARCH_SPACE.particles[particle_index].position[0], \
                        SEARCH_SPACE.particles[particle_index].position[1], \
                            marker='.', c='k', alpha=0.3)
        plt.show()

        # increase iteration count
        I += 1

    # print the result of our iteration
    print("Iterations:", I)
    print("Best Solution:", SEARCH_SPACE.global_best_position, "with value", \
      SEARCH_SPACE.global_best_value)

    # plot fitness function record over the iterations
    plt.clf()
    plt.figure(dpi=150)
    plt.title("PSO Fitness Record over iterations")
    plt.xlabel("Iteration Number")
    plt.ylabel("Fitness Function Value")
    plt.plot(FITNESS_RECORD)
