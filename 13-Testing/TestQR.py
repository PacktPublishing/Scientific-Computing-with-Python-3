import unittest
import numpy.testing as npt
from scipy.linalg import qr
from scipy import *

class TestQR(unittest.TestCase):
    def setUp(self):
        self.A=rand(10,10)
        [self.Q,self.R]=qr(self.A)
    def test_orthogonal(self):
        npt.assert_allclose(
            dot(self.Q.T,self.Q),identity(self.Q.shape[0]), atol=1.e-12)
    def test_sanity(self):
             npt.assert_allclose(dot(self.Q,self.R),self.A)
if __name__=='__main__':
    unittest.main()
