import unittest
from unittest.mock import patch
from app.data_storage import DataStorage

class TestDataStorage(unittest.TestCase):
    @patch('builtins.print')
    def test_save_data(self, mock_print):
        storage = DataStorage()
        data = {"temperature": 25, "humidity": 50}
        storage.save_data(data)
        mock_print.assert_called_once_with("Data saved:", data)

if __name__ == '__main__':
    unittest.main()
