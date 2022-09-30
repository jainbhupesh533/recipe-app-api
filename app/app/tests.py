"""
Sample Test
"""

from django.test import SimpleTestCase
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from app import calc

class CalcTest(SimpleTestCase):
	"""Test the Calc Module"""
	
	def test_add_numbers(self):
		"""Test adding numbers together"""
		res = calc.add(5,6)
		logger.info("Success")
		self.assertEqual(res,11)

	def test_subtract_numbers(self):
		"""test subtract numbers together"""
		res = calc.subtract(10,15)
		self.assertEqual(res,5)