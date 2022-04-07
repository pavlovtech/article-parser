from configparser import MAX_INTERPOLATION_DEPTH
from newspaper import Article
from datetime import datetime

#import nltk
#import ssl

#try:
#    _create_unverified_https_context = ssl._create_unverified_context
#except AttributeError:
#    pass
#else:
#    ssl._create_default_https_context = _create_unverified_https_context

#nltk.download()

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/api/v1/parse", methods=['POST'])
def get_text():
    print(request)

    request_data = request.get_json()

    url = request_data['url']

    article = Article(url)

    article.download()

    article.parse()
    article.nlp()
    article.fetch_images()

    publish_date = None

    if article.publish_date is not None:
        article_meta_data = article.meta_data
        publish_date = sorted({value for (key, value) in article_meta_data.items() if key == 'pubdate'})

    return jsonify(
        title=article.title,
        text=article.text,
        topImage=article.top_image,
        images=list(article.imgs),
        authors=article.authors,
        publishDate=str(publish_date),
        movies=article.movies,
        summary=article.summary,
        metaLang=article.meta_lang,
        metaDescription=article.meta_description,
        metaKeywords=article.meta_keywords
    )