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
        
def showResults():        
    print("Your search results: " + currentResults)
    selectionPrompt = input('Type the name of the item you wish to view: ')
    if selectionPrompt != currentResults:
        print(selectionPrompt)
    else:
        print(record)
        
