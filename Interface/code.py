from flask import Flask , render_template , url_for , request
import json
import codecs
import pyodbc 
from tqdm.notebook import tqdm
from elasticsearch import Elasticsearch
import requests


es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])



app = Flask(__name__ , template_folder = 'templates')
@app.route("/")
def index():
    return render_template('index.html')



@app.route("/" , methods=["GET","POST"])
def search():
    if request.method == "POST" :
        ayah = request.form["search-query"]
        query_body = {
                        "size":1000,
                        "query": {
                        "match": {
                        "aya_no_chakl": {
                        "query":ayah
                                        }
                                        }
                                        }
                                        }
      
        result = es.search(index="quran1", body=query_body)
        return render_template('search.html',result=result)
        


if __name__ == "__main__":
    app.run()