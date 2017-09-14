#!/usr/bin/env python3
import requests, sys

searchPath = 'https://api.github.com/search/repositories?q='

def main():
    searchTerm = None
    if len(sys.argv) <= 1:
        searchTerm = input("Please enter your search term:")
    else:
        searchTerm = ' '.join(sys.argv[1:])
    print("Searching Github for repos using search term:'%s'" % searchTerm)
    repos = requests.get(searchPath+searchTerm).json()
    print("%i results found."%repos['total_count'])

    print("Top 30 Items:")
    for line in ["%s(%s)[%i]"%(item['name'],item['full_name'],item['watchers_count']) for item in repos['items']]:
        print('   '+line)

    

if __name__ == '__main__':
    main()


#Useful links:
#     http://docs.python-requests.org/en/latest/user/quickstart/
#     https://developer.github.com/v3/search/
#     
