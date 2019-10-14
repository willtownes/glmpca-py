"""
Recommended Command line syntax:
nosetests --with-coverage --cover-erase --cover-package=glmpca
"""

import unittest
import numpy as np
from glmpca import glmpca
np.random.seed(202)

class Test_glmpca(unittest.TestCase):
    def setUp(self):
        self.Y = np.random.negative_binomial(4,.8,size=(10,5))
        self.Ybin = self.Y.copy()
        self.Ybin[self.Ybin>0] = 1
        self.g1 = glmpca.glmpca(self.Y,2,fam="poi")
    def test_glmpca_output_data_types(self):
        self.assertIsInstance(self.g1, dict)
        self.assertIsInstance(self.g1["glmpca_family"], glmpca.GlmpcaFamily)
        self.assertTrue(np.all(self.g1["factors"].shape == (5,2)))
        self.assertTrue(np.all(self.g1["loadings"].shape == (10,2)))
    def test_glmpca_deviance_decrease(self):
        self.assertTrue(np.all(np.isfinite(self.g1["dev"])))
        self.assertLess(self.g1["dev"][-1], self.g1["dev"][0])
    def test_glmpca_nb_likelihood(self):
        g1 = glmpca.glmpca(self.Y,2,fam="nb")
    def test_glmpca_mult_likelihood(self):
        g1 = glmpca.glmpca(self.Y,2,fam="mult",sz=np.array(range(1,6)))
    def test_glmpca_bern_likelihood(self):
        g1 = glmpca.glmpca(self.Ybin,2,fam="bern",penalty=10)
    def test_glmpca_dims_L1(self):
        g1 = glmpca.glmpca(self.Y,1,fam="poi")
    def test_glmpca_covariates(self):
        X = np.array(range(1,6))
        Z = np.array(range(1,11))
        g1= glmpca.glmpca(self.Y,2,fam="poi",X=X[:,None],Z=Z[:,None])
    def test_glmpca_extra_args(self):
        g1= glmpca.glmpca(self.Y,2,fam="poi",verbose=True,penalty=10)
    def test_glmpca_pre_initialized(self):
        f0 = np.random.randn(5,2)/10
        l0 = np.random.randn(10,2)/10
        g1 = glmpca.glmpca(self.Y,2,fam="poi",init={"factors":f0, "loadings":l0})
    def test_glmpca_err_range_bern(self):
        Y = self.Ybin.copy()
        Y[0,0] = 2
        self.assertRaises(glmpca.GlmpcaError, glmpca.glmpca, Y, 2, fam="bern")
    def test_glmpca_err_range_poi(self):
        Y = self.Y.copy()
        Y[0,0] = -1
        self.assertRaises(glmpca.GlmpcaError, glmpca.glmpca, Y, 2, fam="poi")
# the below test doesn't work because the log link function implemented by statmodels...
#...clips the inputs to an epsilon >0 so log(0) ends up being about -36.
# so the zero rows don't raise an error like they do in R.
    # def test_glmpca_err_zerorow(self):
    #     Y = self.Y.copy()
    #     Y[0,:] = 0
    #     self.assertRaises(glmpca.GlmpcaError, glmpca.glmpca, Y, 2, fam="poi")