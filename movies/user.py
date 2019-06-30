from movie import Movie
class User:
    def __init__(self,name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)    

    def watched_movie(self):
        return list(filter(lambda x: x.watched,self.movies))

    def add_moovie(self,name,genere):
        movie = Movie(name,genere,False)
        self.movies.append(movie)

    def delete_moovie(self,name):
         return list(filter(lambda x : x.name != name,self.movies))     

    def save_to_file(self):
      with open('{}.txt'.format(self.name),'w') as f:
          f.write(self.name + '\n')
          for  movie in self.movies:
               f.write('{},{},{}\n'.format(movie.name,movie.genere,str(movie.watched)))
     @classmethod                  
    def load_from_file(cls,filename):
      with open(filename,'r') as f:
        content = f.readlines();
        username = content[0]
        allMovies = []
        print(content,'content===')
        for movie in content:
            movies_data = movie.split(",")
            print(movies_data,'datttttt')
            if  len(movies_data)>1:    
                allMovies.append(Movie(movies_data[0] , movies_data[1] , movies_data[2]=="True"))

        user = cls(username)
        user.movies = allMovies
        return user        
      def convert_to_json(self):
          return{
            "name":self.name,
            "movies":[
              movies.json() for movie in self.movies

            ]
        
        
           }  