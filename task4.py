movies = {
    "Avengers": "Action",
    "John Wick": "Action",
    "Titanic": "Romance",
    "Romeo Juliet": "Romance",
    "Interstellar": "Sci-Fi",
    "Enthiran": "Sci-Fi",
    "Toy Story": "Animation",
    "Finding Nemo": "Animation"
}

user_preferred = input("Enter your preferred genre (Action/Romance/Sci-Fi/Animation): ")

print("\nRecommended Movies for you:")
found = False

for movie, genre in movies.items():
    if genre.lower() == user_preferred.lower():
        print("-", movie)
        found = True

if not found:
    print("Sorry, no movies found for this genre.")
