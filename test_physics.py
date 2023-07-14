import unittest
import physics
import numpy as np


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
        self.assertEqual(
            physics.calculate_auv_acceleration(100, np.pi / 6), np.array([])
        )

    def test_calculateAUVAngularAcceleration(self):
        pass

    def test_calculateAUV2Acceleration(self):
        pass

    def test_calculateAUV2AngularAcceleration(self):
        pass


if __name__ == "__main__":
    print(physics.calculateBuoyancy(10, 10))
    print(physics.willItFloat(10000, 1), True)
    print(physics.calculatePressure(1))
