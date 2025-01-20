from resume_app.counter import Counter
from django.test import TestCase

class TestCounter(TestCase):

    def setUp(self):
        self.counter = Counter(count=0, max=5)

    def test_default_initialization(self):
        self.assertEqual(self.counter.count, 0)
        self.assertEqual(self.counter.max, 5)

    def test_custom_initialization(self):
        self.assertEqual(self.counter.increment(), 1)
        self.assertEqual(self.counter.increment(), 2)
        self.assertEqual(self.counter.increment(), 3)
        self.assertEqual(self.counter.increment(), 4)
        self.assertEqual(self.counter.increment(), 0)
        self.assertEqual(self.counter.increment(), 1)
        self.assertEqual(self.counter.increment(), 2)
