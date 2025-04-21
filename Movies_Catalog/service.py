import os


class Service:

    def __init__(self):
        self.file_name = "Movies_Catalog/movies.txt"

    def add_movie(self, movie):
        with open(self.file_name, "a", encoding="utf8") as file:
            file.write(f"{movie.name}\n")

    def list_movies(self):
        with open(self.file_name, "r", encoding="utf8") as file:
            print("  ***  Movie List  ***  ")
            print(file.read())

    def remove_movies_file(self):
        os.remove(self.file_name)
        print(f"File removed: {self.file_name}")