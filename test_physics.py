import unittest
import physics


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


if __name__ == "__main__":
    print(physics.calculateBuoyancy(10, 10))
    print(physics.willItFloat(10000, 1), True)
    print(physics.calculatePressure(1))
