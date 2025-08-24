import json
import time

from tabulate import tabulate

__all__ = ["average", "some_report"]

def average(files: list, dates: str | None = None):
    try:
        urlStat = {}

        def addRequestToStat(elem):
            if elem['url'] in urlStat.keys():
                urlStat[elem['url']]["total"] = urlStat[elem['url']]["total"] + 1
                urlStat[elem['url']]["responses_time"].append(elem["response_time"])
            else:
                urlStat[elem['url']] = {
                    "total": 1,
                    'responses_time': [elem["response_time"]],
                }

        for filePath in files:
            with open(filePath, 'r') as f:
                strNotes = f.read().split("\n")

            for strNote in strNotes:
                if len(strNote) != 0:
                    elem = json.loads(strNote)
                    if dates:
                        for date in dates: time.strptime(date, '%Y-%m-%d')
                        if elem['@timestamp'].split("T")[0] in dates: addRequestToStat(elem)
                    else: addRequestToStat(elem)

        listToView = []
        for url in urlStat:
            listToView.append((url,
                               urlStat[url]["total"],
                               (sum(urlStat[url]["responses_time"]) / len(urlStat[url]["responses_time"]))))

        # ВЫВОД ТАБЛИЦЫ
        if dates: print("\n Статистика за даты:\n" + "\n".join(dates))
        print(tabulate(listToView,
                       headers=["End point URL", "Total request number", "Average time"],
                       tablefmt="grid"))

        return 0

    except FileNotFoundError:
        print(f"Указанный файл {filePath} не найден.")
        return "fileNotFound"
    except json.decoder.JSONDecodeError:
        print(f"Содержимое файла {filePath} невозможно декодировать. Формат не соответствует JSON")
        return "fileFormatError"
    except ValueError:
        print("Неверный формат параметра --date, необходимо: YYYY-MM-DD/YYYY-MM-D/YYYY-M-DD/YYYY-M-D")
        return "dateFormatError"

