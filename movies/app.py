from movie import Movie
from user import User
with open('my_file.txt','w') as f:
    f.write('Hello new file whats up')
my_movie = Movie("The Matrix","Sci-fi",True)
user = User("Jose")
user.movies.append(my_movie)
with open('my_file.txt','r') as g:
    print(g.readline()) 
print(my_movie,user.watched_movie())
#user.save_to_file()
userlist = User.load_from_file(user.name + '.txt')
