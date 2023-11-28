# Initializing the lists to store two friends' movie preferences
friend1_movies = []

# Ask the first friend to enter the movies they like
movie = input("Friend 1, enter the movies you like (comma-separated): ")
friend1_movies.append(movie)

common_movies = 0

while True:
    # Ask the second friend to enter the movie they like
    friend2_movie = input("Friend 2, enter a movie you like: ")
    
    if friend2_movie in friend1_movies:
        print(f"You both like {friend2_movie}")
        common_movies += 1
    
    if common_movies >= 3:
        break
    else:
        print("Try again")

print("You both have at least 3 movies in common")
print(", ".join(friend1_movies))