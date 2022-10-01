"""
Sample Test
"""

from app import calc
from django.test import SimpleTestCase
import logging

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


class CalcTest(SimpleTestCase):
    """Test the Calc Module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)
        logging.info("Success")
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """test subtract numbers together"""
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
