import unittest
import Module_12_2
import Module_12_1

a = unittest.TestSuite()

a.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_1.RunnerTest))
a.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(a)