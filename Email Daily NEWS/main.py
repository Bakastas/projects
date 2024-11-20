import requests

api_key = "a7d63f1c2a914bd39c002a60337acbeb"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-10-21&\
    sortBy=publishedAt&apiKey=a7d63f1c2a914bd39c002a60337acbeb"

#Make requests
request = requests.get(url)

#Get dictionary with data
content = request.json()

#Output content from data
for article in content["articles"]: 
    print(article["description"])
    print(article["titles"])