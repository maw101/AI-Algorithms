"""Model of Discrete Fuzzy Logic.

This module provides a set of functions to manipulate discrete fuzzy logic 
sets represented in a vector notation.

Example:
    $ python3 FuzzySet.py
    Define the operations to be performed below.

"""

DECIMAL_PLACE_ROUND = 2

class FuzzySet:
    """Represents a Discrete Fuzzy Set in a vector notation. Each element is:
    <membership value>/<element>, this is converted into a tuple of:
    (<membership value>, <element>)

    Attributes:
        set: stores the Discrete Fuzzy Set in a vector notation

    """

    def __init__(self, iterable: any):
        """Initialises a new Discrete Fuzzy Set.

        Ensures that each element is a tuple and has an assigned probability."""
        self.set = set(iterable)
        # ensure we have a probability for each element
        for element in self.set:
            # check if element is a tuple
            if not isinstance(element, tuple):
                raise TypeError('Fuzzy set has element which is not a tuple')
            # ensure probability for each element
            if not isinstance(element[0], float):
                raise ValueError('Element has no assigned probability')


    def __invert__(self):
        """Inverts each element in the set."""
        resulting_set_as_list = list(self.set.copy())
        # iterate over each element and determine inverted probability
        for index, element in enumerate(resulting_set_as_list):
            new_probability = float(round(1 - element[0], DECIMAL_PLACE_ROUND))
            resulting_set_as_list[index] = (new_probability, element[1])
        # return this resulting set as a fuzzy set
        return FuzzySet(resulting_set_as_list)


    def __or__(self, other_set):
        """Performs the or operation on two sets, utilises the max function.

        Attributes:
            other_set (FuzzySet): the other Fuzzy Set

        """
        return self.get_max(other_set)


    def __and__(self, other_set):
        """Performs the and operation on two sets, utilises the min function.

        Attributes:
            other_set (FuzzySet): the other Fuzzy Set

        """
        if len(self.set) != len(other_set.set):
            raise ValueError('The two sets have differing lengths')
        current_set_as_list = list(self.set.copy())
        other_set_as_list = list(other_set.set.copy())
        resulting_set = [(min(current_set_as_list[index][0], other_set_as_list[index][0]),
                          current_set_as_list[index][1])
                         for index in range(len(current_set_as_list))]
        return FuzzySet(set(resulting_set))


    def chop(self, value_to_chop_at):
        """Performs a chop on the Fuzzy Set, chops values above a given value.

        Attributes:
            other_set (FuzzySet): the other Fuzzy Set

        """
        current_set_as_list = list(self.set.copy())
        resulting_set = [(min(current_set_as_list[index][0], value_to_chop_at),
                          current_set_as_list[index][1])
                         for index in range(len(current_set_as_list))]
        return FuzzySet(resulting_set)


    def get_centre_of_gravity(self):
        """Determines the Centre of Gravity for the Fuzzy Set."""
        current_set_as_list = list(self.set.copy())
        # sum of product of each element
        sum_of_products = sum([elem[0]*elem[1] for elem in current_set_as_list])
        sum_of_elements = sum([elem[0] for elem in current_set_as_list])
        return sum_of_products / sum_of_elements


    def get_centre_of_gravity_sum(self):
        """Gets the string representation of the Centre of Gravity sum."""
        current_set_as_list = list(self.set.copy())
        # sum of product of each element
        sum_of_products = ['('+str(elem[0])+' * '+str(elem[1])+')'
                           for elem in current_set_as_list]
        sum_of_elements = [str(elem[0]) for elem in current_set_as_list]
        return '(' + ' + '.join(sum_of_products) + ') / (' + \
            (' + ').join(sum_of_elements) + ')'


    def get_elements_membership(self, element):
        """Gets the membership value for a given element.

        Attributes:
            element: the element to get the membership value for

        """
        for elem in self.set:
            if elem[1] == element:
                return elem[0]
        print('Element', element, 'was not found in the fuzzy set.')
        return None


    def get_max(self, other_set):
        """Performs the max operation on two sets.

        Attributes:
            other_set (FuzzySet): the other Fuzzy Set

        """
        if len(self.set) != len(other_set.set):
            raise ValueError('The two sets have differing lengths')
        current_set_as_list = list(self.set.copy())
        other_set_as_list = list(other_set.set.copy())
        resulting_set = [(max(current_set_as_list[index][0], other_set_as_list[index][0]),
                          current_set_as_list[index][1])
                         for index in range(len(self.set))]
        return FuzzySet(resulting_set)


    def __str__(self):
        """Prints the Fuzzy Set's Data Members."""
        # sort using second element of tuple
        sorted_set = sorted(self.set, key=lambda x: x[1])
        return f'{[elem for elem in sorted_set]}'


