from task import hello

class NewClass(hello):
    def greet(self):
        super().greet()
        print("Hello from NewClass!")

# Тестирование
if __name__ == "__main__":
    obj = NewClass()
    obj.greet()

