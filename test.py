import unittest
import main

class AdvanceCalc(unittest.TestCase):

    
    def setUp(self) -> None:
        main.app.testing = True
        self.app = main.app.test_client()

    
    
    def min_test(self):

        #Test script for taking  maniumum value in a given input
        reply=self.app.get("/min?X=15,1,57,37,8,34,5")
        self.assertEqual(b'1\n',reply.data)

        reply=self.app.get("/min?X=1,2,45,7,0,7.5,3")
        self.assertEqual(b'0\n',reply.data)


if __name__ == "__main__":
    unittest.main()