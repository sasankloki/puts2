import unittest
import main

class AdvanceCalc(unittest.TestCase):

    
    def setUp(self) -> None:
        main.app.testing = True
        self.app = main.app.test_client()

    
    
    def test_max(self):

        #Test script for taking  maximum value in a given list
        reply=self.app.get("/max?X=15,35,200,50,45")
        self.assertEqual(b'200 \n',reply.data)

        reply=self.app.get("/max?X=15,35,20.7,50.78,45.9")
        self.assertEqual(b'50.78 \n',reply.data)


if __name__ == "__main__":
    unittest.main()