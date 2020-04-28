class Source:
    """
    source class to define sources Objects
    """

    def __init__(self, name, category, country, language, url, description, source_id):
        self.name = name
        self.category = category
        self.country = country
        self.language = language
        self.url = url
        self.description = description
        self.source_id = source_id


class Articles:
    '''
    Article class that defines the article objects
    '''

    def __init__(self, author, title, description, url, urlToImage, source_id):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.source_id = source_id


