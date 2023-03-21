import pytest

from calc import Calculator

class TestCalc1:
	def setup(self):
		self.calc = Calculator

	def test_1(self):
		assert self.calc.multiply(self, 2, 5) == 10

	def test_2(self):
		assert self.calc.division(self, 5, 5) == 1

	def test_3(self):
		assert self.calc.subtraction(self, 88, 80) == 8

	def test_4(self):
		assert self.calc.adding(self, 10, 10) == 20

	def teardown(self):
		print("teardown")
