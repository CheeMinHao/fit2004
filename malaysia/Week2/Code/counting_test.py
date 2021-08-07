import unittest
from counting_sort import sort_counting, sort_counting_alphabet, sort_counting_stable

class TestCountingSort(unittest.TestCase):

    def testCountingSort(self):
        lst = [2, 5, 3, 6, 4, 7, 8]
        answer = [2, 3, 4, 5, 6, 7, 8]
        result = sort_counting(lst)
        self.assertEqual(result, answer, msg="Counting Sort wrongly implemented")

        for i in range(len(result) - 1):
            self.assertTrue(result[i] <= result[i+1], msg="Counting Sort wrongly implemented")

    def testCountingSortAlphabet(self):
        lst = ["a", "t", "H", "Z", "o"]
        answer = ["H", "Z", "a", "o", "t"]
        result = sort_counting_alphabet(lst)
        self.assertEqual(result, answer, msg="Counting Sort wrongly implemented")

        for i in range(len(result) - 1):
            self.assertTrue(result[i] <= result[i+1], msg="Counting Sort wrongly implemented")

    def testCountingSortStable(self):
        lst = [3, 4, 7, 3, 6, 7, 4, 7]
        answer = [3, 3, 4, 4, 6, 7, 7, 7]
        result = sort_counting(lst)
        self.assertEqual(result, answer, msg="Counting Sort wrongly implemented")

        for i in range(len(result) - 1):
            self.assertTrue(result[i] <= result[i+1], msg="Counting Sort wrongly implemented")

if __name__ == "__main__":
    unittest.main()