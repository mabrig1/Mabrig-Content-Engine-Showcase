import unittest
from datetime import datetime, timezone, timedelta
from scheduling import Post, status

class SchedulingTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 1, 1, tzinfo=timezone.utc)
    def test_unapproved(self):
        self.assertEqual(status(Post("A", False, self.now), self.now), "awaiting review")
    def test_due(self):
        self.assertEqual(status(Post("A", True, self.now), self.now), "eligible for simulated queue")
    def test_future(self):
        self.assertEqual(status(Post("A", True, self.now + timedelta(hours=1)), self.now), "scheduled")
    def test_naive(self):
        with self.assertRaises(ValueError):
            status(Post("A", True, datetime(2026, 1, 1)), self.now)
    def test_blank(self):
        with self.assertRaises(ValueError):
            status(Post(" ", True, self.now), self.now)

if __name__ == "__main__":
    unittest.main()
