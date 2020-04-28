import unittest
from app.models import Source


class SourceTest(unittest.TestCase):
    '''
    Test class to test the behavior of the Source class
    '''

    def setUp(self):
        '''
        Set Up method that will run before evert test
        '''
        self.new_source = Source('name', 'cartegory', 'country', 'language', 'url', 'description')

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))



