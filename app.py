from configparser import MAX_INTERPOLATION_DEPTH
from newspaper import Article

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
    if not (article.publish_date is None):
        publish_date = str(article.publish_date)
    else:
        publish_date = None

    return jsonify(
        title=article.title,
        text=article.text,
        topImage=article.top_image,
        images=list(article.imgs),
        authors=article.authors,
        publishDate=publish_date,
        movies=article.movies,
        summary=article.summary,
        metaLang=article.meta_lang,
        metaDescription=article.meta_description,
        metaKeywords=article.meta_keywords
    )