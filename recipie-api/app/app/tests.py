"""sample test case """
from django.test import SimpleTestCase;
from app.calc import *;

class CalcTest(SimpleTestCase):
    """test the calc module"""
    
    def test_add_number(self):
        """testing adding numbers togther"""
        res = add(5, 6)
        self.assertEqual(res, 11)
    
    def test_subtract_number(self):
        """testing subtracting numbers togther"""     
        res = subtract(6, 5)
        self.assertEqual(res, 1)