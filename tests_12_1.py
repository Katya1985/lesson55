import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walk1 = runner.Runner("Katya")
        for i in range(10):
            walk1.walk()
        self.assertEqual(walk1.distance, 50)

    def test_run(self):
        run2 = runner.Runner("Alex")
        for i in range(10):
            run2.run()
        self.assertEqual(run2.distance, 100)

    def test_challenge(self):
        chall3 = runner.Runner("Michel")
        chall4 = runner.Runner("Dasha")
        for i in range(10):
            chall3.walk()
            chall4.run()

        self.assertNotEqual(chall3.distance, chall4.distance)


if __name__ == '__main__':
    unittest.main()