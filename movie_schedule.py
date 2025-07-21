current_movies = {"The Grinch": "11:00", "Rudolph": "13:00", "Frosty the snowman":"15:00","Christmas Vacation":"17:00"}

print("We're showing the following movies:")

for key in current_movies:
    print(key)

movie_title = input("Which movie would you like to enquire about?\n")

showtime = current_movies.get(movie_title)

if showtime == None:
    print("We are not showing that movie at the moment")
else:
    print(movie_title, "is playing at: ",showtime)