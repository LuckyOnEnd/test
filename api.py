import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class FilePaths(BaseModel):
    paths: List[str]

FILE_PATH = "files.txt"

@app.post("/upload_paths")
async def upload_paths(file_paths: FilePaths):
    if not os.path.exists(FILE_PATH):
        open(FILE_PATH, "w").close()

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        for path in file_paths.paths:
            f.write(path + "\n")

    return {"message": f"Сохранено {len(file_paths.paths)} файлов в {FILE_PATH}"}
