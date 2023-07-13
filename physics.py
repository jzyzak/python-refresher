import numpy as np


def calculate_buoyancy(V, density_fluid):
    '''Calculates the buoyancy of an object with volume "V" in a given fluid with density "density_fluid"'''
    if (
        density_fluid < 0 or V < 0
    ):  # raises an error if the fluid density or object volume is inputted as a negative number
        raise ValueError("Volume and fluid density cannot be negative.")
    else:  # calculates and returns buoyancy
        return density_fluid * V * 9.81


def will_it_float(V, mass):
    """Returns true if an object with a given volume "V" and mass will float in water and false if it will sink in water."""
    if (
        V < 0 or mass < 0
    ):  # raises an error if the object volume or mass is inputted as a negative number
        raise ValueError("Volume and mass cannot be negative.")
    else:
        density_object = mass / V  # calculates the density of the object
        if density_object > 1000:  # returns false if the object won't float in water
            return False
        else:  # returns true if the object will float in water
            return True


def calculate_pressure(depth):
    """Calculates the pressure of an object in water at a given depth."""
    if depth < 0:  # raises an error if the depth is inputted as a negative number
        raise ValueError("Depth cannot be negative.")
    else:  # calculates and returns the pressure at the given depth
        return 1000 * 9.81 * depth
