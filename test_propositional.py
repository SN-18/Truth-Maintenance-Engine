import unittest

from propositional import TMS


class TestAssert(unittest.TestCase):
    def test1(self):
        tms=TMS([])
        tms.assert_s([18,'d','v'])
        assert tms.kb[0]==[18,'d','v']
        # tms.assert_s([1,'c','d'])
        # assert tms.kb==[[18,'d','v'],[1,'c','d']]
        # self.assertEqual(tms.assert_s([1, 'a', 'b']), [[2, 'b'], [3, 'c', 'd'], [4, 'a', 'b']])

class TestRetract(unittest.TestCase):
    def test1(self):
        tms=TMS([])
        tms.assert_s([1,'a'])
        tms.assert_s([2,'b'])
        tms.assert_s([3,'c','d'])
        tms.assert_s([4,'a','b'])

        tms.retract_s(['1'])
        print(tms.kb)
        self.assertEqual(tms.kb,[[2, 'b'],[3, 'c', 'd'],[4,'a','b']])
        # assert tms.kb!=

if __name__=='__main__':
    unittest.main()





