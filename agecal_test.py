import unittest
from datetime import datetime
from agecal import current_age
"""
class
"""
class AgecalTest(unittest.TestCase):
    """
    def
    """
    def test_current_age_today(self):
        """
        content
        """
        birthday=datetime.strptime("1988.02.02", "%Y.%m.%d")
        result=current_age(birthday)
        self.assertEqual(result,34)
if __name__ == '__main__':
    unittest.main()
    