from unittest import TestCase
from models.config import MAX_VALUE
from models.captured import CapturedCollection, CapturedNumber
from models.stats import DataCapture , Stats
from itertools import chain

class TestCapturedNumber(TestCase):
    def test_captured_number_values(self):

        numbers = range(1 , MAX_VALUE)

        for number in numbers:
            i = CapturedNumber(number)
            self.assertIsInstance(i.value, int)
            self.assertEqual(i.value, number)
            self.assertIsInstance(i.greater, int)
            self.assertEqual(i.greater, 0)
            self.assertIsInstance(i.less, int)
            self.assertEqual(i.less, 0)
            self.assertIsInstance(i.count, int)
            self.assertEqual(i.count, 0)

class TestCapturedCollection(TestCase):
    def test_captured_collection_values(self):
        captured_collection = CapturedCollection()
        self.assertIsInstance(captured_collection.collection, dict)
        for i in range(1, MAX_VALUE + 1):
            self.assertIsInstance(captured_collection[i], CapturedNumber)
            self.assertEqual(captured_collection[i].value, i)

    def test_captured_collection_getitem_error(self):
        captured_collection = CapturedCollection()
        tests = chain(
            range(0, -10, -1),  # Negative numbers
            range(MAX_VALUE + 1, MAX_VALUE + 10),  # out of range
        )

        for test in tests:
            with self.assertRaises(ValueError):
                captured_collection[test]

class TestDataCapture(TestCase):
    def test_init(self):
        datacapture = DataCapture()
        self.assertIsInstance(datacapture, DataCapture)
        self.assertIsInstance(datacapture.count, int)
        self.assertIsInstance(datacapture.data, CapturedCollection)
        self.assertEqual(datacapture.count, 0)
        self.assertEqual(len(datacapture.data), 0)

    def test_build_stats(self):
        datacapture = DataCapture()
        for i in range(1, MAX_VALUE + 1):
            datacapture.add(i)
        stats = datacapture.build_stats()
        self.assertIsInstance(stats, Stats)

    def test_add(self):
        for i in range(1, MAX_VALUE + 1):
            datacapture = DataCapture()
            datacapture.add(i)
            self.assertEqual(datacapture.count, 1)
            self.assertEqual(len(datacapture.data), 1)
            self.assertEqual(datacapture.data[i].value, i)

