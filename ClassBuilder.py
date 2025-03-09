class ClassBuilder:
    def __init__(self, class_name):
        self.name = class_name

    def say_hi(self):
        print("Hello " + self.name)


if __name__ == "__main__":
    test_class = ClassBuilder("TestClass")
    test_class.say_hi()