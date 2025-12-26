from abc import ABC, abstractmethod

class Sample(ABC):
    @abstractmethod
    def display(self):
        pass

class Demo(Sample):
    def display(self):
        print("Abstract method implemented")

obj = Demo()
obj.display()
