from googlesearch import search

class Google:
    def __init__(self):
        self.resultsNum = 5

    def search(self, query):
        resultsNum = self.resultsNum
        results = []
        for res in search(query, tld="co.in", num=resultsNum, stop=resultsNum, pause=3):
            results.append(str(res))

        resString = '\n'.join(r for r in results)
        return resString

# obj = Google()
# res = obj.search("nodejs")
# print(type(res))
# print(res)

