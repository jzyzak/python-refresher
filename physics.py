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
        buoyancy = density_fluid * V * g  # N
        return buoyancy


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
        pressure = water_density * g * depth + surface_pressure
        return pressure


def calculate_acceleration(F, m):
    """Calculates the acceleration of an object given the net force exerted on it and the mass of the object."""

    if (
        m <= 0
    ):  # raises an error if an invalid mass (less than or equal to 0) is inputted
        raise ValueError("Mass cannot be negative or equal to 0.")
    else:  # calculates and returns the acceleration of the object
        acceleration = F / m
        return acceleration


def calculate_angular_acceleration(tau, I):
    """Calculates the angular acceleration of an object given the net torque exerted on it and the object's moment of inertia"""

    if (
        I <= 0
    ):  # raises an error if an invalid moment of inertia (less than or equal to 0) is inputted
        raise ValueError("Moment of inertia cannot be negative or equal to 0.")
    else:  # calculates and returns the angular acceleration of the object
        angular_acceleration = tau / I
        return angular_acceleration


def calculate_torque(F_magnitude, F_direction, r):
    """Calculates the torque exerted on an object given the magnitude of the force exerted on it, the direction of the force,
    and the distance from the axis of rotation to the point where the force is applied
    """
    if r < 0:  # raises an error if an invalid r (less than 0) is inputted
        raise ValueError("r cannot be less than 0.")
    else:
        direction_radians = (
            F_direction * np.pi / 180.0
        )  # converts the direction of the force to radians
        torque = (
            r * F_magnitude * np.sin(direction_radians)
        )  # calculates the torque exerted on the object
        return torque


def calculate_moment_of_inertia(m, r):
    """Calculates the moment of inertia of an object given its mass and the distance from the axis of rotation
    to the center of mass of the object"""

    if (
        m <= 0
    ):  # raises an error if an invalid mass (less than or equal to 0) is inputted
        raise ValueError("Mass cannot be negative or equal to 0.")
    elif r < 0:  # raises an error if an invalid r (less than 0) is inputted
        raise ValueError("r cannot be less than 0.")
    else:  # calculates and returns the moment of inertia of the object
        I = m * r * r
        return I


def calculate_auv_acceleration(
    F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5
):
    """Calculates the acceleration of the AUV in the 2D Plane for one thruster."""

    if (
        F_magnitude > 100
    ):  # raises an error if the magnitude of the force inputted is greater than the maximum possible force
        raise ValueError("The thruster can only apply a maximum force of 100 N")
    elif (
        F_angle != -30 and F_angle != 30
    ):  # raises an error if the thruster rotation is not a possible angle value
        raise ValueError(
            "The thrusters can only rotate 30 degrees in either direction of the x-axis"
        )
    else:  # calculates and returns the accelerations of the AUV in the x and y directions
        acceleration_x = (F_magnitude * np.cos(F_angle)) / mass
        acceleration_y = (F_magnitude * np.sin(F_angle)) / mass
        acceleration = np.array([acceleration_x], [acceleration_y])
        return acceleration


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    """Calculates the angular acceleration of the AUV when accounting for one thruster."""

    if (
        F_magnitude > 100
    ):  # raises an error if the magnitude of the force inputted is greater than the maximum possible force
        raise ValueError("The thruster can only apply a maximum force of 100 N")
    elif (
        F_angle != -30 and F_angle != 30
    ):  # raises an error if the thruster rotation is not a possible angle value
        raise ValueError(
            "The thrusters can only rotate 30 degrees in either direction of the x-axis"
        )
    else:  # calculates and returns the angular acceleration of the AUV
        torque = thruster_distance * F_magnitude * np.sin(F_angle)
        angular_acceleration = torque / inertia
        return angular_acceleration


def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    """Calculates the acceleration of the AUV in the 2D Plane for all four thrusters."""

    rotation_matrix = [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
    x_and_y_component_matrix = [
        [np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
        [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)],
    ]
    # forces = np.matmul(rotation_matrix, x_and_y_component_matrix, T)
    forces = np.dot(rotation_matrix, np.dot(x_and_y_component_matrix, T))

    acceleration = forces / mass
    return acceleration


def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia=100):
    """Calculates the angular acceleration of the AUV when accounting for all four thrusters"""

    if L < 0 or l < 0:
        raise ValueError("L or l cannot be negative.")
    elif inertia <= 0:
        raise ValueError("Inertia cannot be negative or less than or equal to 0.")
    else:
        signs_matrix = np.array([1, -1, 1, -1])

        torques = np.multiply(
            signs_matrix, (T * (L * np.sin(alpha) + l * np.cos(alpha)))
        )

        angular_acceleration = torques / inertia

        return angular_acceleration
