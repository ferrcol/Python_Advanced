class Movie:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Movie: {self.name}"