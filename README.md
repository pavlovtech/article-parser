# article-parser

Simple HTTP API endpoint that takes URL to any article and returns JSON object containing information about the article.

* Written in Python
* Based on Newspaper3k library
* Uses Flusk for HTTP API
* Dockerized

To start run the following command inside the project directory:

> flask run


## Request

POST /api/v1/parse
{
  "url": "https://yoursite.com/article1"
}

## Response

```
{
 "title": ""
 "text": ""
 "topImage": ""
 "images": ""
 "authors": ""
 "publishDate": ""
 "movies": ""
 "summary": ""
 "metaLang": ""
 "metaDescription": ""
 "metaKeywords": ""
}
```
