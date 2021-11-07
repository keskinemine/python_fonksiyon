myList = [1,2,3]
# myString = 'my string'

# print(len(myList))
# print(len(myString))
# print(type(myList))
# print(type(myString))


class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi oluşturuldu.')

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print('film silindi')

m = Movie('filmin adı', 'yönetmen adı', 123)


# print(str(myList))
print(str(m))
# print(len(myList))
# print(len(m))


