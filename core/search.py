from flask import current_app
from elasticsearch import Elasticsearch

def CoreSearch(app):
    if 'ELASTICSEARCH_URL' in app.config and app.config['ELASTICSEARCH_URL']:
        return Elasticsearch([app.config['ELASTICSEARCH_URL']])

def add_to_index(index, model):
    try:
        if not current_app.elasticsearch:
            return
        payload = {}
        for field in model.__searchable__:
            payload[field] = getattr(model, field)
        current_app.elasticsearch.index(index=index, id=model.id, body=payload)
    except Exception as e:
        print(e)

def remove_from_index(index, model):
    if not current_app.elasticsearch:
        return
    current_app.elasticsearch.delete(index=index, id=model.id)

def query_index(index, query, page, per_page):
    if not current_app.elasticsearch:
        return [], 0
    search = current_app.elasticsearch.search(
        index=index,
        body={'query': {'multi_match': {'query': query, 'fields': ['*']}},
              'from': (page - 1) * per_page, 'size': per_page})
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    return ids, search['hits']['total']['value']