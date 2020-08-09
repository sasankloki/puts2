import unittest
import main

class AdvanceCalc(unittest.TestCase):

    
    def setUp(self) -> None:
        main.app.testing = True
        self.app = main.app.test_client()

    
    
    def test_max(self):

        #Test script for taking  maximum value in a given list
        reply=self.app.get("/max?X=15,35,200,500,459")
        self.assertEquals(b'500\n',reply.data)

        reply=self.app.get("/max?X=15,35,20.7,50.78,45.9")
        self.assertEquals(b'500\n',reply.data)
