import unittest
from unittest.mock import patch
from app.data_analysis import DataAnalyzer

class TestDataAnalyzer(unittest.TestCase):
    @patch('builtins.print')
    def test_analyze_data(self, mock_print):
        analyzer = DataAnalyzer()
        data = {"temperature": 25, "humidity": 50}
        analyzer.analyze_data(data)
        mock_print.assert_called_once_with("Data analyzed:", data)

if __name__ == '__main__':
    unittest.main()
