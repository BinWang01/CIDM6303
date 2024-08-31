from pathlib import Path
import csv
import json

# Chapter 9.6- Working with CSV files
print("\nChapter 9.6- Working with CSV files " + "-" * 20)

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1000, 2, 15])

with open("data_noblanklines.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1000, 2, 15])

print("read all content from a csv file")
with open("data.csv") as file:
    reader = csv.reader(file)
    data = list(reader)
    print(data)

print("read each row from a csv file")
with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Chapter 9.7- Working with JSON files
print("\nChapter 9.7- Working with JSON files " + "-" * 20)
movies = [
    {"id": 1, "title": "Terminator", "year": 1984},
    {"id": 2, "title": "Kindergarten Cop", "year": 1990}
]

data = json.dumps(movies)
Path("movies.json").write_text(data)


data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0])
print(movies[1])

print(f"In what year was Kindergarten released? {movies[1].get('year')}")

for movie in movies:
    print(
        f"the movie {movie.get('title')} was released in {movie.get('year')}"
    )
