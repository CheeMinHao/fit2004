import unittest
from radix_sort import radix_sort

class TestRadixSort(unittest.TestCase):

    def testRadixSort(self):
        lst, col = [434, 343, 723, 367, 646, 773, 428, 734], 3
        answer = [343, 367, 428, 434, 646, 723, 734, 773]
        result = radix_sort(lst, col)
        self.assertEqual(result, answer, msg="Counting Sort wrongly implemented")

        for i in range(len(result) - 1):
            self.assertTrue(result[i] <= result[i+1], msg="Counting Sort wrongly implemented")

if __name__ == "__main__":
    unittest.main()