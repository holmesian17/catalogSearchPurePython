records = []

class record:
    def __init__(self, name, description, rankingAdditive, numberOfHolds)
        self.name = name
        self.description = description
        self.rankingAdditive = rankingAdditive
        self.numberOfHolds = numberOfHolds	
    
def doASearch():
    searchResults = []
    searchTerm = input('Search for something: ')
    if searchTerm != records:
	continue
    else:
	for record in records:
	    searchResults.append(record)

def showResults():
    searchResults.sort()
    print(searchResults)

