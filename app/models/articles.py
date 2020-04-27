class Articles:
    '''
    Article class that defines the article objects
    '''

    def __init__(self, author, title, description, url, urlToImage):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage