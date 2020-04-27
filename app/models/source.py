class Source:
    """
    source class to define sources Objects
    """

    def __init__(self, name, category, country, language, url, description):
        self.name = name
        self.category = category
        self.country = country
        self.language = language
        self.url = url
        self.description = description
