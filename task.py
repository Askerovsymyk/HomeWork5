from art import tprint
from class1 import NewClass

tprint("PYTHON")

class hello:
    def greet(self):
        print("Hello, world!")

def tprint(instance):
    if hasattr(instance, 'greet'):
        instance.greet()
    else:
        print("Instance has no method 'greet'.")

if __name__ == "__main__":
    obj = NewClass()
    tprint(obj)