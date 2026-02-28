# test_backgryph.py
"""
Tests for BackGryph module.
"""

import unittest
from backgryph import BackGryph

class TestBackGryph(unittest.TestCase):
    """Test cases for BackGryph class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BackGryph()
        self.assertIsInstance(instance, BackGryph)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BackGryph()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
