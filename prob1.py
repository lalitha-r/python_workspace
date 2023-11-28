#initializing the lists to storre two friends movie
friend1_movies=[]

#ask the first friend to enter the movies he like
movie=input("friend1:enter the movies")
friend1_movies.append(movie)

common_movies=0
while True:
    friend2_movie=input("friend2: enter the movie u like")
    
    
    if friend2_movie in friend1_movies:
        print(f"you both like{friend2_movie}")
        common_movies += 1

    elif common_movies >= 3:
        break
    else:
       print("try again")

print("you both have atleat 3 movies in common")

        

    
