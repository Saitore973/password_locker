import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def SetUp(self):
        self.new_account = User("awadh","Dreezy@84")