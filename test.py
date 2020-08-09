import unittest
import main

class AdvanceCalc(unittest.TestCase):

    
    def setUp(self) -> None:
        main.app.testing = True
        self.app = main.app.test_client()

    
    
    def Empty_Page(self):
        #Test the page with an empty route

        reply = self.app.get("/")
        self.assertEqual(b'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n', reply.data)