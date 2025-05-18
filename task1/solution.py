"""
Необходимо реализовать декоратор @strict
Декоратор проверяет соответствие типов переданных в вызов функции аргументов типам аргументов, объявленным в прототипе функции.
(подсказка: аннотации типов аргументов можно получить из атрибута объекта функции func.__annotations__ или с помощью модуля inspect)
При несоответствии типов бросать исключение TypeError
Гарантируется, что параметры в декорируемых функциях будут следующих типов: bool, int, float, str
Гарантируется, что в декорируемых функциях не будет значений параметров, заданных по умолчанию
"""
from functools import wraps

import pytest


def strict(func):
    @wraps(func)
    def wrapper(*args,):
        classes = tuple(func.__annotations__.values())
        for i in range(len(args)):
            if type(args[i]) != classes[i]:
                raise TypeError
        return func(*args)
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    assert sum_two(1, 2) == 3
    with pytest.raises(TypeError):
        sum_two(1, 2.4)
