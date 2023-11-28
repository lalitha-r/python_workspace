# Ask the first friend for movies they like and save them in a list
friend1_movies= input("Friend 1, what movies do you like? (comma-separated): ")
friend1_movie_list = friend1_movies.split(',')

#initializing the common movie count as 0
common_movie=[]
common_movie_count = 0

while True:
    # Ask the second friend for a movie
    friend2_movie = input("Friend 2, enter a movie you like: ")

    # Check if the movie is in the first friend's list
    if friend2_movie in friend1_movie_list:
        common_movie.append(friend2_movie)
        print(f"You both like '{friend2_movie}'")
        common_movie_count += 1
    
    # Check if we reached the required common movies
    if common_movie_count >= 3:
        break
    else:
        print("Try again")

print("\nYou both have at least 3 favorite movies in common:")
print(f"movies in common:{common_movie}")

