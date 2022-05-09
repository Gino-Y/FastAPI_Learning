"""
typing
"""
from typing import List, Union, NewType


def get_name(name: str) -> str:
    new_name = name.split('.')[0]
    return new_name


def test_sum(num: int) -> int:
    return num + 1


def is_ok(b: bool) -> str:
    if b:
        return 'ok'
    else:
        return 'not ok'


my_list = List[int or str]


def get_new_list(li: my_list) -> Union[int, str, bool]:
    return li

