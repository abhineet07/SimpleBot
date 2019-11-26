import re

class History:
    def getRecentTen(self, query):
        results = ""
        file = open('history.txt', 'r')
        lines = file.readlines()

        myregex = r'\b' + query + r's?\b'
        for i in range(0, len(lines), 1):
            if re.search(myregex, lines[i]):
                results += lines[i].strip() + "\n"

        results = results.strip()
        return results

# obj = History()
# res = obj.getRecentTen("game")
# print(type(res))
# print(res)