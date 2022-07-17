from unittest import TestCase
from models.captured import CapturedCollection
from models.stats import Stats

class TestStats(TestCase):
    def test_init(self):
        stats = Stats(10)
        self.assertIsInstance(stats, Stats)
        self.assertIsInstance(stats.count, int)
        self.assertIsInstance(stats.data, CapturedCollection)
        self.assertEqual(stats.count, 10)
        self.assertEqual(len(stats.data), 0)