# ОБРАБОТКА ИСКЛЮЧЕНИЯ ПРИ ВВОДЕ
#   ФАЙЛА НЕ ТОГО ТИПА
#   ОТСУТСТВУЮЩИЙ ФАЙЛ
#   ФОРМАТ ДАТЫ НЕВЕРНЫЙ
#   ВВЕДЕНА НЕ ДАТА
#   ВВЕДЁН НЕСУЩЕСТВУЮЩИЙ ОТЧЁТ
# ОШИБКИ РОУТЕРА

import pytest
from router import router

@pytest.fixture(scope='module')
def router_object():
    yield router



def test_router_get_method2(router_object):
    method_name = "average"
    assert type(router_object.get_method(method_name)) == type(lambda x: x), "роутер не возвращает функцию: тест провален"

def  test_check_args_method(router_object):
    def someMethod(a: int, b: str): pass
    args = {"a":3, "b":"5"}
    assert router_object.check_args(someMethod, args)

def  test_check_args_method2(router_object):
    def someMethod(a: int, b: str): pass
    args = {"a":3}
    assert not router_object.check_args(someMethod, args)

