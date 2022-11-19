"""
typing
"""
from typing import List, Union, NewType, Callable, TypeVar, Generic, Any


def get_name(name: str) -> str:
    new_name = name.split('.')[0]
    return new_name


def my_sum(num: int) -> int:
    return num + 1


def is_ok(b: bool) -> str:
    if b:
        return 'ok'
    else:
        return 'not ok'


my_list = List[int or str]


def get_new_list(li: my_list) -> Union[int, str, bool]:
    return li


# NewType: 用于类型检查
Id = NewType('Id', int)
print(Id('111'))


# Callable: 作为返回值
def print_name(name: str):
    print(name)


def is_callable(call: Callable[[str], None]):
    return call


print_name('Gino')
myCallable = isinstance(print_name, Callable)
print(myCallable)
print('---')
call = is_callable(print_name)
call('gino')

# 泛型
T = TypeVar('T')


def get_all_data(data: T):
    print(data)


print('---')
get_all_data(111)
get_all_data('Gino')


# 自定义泛型类
class UserInfo(Generic[T]):
    def __init__(self, v: T):
        self.v = v

    def get(self):
        return self.v


user = UserInfo(111)
res = user.get()
print('---')
print(res)

