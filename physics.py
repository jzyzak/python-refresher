import numpy as np

g = 9.81  # m/s^2
water_density = 1000  # kg/m^3
surface_pressure = 101325  # kPa


def calculate_buoyancy(V, density_fluid):
    '''Calculates the buoyancy of an object with volume "V" in a given fluid with density "density_fluid"'''
    if (
        density_fluid < 0 or V < 0
    ):  # raises an error if the fluid density or object volume is inputted as a negative number
        raise ValueError("Volume and fluid density cannot be negative.")
    else:  # calculates and returns buoyancy
        return density_fluid * V * g  # N


def will_it_float(V, mass):
    """Returns true if an object with a given volume "V" and mass will float in water. false if it will sink in water, and None if it is neutrally buoyant."""
    if (
        V < 0 or mass < 0
    ):  # raises an error if the object volume or mass is inputted as a negative number
        raise ValueError("Volume and mass cannot be negative.")
    else:
        density_object = mass / V  # calculates the density of the object
        if (
            density_object > water_density
        ):  # returns false if the object won't float in water
            return False
        elif (
            density_object == water_density
        ):  # returns None if the object is neutrally buoyant
            return None
        else:  # returns true if the object will float in water
            return True


def calculate_pressure(depth):
    """Calculates the pressure of an object in water at a given depth."""
    if depth < 0:  # raises an error if the depth is inputted as a negative number
        raise ValueError("Depth cannot be negative.")
    else:  # calculates and returns the pressure at the given depth
        return water_density * g * depth + surface_pressure
