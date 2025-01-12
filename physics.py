import numpy as np
import matplotlib.pyplot as plt

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
    elif F_magnitude < 0:
        raise ValueError("Force magnitude cannot be less than 0.")
    else:
        direction_radians = (
            np.deg2rad(F_direction)
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
        F_magnitude > 100 or F_magnitude < 0
    ):  # raises an error if the magnitude of the force inputted is greater than the maximum possible force
        raise ValueError("The thruster can only apply a maximum force of 100 N and the force magnitude cannot be negative.")
    elif (
        F_angle != -np.pi/6 and F_angle != np.pi/6
    ):  # raises an error if the thruster rotation is not a possible angle value
        raise ValueError(
            "The thrusters can only rotate 30 degrees in either direction of the x-axis."
        )
    else:  # calculates and returns the accelerations of the AUV in the x and y directions
        acceleration_x = (F_magnitude * np.cos(F_angle)) / mass
        acceleration_y = (F_magnitude * np.sin(F_angle)) / mass
        acceleration = [acceleration_x, acceleration_y]
        #acceleration = np.array([acceleration_x], [acceleration_y])
        return acceleration


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    """Calculates the angular acceleration of the AUV when accounting for one thruster."""

    if (
        F_magnitude > 100 or F_magnitude < 0
    ):  # raises an error if the magnitude of the force inputted is greater than the maximum possible force
        raise ValueError("The thruster can only apply a maximum force of 100 N and the force magnitude cannot be negative.")
    elif (
        F_angle != -np.pi/6 and F_angle != np.pi/6
    ):  # raises an error if the thruster rotation is not a possible angle value
        raise ValueError(
            "The thrusters can only rotate 30 degrees in either direction of the x-axis."
        )
    else:  # calculates and returns the angular acceleration of the AUV
        torque = thruster_distance * F_magnitude * np.sin(F_angle)
        angular_acceleration = torque / inertia
        return angular_acceleration


def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    """Calculates the acceleration of the AUV in the 2D Plane for all four thrusters."""
    #if type(T) != np.ndarray:
       #raise ValueError("T should be a numpy array.")
    #elif np.shape(T) != (1,4):
        #raise ValueError("T should have the shape (1,4).")
    rotation_matrix = [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
    x_and_y_component_matrix = [
        [np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
        [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)],
    ]
    # forces = np.matmul(rotation_matrix, x_and_y_component_matrix, T)
    forces = np.dot(x_and_y_component_matrix, T)
    forces = np.dot(rotation_matrix, forces)

    acceleration = np.array([forces[0] / mass, forces[1] / mass])
    return acceleration
    #return np.array([0.00980067, -0.00198669])


def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia=100):
    """
    Calculates the angular acceleration of the AUV when accounting for all four thrusters
    T: an np.ndarray of the magnitudes of the forces applied by the thrusters in Newtons
    alpha: the angle of the thrusters in radians
    theta: the angle of the AUV in radians
    mass: the mass of the AUV in kilograms. The default value is 100kg.
    """

    #if type(T) != np.ndarray:
        #raise ValueError("T should be a numpy array.")
    #elif np.shape(T) != (4,1):
        #raise ValueError("T should have the shape (4,1).")
    if L < 0 or l < 0:
        raise ValueError("L or l cannot be negative.")
    elif inertia <= 0:
        raise ValueError("Inertia cannot be negative or less than or equal to 0.")
    else:
        signs_matrix = np.array([1, -1, 1, -1])
        #r = np.sqrt(np.power(L,2) + np.power(l, 2))
        torque = np.sum(np.multiply(signs_matrix, T) * (L*np.sin(alpha) + l*np.cos(alpha)))
        #torque = np.dot(signs_matrix,T)
        angular_acceleration = torque / inertia

        return angular_acceleration
    
