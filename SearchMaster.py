# How to Perform a Google Search using python code By FR13NDS 

from googlesearch import search

# Prompt the user to enter a search query
query = input("Ingrese el término de búsqueda: ")

# Set the query you want to search
query = "Google Search using Python code"

# Set the query you want to search
query = "Google Search using Python code"

# Perform the search and specify the number of results
for result in search(query, num=10):
    print(result)