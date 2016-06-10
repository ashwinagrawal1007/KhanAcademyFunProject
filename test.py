import infection
import unittest

infection.user_base = { 0 : [1, 2, 3, 4, 8],
                        1 : [0, 2, 5, 6, 7],
                        2 : [0, 1, 4, 8, 9],
                        3 : [0, 4, 5, 6, 9],
                        4 : [0, 2, 3, 5, 7],
                        5 : [1, 3, 4, 6, 9],
                        6 : [1, 3, 5, 7, 8],
                        7 : [1, 4, 6],
                        8 : [0, 2, 6, 9],
                        9 : [2, 3, 5, 8],
                        10 : [11],
                        11 : [10]
        }

class TestInfection(unittest.TestCase):
    def test_total_infection(self):
        infection.infected = []
        infection.to_be_infected = []
        self.assertEqual(infection.total_infection(True), len(infection.user_base))

    def test_total_infection_pass(self):
        infection.infected = []
        infection.to_be_infected = []
        self.assertNotEqual(infection.total_infection_pass(), len(infection.user_base))

    def test_limited_infection(self):
        infection.infected = []
        infection.to_be_infected = []
        self.assertEqual(infection.limited_infection(5), 2)

    def test_limited_infection_closest(self):
        infection.infected = []
        infection.to_be_infected = []
        infected_users = infection.limited_infection(6)
        self.assertTrue(infected_users == 2 or infected_users == 10)

    def test_limited_infection_strict(self):
        infection.infected = []
        infection.to_be_infected = []
        self.assertEqual(infection.limited_infection(6,True), 0)
        self.assertEqual(infection.limited_infection(10,True), 10)

if __name__ == '__main__':
    unittest.main()