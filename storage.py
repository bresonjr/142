import csv
allArticles = []
with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allArticles = data[1:]
likedArticles = []
notLikedArticles = []