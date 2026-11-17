
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
try:
    df = pd.read_csv("movies.csv", dtype=str, keep_default_na=False)
except FileNotFoundError:
    print("Error: movies.csv file not found!")
    exit()

# Check required columns
required = ["Movie", "Genre", "Rating"]

if not all(col in df.columns for col in required):
    print("Error: CSV must contain Movie, Genre and Rating columns.")
    exit()

valid_movies = []
seen = set()

# Validate data
for index, row in df.iterrows():

    row_no = index + 1
    movie = row["Movie"].strip()
    genre = row["Genre"].strip()
    rating = row["Rating"].strip()

    if not movie or not genre or not rating:
        print(f"Row {row_no} skipped: Missing values.")
        continue

    try:
        rating = float(rating)
    except ValueError:
        print(f"Row {row_no} skipped: Invalid rating '{rating}'.")
        continue

    if rating < 0 or rating > 10:
        print(f"Row {row_no} skipped: Rating {rating:g} must be between 0 and 10.")
        continue

    record = (movie, genre, rating)

    if record in seen:
        print(f"Row {row_no} skipped: Duplicate row.")
        continue

    seen.add(record)

    valid_movies.append({
        "Movie": movie,
        "Genre": genre,
        "Rating": rating
    })

# Create DataFrame
movies = pd.DataFrame(valid_movies)

print(f"\nValid rows: {len(movies)}")

if movies.empty:
    print("No valid movie records found!")
    exit()

# Menu
print("\nMOVIE RATING ANALYZER")
print("1. Summary")
print("2. Genre-wise Average")

choice = input("Enter your choice: ")

# Option 1
if choice == "1":

    average = movies["Rating"].mean()
    top = movies.loc[movies["Rating"].idxmax()]
    lowest = movies.loc[movies["Rating"].idxmin()]

    print("\n--- MOVIE SUMMARY ---")
    print(f"Average rating: {average:.2f}")
    print(f"Top rated: {top['Movie']} ({top['Rating']})")
    print(f"Lowest: {lowest['Movie']} ({lowest['Rating']})")

    plt.figure(figsize=(8, 5))
    plt.bar(movies["Movie"], movies["Rating"])
    plt.title("Movie Ratings")
    plt.xlabel("Movies")
    plt.ylabel("Ratings")
    plt.ylim(0, 10)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.hist(movies["Rating"], bins=5, edgecolor="black")
    plt.title("Movie Rating Histogram")
    plt.xlabel("Ratings")
    plt.ylabel("Number of Movies")
    plt.tight_layout()
    plt.show()

# Option 2
elif choice == "2":

    genre_avg = movies.groupby("Genre")["Rating"].mean()

    print("\n--- GENRE-WISE AVERAGE ---")

    for genre, rating in genre_avg.items():
        print(f"{genre}: {rating:.2f}")

    print(f"\nBest genre: {genre_avg.idxmax()}")

    plt.figure(figsize=(8, 5))
    genre_avg.plot(kind="bar")
    plt.title("Genre-wise Average Rating")
    plt.xlabel("Genre")
    plt.ylabel("Average Rating")
    plt.ylim(0, 10)
    plt.tight_layout()
    plt.show()

else:
    print("Invalid menu choice!")
