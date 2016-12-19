import unittest
from bisection import bisect

class Tests(unittest.TestCase):
    def checkifzero(self,fcn_with_zero,interval):
        result = bisect(fcn_with_zero,*interval,tol=1.e-8)
        function_value=fcn_with_zero(result)
        expected=0.
        self.assertAlmostEqual(function_value, expected)
test_data=[
           {'name':'identity', 'function':lambda x: x,
                                     'interval' : [-1.2, 1.]},
           {'name':'parabola', 'function':lambda x: x**2-1,
                                        'interval' :[0, 10.]},
           {'name':'cubic', 'function':lambda x: x**3-2*x**2,
                                       'interval':[0.1, 5.]},
               ] 
def make_test_function(dic):
        return lambda self :\
                   self.checkifzero(dic['function'],dic['interval'])
for data in test_data:
    setattr(Tests, "test_{name}".format(name=data['name']),
                                           make_test_function(data))

if __name__=='__main__':
    unittest.main()