#####################################
# EXAMPLE 1
#####################################

A = FuzzySet({(0.0, 1), (0.4, 2), (0.8, 3), (1.0, 4)})
B = FuzzySet({(0.2, 1), (0.2, 2), (0.4, 3), (0.5, 4)})

print('a) A AND B =', A & B)
print('b) NOT A =', ~A)
print('c) (NOT A) AND B =', (~A) & B)
print('d) (A AND B) OR ((NOT A) AND B) =', (A & B) | ((~A) & B))


#####################################
# EXAMPLE 2
#####################################

# WALK_FAST = FuzzySet({(0.0, 1), (0.0, 2), (0.3, 3), (0.6, 4), (1.0, 5)})
# WALK_SLOW = FuzzySet({(1.0, 1), (1.0, 2), (0.5, 3), (0.0, 4), (0.0, 5)})

# POWER_LOW = FuzzySet({(1.0, 1), (1.0, 2), (0.0, 3), (0.0, 4), (0.0, 5)})

# # if walking pace is fast or not slow, set power to low
# FAST_OR_NOT_SLOW_WALK = WALK_FAST | (~WALK_SLOW)
# print('FAST OR NOT SLOW WALKER = ', FAST_OR_NOT_SLOW_WALK)

# THREE_MEMBERSHIP_VALUE = FAST_OR_NOT_SLOW_WALK.get_elements_membership(3)
# print('Membership value of element 3 =', THREE_MEMBERSHIP_VALUE)

# CHOPPED_POWER_LOW = POWER_LOW.chop(THREE_MEMBERSHIP_VALUE)
# print('Chopped POWER_LOW for membership value of 0.5 =', CHOPPED_POWER_LOW)

# # note: no composition required as no rule, therefore the step is skipped

# COG_CHOPPED_POWER_LOW = CHOPPED_POWER_LOW.get_centre_of_gravity()
# print('Chopped POWER_LOW COG SUM =', CHOPPED_POWER_LOW.get_centre_of_gravity_sum())
# print('Chopped POWER_LOW COG =', COG_CHOPPED_POWER_LOW)



#####################################
# EXAMPLE 3
#####################################

# # A robot has a fuzzy controller that decides how fast it should go (slow, medium, fast)
# # based on two factors: the bumpiness of the terrain (graded from 1 (flat) to 5 (very
# # bumpy)) and current energy levels (graded from 0 (no energy) to 4 (full battery)). The
# # rules and fuzzy sets for the controller are:
# #     IF Terrain is Bumpy OR Energy is Low THEN Speed is Slow
# #     IF Terrain is NOT Flat AND Energy is NOT Low THEN Speed is Medium
# #     IF Terrain is Flat OR Energy is High THEN Speed is Fast

# # Terrain fuzzy sets
# TERRAIN_FLAT = FuzzySet({(1.0, 1), (0.8, 2), (0.6, 3), (0.2, 4), (0.0, 5)})
# TERRAIN_BUMPY = FuzzySet({(0.0, 1), (0.2, 2), (0.4, 3), (0.8, 4), (1.0, 5)})

# # Energy level fuzzy sets
# ENERGY_LOW = FuzzySet({(1.0, 0), (0.8, 1), (0.5, 2), (0.1, 3), (0.0, 4)})
# ENERGY_HIGH = FuzzySet({(0.0, 0), (0.2, 1), (0.5, 2), (0.9, 3), (1.0, 4)})

# # Speed (output) fuzzy sets
# SPEED_SLOW = FuzzySet({(1.0, 2), (0.6, 4), (0.2, 6), (0.0, 8)})
# SPEED_MEDIUM = FuzzySet({(0.4, 2), (1.0, 4), (0.4, 6), (0.2, 8)})
# SPEED_HIGH = FuzzySet({(0.0, 2), (0.1, 4), (0.6, 6), (1.0, 8)})

