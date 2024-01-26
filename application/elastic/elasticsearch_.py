import os

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

client = Elasticsearch(os.getenv("ELASTICSEARCH_URL"))

s = Search(using=client).query("match", currency="EUR")

response = s.execute()
print(s.to_dict())

print(response.to_dict())

for hit in s.to_dict():
    print(hit['category'])
