from fastapi import FastAPI, Query, UploadFile, File, HTTPException
import collections, shutil, os
from typing import List
from starlette.responses import FileResponse

app = FastAPI(
    title = "Оруджов Рамил"
)

@app.post('/filter/case_sensitive')
def post_word(request: List[str] = Query([])):
    dup_reqeust = [item for item, count in collections.Counter(request).items() if count > 1]
    r1 = [x.lower() for x in request]
    r2 = [x.lower() for x in dup_reqeust]
    res = list(set(r1) ^ set(r2))
    return res

@app.post("/upload/<file_name>")
def Data_aggregation(file: UploadFile = File(...)):
    error_files = "Файл имеет не подходящий формат. Используйте форматы: .csv, .json"
    if file.filename.endswith((".csv", ".json")):
        with open(f'{file.filename}', 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"file": file}
    else:
        raise HTTPException(status_code=415, detail=error_files)

@app.post("/load/{filename}")
def load_file(filename: str):
    path = os.path.join(filename)
    if os.path.isfile(path):
        return FileResponse(path)
    else:
        raise HTTPException(status_code=404, detail="file not found: " + filename)