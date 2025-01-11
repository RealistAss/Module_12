import unittest
from unittest import TestCase

from runner_and_tournament import Runner, Tournament

class TournamentTest(TestCase):
    @classmethod
    def SetUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runs = {'Усейн': 10, 'Андрей': 9, 'Ник': 3}
        self.runners = {x: Runner(name=x, speed=y) for x, y in self.runs.items()}

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'{key}: {value}')

    def test_tournament(self):
        a = Tournament(90, self.runners['Усейн'], self.runners['Андрей'])
        all_results = a.start()
        self.assertTrue(all_results[2], self.runs[1])

if __name__ == 'main':
    unittest.main()