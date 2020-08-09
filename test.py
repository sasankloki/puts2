import unittest
import main


class AdvanceCalc(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def testEmpty_Page(self):
        # Test the page with an empty route
        reply = self.app.get("/")
        self.assertEqual(b'Usage: <operation>?<X1, X2, X3, ..., XN>\n', reply.data)

    def test_avg(self):
        reply = self.app.get("/average?X=1,2,3,4,5,6")
        self.assertEqual(b'3.5\n', reply.data)

        reply = self.app.get("/mean?X=2,3,4,6")
        self.assertEqual(b'3.75\n', reply.data)

        reply = self.app.get("/avg?X=2,3,4")
        self.assertEqual(b'3\n', reply.data)

        reply = self.app.get("/average?X=10,2.8,100")
        self.assertEqual(b'37.6\n', reply.data)

        reply = self.app.get("/mean?X=10,2.8,100")
        self.assertEqual(b'37.6\n', reply.data)

        reply = self.app.get("/avg?X=10,2.8,100")
        self.assertEqual(b'37.6\n', reply.data)

    def test_minimum(self):
        # Test script for taking  maniumum value in a given input
        reply = self.app.get("/min?X=15,1,57,37,8,34,5")
        self.assertEqual(b'1\n', reply.data)

        reply = self.app.get("/min?X=1,2,45,7,0,7.5,3")
        self.assertEqual(b'0\n', reply.data)

    def test_maximum(self):
        reply = self.app.get("/max?X=15,1,57,37,8,34,5")
        self.assertEqual(b'57\n', reply.data)

        reply = self.app.get("/max?X=1,2,45,7,0,7.5,3")
        self.assertEqual(b'45\n', reply.data)


if __name__ == "__main__":
    unittest.main()
