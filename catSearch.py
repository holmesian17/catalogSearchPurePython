records = []

class record():
    name = "book"
    description = "this is a description. whatever." 
    rankingAdditive = 0
    numberOfHolds = 0

def lookyLoo(record):
    
def doASearch():
    currentResults = []
    searchTerm = input('Search for something: ')
    if searchTerm in records:
        for record in records:
            currentResults += record
    else:
        continue
    print(currentResults)
