from movie import Movie
from service import Service


class AppMoviesCatalog:

    def __init__(self):
        self.service = Service()

    def menu(self):
        print("  *** App Movies Catalog ***  ")
        while True:
            try:
                print(f'''Options:
                1 . Add movie
                2 . List movies
                3 . Delete movies catalog
                4 . Exit''')
                choice = int(input("Select one option: "))

                if choice == 1:
                    name_movie = input("New movie name:")
                    movie = Movie(name_movie)
                    self.service.add_movie(movie)
                elif choice == 2:
                    self.service.list_movies()
                elif choice == 3:
                    self.service.remove_movies_file()
                elif choice == 4:
                    print("Exit the program:")
                    break
                else:
                    print("Invalid option")

            except ValueError:
                print("Error: invalid number")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    app = AppMoviesCatalog()
    app.menu()