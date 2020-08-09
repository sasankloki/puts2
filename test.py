import unittest
import main

class AdvanceCalc(unittest.TestCase):

    
    def setUp(self) -> None:
        main.app.testing = True
        self.app = main.app.test_client()

    
    
    def Empty_Page(self):
        #Test the page with an empty route

        reply = self.app.get("/median?X=1,2,0,3,4,100,-15,-20,-3")
        self.assertEqual(b'1 \n', reply.data)