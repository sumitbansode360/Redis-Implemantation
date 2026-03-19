import redis
import time
import json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

#Fake db function
def get_books_from_db():
    print("fetching from db...")
    time.sleep(2)
    return [
        {"id": 1, "name": "book1"},
        {"id": 2, "name": "book2"},
    ]

def get_books():
    cache_key = "cache:books"

    # get from redis
    books = r.get(cache_key)

    if books:
        print("fetching from redis...")
        return json.loads(books)
    
    # get from db
    books = get_books_from_db()

    # store in redis
    r.set(cache_key, json.dumps(books), ex=60)

    return books

print(get_books())
print(get_books())
print(get_books())

