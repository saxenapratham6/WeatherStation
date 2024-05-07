import unittest
from unittest.mock import patch
from app.data_transmission import DataTransmitter

class TestDataTransmitter(unittest.TestCase):
    @patch('builtins.print')
    def test_transmit_data(self, mock_print):
        transmitter = DataTransmitter()
        data = {"temperature": 25, "humidity": 50}
        transmitter.transmit_data(data)
        mock_print.assert_called_once_with("Data transmitted:", data)

if __name__ == '__main__':
    unittest.main()
