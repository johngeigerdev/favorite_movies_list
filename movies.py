#ask the user if would like to add, remove or view favorite movies
fav_Movies = []

def addMovie():
    movie = input("Please list a movie to add. Press 'q' to end. ")
    if input != "q":
        fav_Movies.append(movie.title())
    else:
        break

def reMovie():
    prompt(input("Please type the name of the movie to remove. Press 'q' to quit. "))
    fav_Movies.remove(input(prompt))

def viewMovies():
    for movie in fav_Movies[:]:
        print(movie.title())

    prompt = "Hello, this program will allow you to add, remove or view a list of your favorite movies. "
    prompt += "\nWould you like to add, remove or view your list? "

if prompt == "add":
    addMovie()
elif input(prompt) == "remove":
    reMovie()
else: viewMovies()




#if view, type, "view"

#if add, ask the user to input favorite movies and press "q" when finished

#if remove, ask user to type movie to remove


print(prompt)