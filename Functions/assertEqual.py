# unit test case 
import unittest 

def sub(a,b):
	return a-b

class TestSub(unittest.TestCase): 
    def test_positive_numbers(self):
        result = sub(10, 5)
        self.assertEqual(result, 2)
    
    def test_negative_numbers(self):
        result = sub(-2, -2)
        self.assertEqual(result, 1)
	
    def test_large_numbers(self):
        result = sub(1000000000, 1)
        self.assertEqual(result, 999999998)

if __name__ == '__main__': 
	unittest.main() 