def simulate_auv2_motion(T, alpha, L, l, mass=100, inertia=100, dt=0.1, t_final=10, x0=0, y0=0, theta0=0):
    '''
    Simulates the motion of the AUV in the 2D plane.

    Accepts:
        T: an np.ndarray of the magnitudes of the forces applied by the thrusters in Newtons.
        alpha: the angle of the thrusters in radians.
        L: the horizontal distance from the center of mass of the AUV to the thrusters in meters.
        l: the vertical distance from the center of mass of the AUV to the thrusters in meters.
        inertia (optional): the moment of inertia of the AUV in kg*m^2. The default value is 100 kg*m^2
        dt (optional): the time step of the simulation in seconds. The default value is 0.s
        t_final (optional): the final time of the simulation in seconds. The default value is 10s
        x0 (optional): the initial x-position of the AUV in meters. The default value is 0m
        y0 (optional): the initial y-position of the AUV in meters. The default value is 0m
        theta0 (optional): the initial angle of the AUV in radians. The default value is 0rad

    Returns:
        t: an np.ndarray of the time steps of the simulation in seconds.
        x: an np.ndarray of the x-positions of the AUV in meters.
        y: an np.ndarray of the y-positions of the AUV in meters.
        theta: an np.ndarray of the angles of the AUV in radians.
        v: an np.ndarray of the velocities of the AUV in meters per second.
        omega: an np.ndarray of the angular velocities of the AUV in radians per second.
        a: an np.ndarray of the accelerations of the AUV in meters per second squared.
    '''
    # add raise value error things
    # Initializes numpy arrays with zeros
    t = np.arange(0, t_final, dt)
    
    x = np.zeros_like(t)
    x[0] = x0
   
    y = np.zeros_like(t)
    y[0] = y0
    
    theta = np.zeros_like(t)
    theta[0] = theta0
    
    #v = np.zeros_like(t)
    
    omega = np.zeros_like(t)
    
    #a = np.zeros_like(t)
    a= np.zeros((len(t), 2))
    v = np.zeros((len(t), 2))
    
    # Calculates the angular acceleration outside of the for loop because parameters are constant
    angular_acceleration = calculate_auv2_angular_acceleration(T, alpha, L, l, inertia)
    
    for i in range(1, len(t)):
        # uses the previous angular velocity and angular acceleration to calculate the current angular velocity
        omega[i] = omega[i-1] + angular_acceleration * dt

        # uses the previous angle and the previous angular velocity to calculate the current angle
        theta[i] = theta[i-1] + omega[i] * dt 

        # initializes a temporary array to store the x and y components of acceleration
        temp_a = calculate_auv2_acceleration(T, alpha, theta[i], mass)

        # assigns the x and y components of acceleration to the proper indices of matrix a
        a[i][0] = temp_a[0]
        a[i][1] = temp_a[1]
        # a[i] = temp_a

        # uses the previous x/y velocities and the previous x/y accelerationies to calculate the current x/y velocities
        v[i][0] = v[i-1][0] + a[i][0] * dt
        v[i][1] = v[i-1][1] + a[i][1] * dt
        # v[i] = v[i-1] + a[i-1] * dt

        # uses the previous x/y positions and the previous x/y velocities to calculate the current x/y positions
        x[i] = x[i-1] + v[i][0] * dt
        y[i] = y[i-1] + v[i][1] * dt

    return t, x, y, theta, v, omega, a

def plot_auv2_motion(t, x, y, theta, v, omega, a):
    '''
    Plots the motion of the AUV in the 2D plane

    Accepts:
        t: an np.ndarray of the time steps of the simulation in seconds.
        x: an np.ndarray of the x-positions of the AUV in meters.
        y: an np.ndarray of the y-positions of the AUV in meters.
        theta: an np.ndarray of the angles of the AUV in radians.
        v: an np.ndarray of the velocities of the AUV in meters per second.
        omega: an np.ndarray of the angular velocities of the AUV in radians per second.
        a: an np.ndarray of the accelerations of the AUV in meters per second squared.

    Returns:
        Plots :)
    '''

    plt.plot(t, x, label="X Position")
    plt.plot(t, y, label="Y Position")
    plt.plot(t, theta, label="Angle")
    plt.plot(t, v, label="Velocity")
    plt.plot(t, omega, label="Angular Velocity")
    plt.plot(t, a, label="Acceleration")
    plt.xlabel("Time (s)")
    plt.ylabel("X Position (m), Y Position (m), Angle (radians), Velocity (m/s), Angular Velocity (radians/s^2), Acceleration (m/s^2)")
    plt.legend()
    plt.show()