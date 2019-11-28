from googlesearch import search

class Google:
	# in constructor we are setting the the google search results limit to 5
    def __init__(self):
        self.resultsNum = 5

    def search(self, query):
        resultsNum = self.resultsNum
        results = []
		# using the search method from 'googlesearch' for query
        for res in search(query, tld="co.in", num=resultsNum, stop=resultsNum, pause=3):
            results.append(str(res))

        resString = '\n'.join(r for r in results)
        return resString



