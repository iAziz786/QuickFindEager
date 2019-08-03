import unittest
from .main import QuickFind

class TestQuickFindEager(unittest.TestCase):

    def test_upper(self):
      quick = QuickFind(10)
      quick.join(5, 6)
      quick.join(6, 7)
      quick.join(1, 5)
      quick.join(0, 1)
      
      self.assertEqual(quick.is_connected(1, 7), True)


if __name__ == '__main__':
    unittest.main()