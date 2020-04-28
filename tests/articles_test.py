import unittest
from app.models import Articles


class TestArticles(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''

    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_article = Articles('Alex', 'Tech is great', 'Advanced technology improving life',
                                    'https://twiter.com', 'https://google.com/images')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.author, 'Alex')
        self.assertEquals(self.new_article.title, 'Tech is great')
        self.assertEquals(self.new_article.description, 'Advanced technology improving life')
        self.assertEquals(self.new_article.url, 'https://twittwer.com')
        self.assertEquals(self.new_article.urlToImage, 'https://google.com/images')