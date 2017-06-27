"""A listing of the substances available in GPUMCI."""
import numpy as np

__all__ = ('substances',)


class Substance(object):
    def __init__(self, name, Z, propotion):
        """ Initialize a substance

        Parameters
        ----------
        name : `str`
            The name of the substance
        Z : `int` array-like
            The atomic numbers of the parts of the substance
        propotion : `float` array-like
            Stoichiometric propotion of the atomic parts.
        """
        self.name = str(name)
        self.Z = np.array(Z, dtype=int)
        self.propotion = np.array(propotion, dtype=float) / np.sum(propotion)
        assert self.Z.shape == self.propotion.shape

    def formula(self):
        import xraylib as xrl
        string = ''
        for z, p in zip(self.Z, self.propotion):
            string += '{}{:.6f}'.format(xrl.AtomicNumberToSymbol(z), p)
        return string

    def __repr__(self):
        return 'Substance({}, {}, {})'.format(self.name, self.Z, self.propotion)


substances = []

#http://physics.nist.gov/cgi-bin/Star/compos.pl?refer=ap&matno=104
substances += [Substance('air',
                         [6, 7, 8, 18],
                         [0.000150, 0.784396, 0.210781, 0.004673])]

#http://physics.nist.gov/cgi-bin/Star/compos.pl?refer=ap&matno=276
substances += [Substance('water',
                         [1, 8],
                         [2.0, 1.0])]

substances += [Substance('carbon',
                         [6],
                         [1.0])]

substances += [Substance('potassium',
                         [19],
                         [1.0])]

substances += [Substance('tissue',
                         [1, 6, 7, 8],
                         [0.630467, 0.058171, 0.011680, 0.299682])]

substances += [Substance('brain',
                         [1, 6, 7, 8, 11, 12, 15, 16, 17, 19, 20, 26, 30],
                         [0.654256, 0.062356, 0.005660, 0.275312, 0.000478, 0.000037, 0.000682, 0.000330, 0.000397, 0.000473, 0.000013, 0.000005, 0.000001])]

#From http://physics.nist.gov/cgi-bin/Star/compos.pl?refer=ap&matno=120
substances += [Substance('bone',
                         [1, 6, 7, 8, 12, 15, 16, 20, 30],
                         [0.474890, 0.122032, 0.030435, 0.283118, 0.000919, 0.034407, 0.000997, 0.053187, 0.000016])]

substances += [Substance('white_matter',
                         [1, 6, 7, 8, 11, 15, 17, 19],
			 [0.637572, 0.090378, 0.008183, 0.261909, 0.000329, 0.000854, 0.000213, 0.000561])]
#                         [0.1056, 0.1780, 0.0188, 0.6872, 0.00123, 0.00434, 0.00123, 0.0036])]

substances += [Substance('grey_matter',
                         [1, 6, 7, 8, 11, 15, 17, 19],
			 [0.644105, 0.052170, 0.007856, 0.293837, 0.000401, 0.000695, 0.000260, 0.000676])]
#                         [0.1058, 0.1009, 0.0179, 0.7646, 0.0015, 0.0035, 0.0015, 0.0043])]
                                  
               
               
               
