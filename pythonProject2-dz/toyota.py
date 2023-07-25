class Toyota:
    def __init__(self):
        self.color = None
        self.shift = None
    def drive(self):
        print("Car start")

    def change_color(self, color):
        self.color = color

    def change_shift(self, shift):
        self.shift = shift
a = Toyota()
a.drive()

print(a.__dict__)
