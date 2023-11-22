import unittest
from Utils import Utils
from students import Student

class TestUtils(unittest.TestCase):

    def test_addCSV(self):
        utils = Utils()
        data_list = []
        utils.addCSV("testdata.csv", data_list)
        self.assertTrue(len(data_list) > 0)

    def test_saveCSV(self):
        utils = Utils()
        students = [Student("John", "Doe", 20, "123456789")]
        utils.saveCSV("testoutput.csv", students)

if __name__ == '__main__':
    unittest.main()
