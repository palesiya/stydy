import json
from functools import wraps


def log(file_name):

    def _dec(func):
        @wraps(func)
        def worker(*args):
            res = func(*args)
            try:
                with open(file_name, "w") as log_file:
                    log_file.write(json.dumps(func(*args), indent=4, ensure_ascii=False))
            except:
                print("Ошибка с файлом")
            return res
        return worker
    return _dec
