class Movie:
    def __init__(self,name,genere,watched):
        self.name = name
        self.genere = genere
        self.watched = watched
    def __repr__(self):
        return "<Movie {} >".format(self.name)    