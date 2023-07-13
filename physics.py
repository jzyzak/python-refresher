import numpy as np


def calculate_buoyancy(V, density_fluid):
    return density_fluid * V * 9.81


def will_it_float(V, mass):
    density_object = mass / V
    if density_object > 1000:
        return False
    else:
        return True


def calculate_pressure(depth):
    return 1000 * 9.81 * depth
