class Parent:
    def hello(self) -> None:
        print('Hello from Parent class')

class Child(Parent):
    def hello(self) -> None:
        super().hello()
        print('Hello from Child class')

class Base1:
    def hello(self) -> None:
        print('Hello from Base1')

class Base2:
    def hello(self) -> None:
        print('Hello from Base2')

class Child2(Base2, Base1):
    def hello(self) -> None:
        # super().hello()
        Base1.hello(self)
        print('Hello from Child2')

def main() -> None:
    # c = Child()
    # c.hello()

    c = Child2()
    c.hello()

    print(Child2.mro())


if __name__ == '__main__':
    main()