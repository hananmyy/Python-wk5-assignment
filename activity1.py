# Base Class: Book
class Book:
    def __init__(self, title, author, genre, published_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.published_year = published_year

    def get_summary(self):
        return f"'{self.title}' by {self.author} is a {self.genre} book published in {self.published_year}."
    
    def __str__(self):
        return f"Book: '{self.title}' by {self.author}, {self.genre}, published in {self.published_year}."

# Derived Class: EBook (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, genre, published_year, file_size, format):
        super().__init__(title, author, genre, published_year)
        self.file_size = file_size
        self.format = format

    def get_file_info(self):
        return f"'{self.title}' is an eBook of size {self.file_size}MB in {self.format} format."

# Derived Class: Audiobook (inherits from Book)
class Audiobook(Book):
    def __init__(self, title, author, genre, published_year, duration, narrator):
        super().__init__(title, author, genre, published_year)
        self.duration = duration  # in hours
        self.narrator = narrator

    def get_audio_info(self):
        return f"'{self.title}' audiobook is narrated by {self.narrator} and lasts for {self.duration} hours."

# Creating instances
if __name__ == "__main__":
    # Book instance
    dust = Book("Dust", "Yvonne Adhiambo Owuor", "Literary Fiction", 2014)
    print(dust.get_summary())
    
    # EBook instance
    black_mamba_boy = EBook("Black Mamba Boy", "Nadifa Mohamed", "Historical Fiction", 2009, 3, "EPUB")
    print(black_mamba_boy.get_summary())
    print(black_mamba_boy.get_file_info())
    
    # Audiobook instance
    baba_segi_wives = Audiobook("The Secret Lives of Baba Segi's Wives", "Lola Shoneyin", "Contemporary Fiction", 2010, 9, "Lola Shoneyin")
    print(baba_segi_wives.get_summary())
    print(baba_segi_wives.get_audio_info())
