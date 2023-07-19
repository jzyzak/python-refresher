import unittest
import physics
import numpy as np
import math


class TestPhysics(unittest.TestCase):
    def test_calculateBuoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(10, 10), 981)
        self.assertNotEqual(physics.calculate_buoyancy(100, 10), 981)
        self.assertRaises(ValueError, physics.calculate_buoyancy, -1, 10)
        self.assertRaises(ValueError, physics.calculate_buoyancy, 10, -1)

    def test_willItFloat(self):
        self.assertEqual(physics.will_it_float(1, 10000), False)
        self.assertEqual(physics.will_it_float(10000, 1), True)
        self.assertRaises(ValueError, physics.will_it_float, -1.0, 10000.0)
        self.assertRaises(ValueError, physics.will_it_float, 10000.0, -1.0)

    def test_calculatePressure(self):
        self.assertEqual(physics.calculate_pressure(0), 101325)
        self.assertNotEqual(physics.calculate_pressure(0), 0)
        self.assertRaises(ValueError, physics.calculate_pressure, -1)

    def test_calculateAcceleration(self):
        self.assertEqual(physics.calculate_acceleration(100, 10), 10)
        self.assertNotEqual(physics.calculate_acceleration(1000, 10), 10)
        self.assertRaises(ValueError, physics.calculate_acceleration, 100, -10)

    def test_calculateAngularAcceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(100, 10), 10)
        self.assertNotEqual(physics.calculate_angular_acceleration(1000, 10), 10)
        self.assertRaises(ValueError, physics.calculate_angular_acceleration, 1000, -10)

    def test_calculateTorque(self):
        self.assertAlmostEquals(physics.calculate_torque(10, 30, 10), 50)
        self.assertNotEqual(physics.calculate_torque(100, 30, 10), 50)
        self.assertRaises(ValueError, physics.calculate_torque, 100, 30, -10)

    def test_calculateMomentOfInertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(5, 10), 500)
        self.assertNotEqual(physics.calculate_moment_of_inertia(10, 5), 500)
        self.assertRaises(ValueError, physics.calculate_moment_of_inertia, 0, 10)
        self.assertRaises(ValueError, physics.calculate_moment_of_inertia, 10, -5)

    def test_calculateAUVAcceleration(self):
        test = physics.calculate_auv_acceleration(100, np.pi/6)
        acceleration = np.array([0.8660254037844388, 0.5])
        self.assertAlmostEqual(test[0], acceleration[0])
        self.assertAlmostEqual(test[1], acceleration[1])

    def test_calculateAUVAngularAcceleration(self):
        self.assertAlmostEquals(physics.calculate_auv_angular_acceleration(100, np.pi/6), 25)
        self.assertRaises(ValueError,physics.calculate_auv_angular_acceleration,200,np.pi/6)
        self.assertRaises(ValueError,physics.calculate_auv_angular_acceleration,100,0)
        #self.assertNotEqual(physics.calculate_auv_angular_acceleration())

    def test_calculateAUV2Acceleration(self):
        testArray = np.array([1, 3, 1, 2])
        result = physics.calculate_auv2_acceleration(testArray, 0.5, 0.3)
        self.assertEqual(result[0], 0.009800665778412416)
        self.assertEqual(result[1], -0.001986693307950612)

    def test_calculateAUV2AngularAcceleration(self):
        self.assertEqual(physics.calculate_auv2_angular_acceleration(np.array([1,3,1,2]), 0.5, 1.5, 1.8), -0.06896360757926927)

    def test_SimulateAUV2Motion(self):
        t_test, x_test, y_test, theta_test, v_test, omega_test, a_test = physics.simulate_auv2_motion(np.array([1, 0, 1, 0]), 0.5, 1.5, 1.8, dt=0.5, t_final=1.5)
        self.assertEqual(t_test[0], 0)
        self.assertEqual(t_test[1], 0.5)
        self.assertEqual(t_test[2], 1.0)
        self.assertEqual(np.all(x_test), 0)
        self.assertEqual(np.all(y_test), 0)
        self.assertEqual(theta_test[0], 0)
        self.assertEqual(theta_test[1], 0)
        self.assertEqual(theta_test[2], 0.011493934596544877)
        self.assertEqual(np.all(v_test), 0)
        self.assertEqual(np.all(a_test), 0)
        self.assertEqual(omega_test[0], 0)
        self.assertEqual(omega_test[1], 0.022987869193089754)
        self.assertEqual(omega_test[2], 0.04597573838617951)


if __name__ == "__main__":
    print(physics.calculateBuoyancy(10, 10))
    print(physics.willItFloat(10000, 1), True)
    print(physics.calculatePressure(1))
