import unittest
import os
from unittest.mock import patch

from lab_2 import *
class TestStudentManagementSystem(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_data.csv"
        self.test_data = [
            {"name": "Jane", "surname": "Doe", "age": "25", "phone": "1234567890"},
            {"name": "John", "surname": "Doe", "age": "22", "phone": "9876543210"}
        ]

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_addnewelement(self):
        addNewElement()
        self.assertEqual(len(list), 1)

    def testdeleteelement(self):
        list.extend(self.test_data)
        deleteElement()
        self.assertEqual(len(list), len(self.test_data) - 1)

    def test_updateelement(self):
        list.extend(self.test_data)
        updateElement()
        updated_element = {"name": "John", "surname": "Smith", "age": "26", "phone": "5555555555"}
        self.assertIn(updated_element, list)

    def test_addcsv(self):
        with open(self.test_file, 'w', newline='') as file:
            fieldnames = ["name", "surname", "age", "phone"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.test_data)

        addCSV(self.test_file)
        self.assertEqual(len(list), len(self.test_data))

    def test_savecsv(self):
        list.extend(self.test_data)
        saveCSV(self.test_file)
        
        loaded_data = []
        with open(self.test_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                loaded_data.append(row)

        self.assertEqual(loaded_data, self.test_data)
    
    @patch('sys.argv', ['script.py', 'test_file'])
    def test_main(self):
        with patch('builtins.print'), self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)
        
if __name__ == '__main__':
    unittest.main()
