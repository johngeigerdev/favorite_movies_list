#initializing blank list of favorite movies
fav_Movies = []

#function that asks for the individual values of the dictionary 'movie' and then establishes
#the keys and associates them with the values
def addMovie():
    movie_title = input("Please type the name of the movie. ")
    movie_director = input("Please type the name of the movie director. ")
    release_year = input("What year was this movie released? ")

    movie = {
        "title": movie_title,
        "director": movie_director,
        "year": release_year
    }

#this checks to see if movie is not already in the fav_moviles list and
#appends the new dictionary to the list if not already in it and notifies user
    if movie not in fav_Movies:
        fav_Movies.append(movie)
        print(f"'{movie_title}' has been added to your favorite movies list. ")
    else:
        print(f"'{movie_title}' is already in your favorite movies list. ")

"""
The below initially prints the enumerated list of moves from viewMovies function and lets the
user select the index of the movie. It ensures they don't select a number higher than the 
length of fav_Movies. If it is a number higher than indexes available, it notifies the user. If
it is within the range/length of the list, it removes the value from the list using the pop() method
and subracts one to ensure it removes the correct index from the list.
"""
def reMovie():
    viewMovies()
    movie_number = int(input("Please type the number of the movie to remove. "))
    if movie_number > len(fav_Movies):
        print(f"{movie_number} is not a valid index. ")
    else:
        fav_Movies.pop(movie_number - 1)

"""this enumerates each movie in the list and lists it to the user with an index + 1 value
for user to see each one enumerated and select a number if they want
"""
def viewMovies():
    for (index, movie) in enumerate(fav_Movies):
        print(f"{index + 1} {movie.get('title')}")
        
#this prompts the user to decide if they want to add, remove or view the list
prompt = "Hello, this program will allow you to add, remove or view a list of your favorite movies. "
prompt += "\nWould you like to add, remove or view your list? Type 'exit' to exit program. "

"""while the values are true, it will iterate through this loop and, depending on user's response
it will run one of the functions to add, remove, view or break the loop
"""
while True:
    answer = (input(prompt))

    if answer == "add":
        addMovie()
    elif answer == "remove":
        reMovie()
    elif answer == "view":
        viewMovies()
    else:
        break

