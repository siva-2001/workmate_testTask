# ОБРАБОТКА ИСКЛЮЧЕНИЯ ПРИ ВВОДЕ
#   ФАЙЛА НЕ ТОГО ТИПА
#   ОТСУТСТВУЮЩИЙ ФАЙЛ
#   ФОРМАТ ДАТЫ НЕВЕРНЫЙ
#   ВВЕДЕНА НЕ ДАТА
#   ВВЕДЁН НЕСУЩЕСТВУЮЩИЙ ОТЧЁТ
# ОШИБКИ РОУТЕРА
from conftest import router_object
from router import router
import pytest

def test_router_get_method(router_object):
    method_name = "average"
    assert type(router_object.get_method(method_name)) == type(lambda x: x)

def test_router_get_method2(router_object):
    method_name = "dont_existing_method"
    assert type(router_object.get_method(method_name)) != type(lambda x: x)

def test_router_get_method3(router_object):
    method_name = "some_report"
    assert type(router_object.get_method(method_name)) != type(lambda x: x)

def  test_check_args_method1(router_object):
    def someMethod(a: int, b: str): pass
    assert router_object.check_args(someMethod, {"a": 3, "b": "5"}) == True

def  test_check_args_method2(router_object):
    def someMethod(a: int, b: str): pass
    assert router_object.check_args(someMethod, {"a": 3, "b": 5}) == False

def  test_check_args_method3(router_object):
    def someMethod(a: int, b: str): pass
    assert router_object.check_args(someMethod, {"a": 3}) == False

def test_average_report_simple(router_object):
    report_method = router_object.get_method("average")
    assert report_method(files=['example1.log']) == 0

def test_average_report_with_date(router_object):
    report_method = router_object.get_method("average")
    assert report_method(files=['example1.log'], dates=["2025-11-15"]) == 0

def test_average_report_two_files(router_object):
    report_method = router_object.get_method("average")
    assert report_method(files=['example1.log', 'example2.log']) == 0

def test_average_report_unexist_file(router_object):
    report_method = router_object.get_method("average")
    assert report_method(files=['example1.log', 'example3.log']) == "fileNotFound"

def test_average_report_file_format_error(router_object):
    report_method = router_object.get_method("average")
    assert report_method(files=['example1.log', 'main.py']) == "fileFormatError"

def test_average_report_date_format_error(router_object):
    report_method = router_object.get_method("average")
    assert report_method(files=['example1.log'], dates=["2025-14-2"]) == "dateFormatError"