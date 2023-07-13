import numpy as np


def calculate_buoyancy(V, density_fluid):
    if density_fluid < 0 or V < 0:
        raise ValueError("Volume and fluid density cannot be negative.")
    else:
        return density_fluid * V * 9.81


def will_it_float(V, mass):
    if V < 0 or mass < 0:
        raise ValueError("Volume and mass cannot be negative.")
    else:
        density_object = mass / V
        if density_object > 1000:
            return False
        else:
            return True


def calculate_pressure(depth):
    if depth < 0:
        raise ValueError("Depth cannot be negative.")
    else:
        return 1000 * 9.81 * depth
