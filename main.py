from flask import Flask, jsonify, request
from storage import allArticles, likedArticles, notLikedArticles
from demographicFiltering import output
from contentFiltering import getRecommendations
app = Flask(__name__)
@app.route('/get-article')
def getArticle():
    movieData = {
        'url': allArticles[0][11],
        'title': allArticles[0][12],
        'text': allArticles[0][13],
        'lang': allArticles[0][14],
        'total_events': allArticles[0][15]
    }
    return jsonify({
        'data': movieData,
        'status': 'success'
    })
@app.route('/liked-article', methods = ['POST'])
def likedArticle():
    article = allArticles[0]
    likedArticles.append(article)
    allArticles.pop(0)
    return jsonify({
        'status': 'success'
    }), 201
@app.route('/unliked-article', methods = ['POST'])
def unlikedArticle():
    article = allArticles[0]
    notLikedArticles.append(article)
    allArticles.pop(0)
    return jsonify({
        'status': 'success'
    }), 201
@app.route('/popular-articles')
def popularA_articles():
    articleData = []
    for article in output:
        d = {
            'url': article[0],
            'title': article[1],
            'text': article[2],
            'lang': article[3],
            'total_events': article[4]
        }
        articleData.append(d)
    return jsonify({
        'data': articleData,
        'status': 'success'
    }), 200
@app.route('/recommended-articles')
def recommendedArticles():
    allRecommended = []
    for likedArticle in likedArticles:
        output = getRecommendations(likedArticle[4])
        for data in output:
            allRecommended.append(data)
    import itertools
    allRecommended.sort()
    allRecommended = list(allRecommended for allRecommended,_ in itertools.groupby(allRecommended))
    articleData = []
    for recommended in allRecommended:
        d = {
            'url': recommended[0],
            'title': recommended[1],
            'text': recommended[2],
            'lang': recommended[3],
            'total_events': recommended[4]
        }
        articleData.append(d)
    return jsonify({
        'data': articleData,
        'status': 'success'
    }), 200
if __name__ == '__main__':
    app.run()