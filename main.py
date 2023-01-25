

from fastapi import FastAPI, Query, UploadFile, File, HTTPException
import collections, shutil
from typing import List

app = FastAPI(
    title = "Оруджов Рамил"
)

@app.post('/filter')
def post_word(request: List[str] = Query([])):
    dup_reqeust = [item for item, count in collections.Counter(request).items() if count > 1]
    r1 = [x.lower() for x in request]
    r2 = [x.lower() for x in dup_reqeust]
    res = list(set(r1) ^ set(r2))
    return res

@app.post("/upload/<file_name>")
def Data_aggregation(file: List[UploadFile] = File(...)):
    error_files = []
    for ing in file:
        if ing.filename.endswith((".csv", ".json")):
            with open(f'{ing.filename}', 'wb') as buffer:
                shutil.copyfileobj(ing.file, buffer)
            return {"file": ing}
        else:
            raise HTTPException(status_code=415, detail=error_files)
   



# @app.post("/load/{file_name}")
# def get_file(file_name):
#     return [file_name for file_name in


# @app.exception_handler(ValidationError)
# async def validation_exception_handler(request: Request, exc: ValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"detail": exc.errors()}),
#     )