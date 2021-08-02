import unittest
from alatest import get_list, find_price


class TestExercise(unittest.TestCase):

    def test_get(self):
        company_list1 = "companyA.csv"
        company_list2 = "companyB.csv"
        dictionaryA = {'name_operation': 'companyA', '1': '0.9', '268': '5.1', '46': '0.17',
                       '4620': '0', '468': '0.15', '4631': '0.15', '4673': '0.9', '46732': '1.1'}
        dictionaryB = {'name_operation': 'companyB', '1': '0.92', '44': '0.5',
                       '46': '0.2', '467': '1', '48': '1.2'}
        self.assertEqual(get_list(company_list1), dictionaryA)
        self.assertEqual(get_list(company_list2), dictionaryB)

    def test_price(self):
        phone1 = "46732589"
        phone2 = "5765493"
        self.assertTrue(find_price(phone1, " ", "999"))
        self.assertFalse(find_price(phone2, " ", "999"))


if __name__ == '__main__':
    unittest.main()
