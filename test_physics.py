import unittest
import physics


class TestPhysics(unittest.TestCase):
    def test_calculateBuoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(10.0, 10.0), 981)
        self.assertNotEqual(physics.calculate_buoyancy(100.0, 10.0), 981)
        self.assertRaises(ValueError, physics.calculate_buoyancy, -1.0, 10.0)
        self.assertRaises(ValueError, physics.calculate_buoyancy, 10.0, -1.0)

    def test_willItFloat(self):
        self.assertEqual(physics.will_it_float(1.0, 10000.0), False)
        self.assertEqual(physics.will_it_float(10000.0, 1.0), True)
        self.assertRaises(ValueError, physics.will_it_float, -1.0, 10000.0)
        self.assertRaises(ValueError, physics.will_it_float, 10000.0, -1.0)

    def test_calculatePressure(self):
        self.assertEqual(physics.calculate_pressure(1.0), 9810)
        self.assertNotEqual(physics.calculate_pressure(100.0), 9810)
        self.assertRaises(ValueError, physics.calculate_pressure, -1.0)