# # Rules
# #TERRAIN_BUMPY_OR_ENERGY_LOW = TERRAIN_BUMPY | ENERGY_LOW               # Rule 1
# #TERRAIN_NOT_FLAT_AND_ENERGY_NOT_LOW = (~TERRAIN_FLAT) & (~ENERGY_LOW)  # Rule 2
# #TERRAIN_FLAT_OR_ENERGY_HIGH = TERRAIN_FLAT | ENERGY_HIGH               # Rule 3

# # The current sensor readings are: 2 for the terrain and 3 for the energy level.
# # Using fuzzy inference (and centre-of-gravity defuzzification), determine the
# #  output speed in mph (miles per hour) of the robot.

# # fuzzification - determine membership values
# TERRAIN_FLAT_MEMBERSHIP = TERRAIN_FLAT.get_elements_membership(2)
# TERRAIN_BUMPY_MEMBERSHIP = TERRAIN_BUMPY.get_elements_membership(2)

# ENERGY_LOW_MEMBERSHIP = ENERGY_LOW.get_elements_membership(3)
# ENERGY_HIGH_MEMBERSHIP = ENERGY_HIGH.get_elements_membership(3)

# print('TERRAIN_FLAT_MEMBERSHIP', TERRAIN_FLAT_MEMBERSHIP)
# print('TERRAIN_BUMPY_MEMBERSHIP', TERRAIN_BUMPY_MEMBERSHIP)
# print('ENERGY_LOW_MEMBERSHIP', ENERGY_LOW_MEMBERSHIP)
# print('ENERGY_HIGH_MEMBERSHIP', ENERGY_HIGH_MEMBERSHIP)

# # inference - get rule firing strenghts
# RULE_1_FIRING_STRENGTH = round(max(TERRAIN_BUMPY_MEMBERSHIP,
#                                     ENERGY_LOW_MEMBERSHIP), DECIMAL_PLACE_ROUND)
# RULE_2_FIRING_STRENGTH = round(min((1 - TERRAIN_FLAT_MEMBERSHIP),
#                               (1 - ENERGY_LOW_MEMBERSHIP)), DECIMAL_PLACE_ROUND)
# RULE_3_FIRING_STRENGTH = round(max(TERRAIN_FLAT_MEMBERSHIP,
#                                     ENERGY_HIGH_MEMBERSHIP), DECIMAL_PLACE_ROUND)

# print('RULE_1_FIRING_STRENGTH', RULE_1_FIRING_STRENGTH)
# print('RULE_2_FIRING_STRENGTH', RULE_2_FIRING_STRENGTH)
# print('RULE_3_FIRING_STRENGTH', RULE_3_FIRING_STRENGTH)

# # inference - chop the rule's output fuzzy set using firing strengths
# RULE_1_CHOPPED = SPEED_SLOW.chop(RULE_1_FIRING_STRENGTH)
# RULE_2_CHOPPED = SPEED_MEDIUM.chop(RULE_2_FIRING_STRENGTH)
# RULE_3_CHOPPED = SPEED_HIGH.chop(RULE_3_FIRING_STRENGTH)

# print('RULE_1_CHOPPED, SPEED_SLOW =', RULE_1_CHOPPED)
# print('RULE_2_CHOPPED, SPEED_MEDIUM =', RULE_2_CHOPPED)
# print('RULE_3_CHOPPED, SPEED_HIGH =', RULE_3_CHOPPED)

# # composition - compose these three output fuzzy sets
# RULE_1_2_CHOPPED_COMPOSED = RULE_1_CHOPPED.get_max(RULE_2_CHOPPED)
# OUTPUT = RULE_1_2_CHOPPED_COMPOSED.get_max(RULE_3_CHOPPED)

# print('OUTPUT =', OUTPUT)

# # defuzzification

# print(OUTPUT.get_centre_of_gravity_sum())
# print('Output COG =', OUTPUT.get_centre_of_gravity())

#####################################
# TEMPLATE
#####################################

# A = FuzzySet({})
# B = FuzzySet({})

# print(A)
# print(B)
