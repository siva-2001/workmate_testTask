from importlib import import_module
from typing import Optional, Callable, get_type_hints

class Router:
    _routes: [str] = []
    module = "reports"

    def __init__(self):
        imported = import_module(self.module)
        if not hasattr(imported, '__all__'): print("В модуле нет перечисления подключаемых очётов")
        self._routes = imported.__all__
        del imported

    def get_method(self, method: str) -> Optional[Callable]:
        try:
            if self._exists(method):
                return getattr(import_module(self.module), method)
            else:  print("Требуемый отчёт не существует, список отчётов: " + str(self._routes))
        except AttributeError:
            print("Требуемый отчёт не добавлен в список публичных функций модуля: " + str(self._routes))
            return None

    def _exists(self, method):
        if method in self._routes: return True
        return False

    def check_args(self, func: Callable, data: dict) -> bool:
        hints = get_type_hints(func)
        for arg, arg_type in hints.items():
            if arg not in data:
                return False
            if not isinstance(data[arg], arg_type):
                return False
        return True

router = Router()

