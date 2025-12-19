print("hello world")


def greet():
    print("こんにちは")


greet()


def print_name(name="name"):
    print(f'私の名前は{name}です')


print_name("まつかん")


def get_greet():
    return "おはようございます"


print(get_greet())


def add(a=0, b=0):
    return a+b


print(add(1, 2))
