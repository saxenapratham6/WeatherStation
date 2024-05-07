import unittest
from app.data_collection import DataCollector

class TestDataCollection(unittest.TestCase):
    def test_collect_data(self):
        collector = DataCollector()
        data = collector.collect_data()
        self.assertIsInstance(data, dict)
        self.assertIn('temperature', data)
        self.assertIn('humidity', data)

if __name__ == '__main__':
    unittest.main()
