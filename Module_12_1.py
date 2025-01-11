import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = Runner('Илья')
        walker.walk()
        walker.walk()
        walker.walk()
        walker.walk()
        walker.walk()
        walker.walk()
        walker.walk()
        walker.walk()
        walker.walk()
        walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        runner = Runner('Марк')
        runner.run()
        runner.run()
        runner.run()
        runner.run()
        runner.run()
        runner.run()
        runner.run()
        runner.run()
        runner.run()
        runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner_2 = Runner('Макс')
        walker_2 = Runner('Миша')
        for i in range(10):
            runner_2.run()
            walker_2.walk()
        self.assertNotEqual(runner_2.distance, walker_2.distance)



