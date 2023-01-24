from fastapi import FastAPI, Query
from schemas import Request, Word
from typing import List

app = FastAPI()

@app.get('/request')
def get_book(test_list: List[str] = Query([])):
    new_list = []
    [new_list.append(x) for x in test_list if x not in new_list]
    return new_list

