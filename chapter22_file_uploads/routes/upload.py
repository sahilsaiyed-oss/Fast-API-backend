from fastapi import APIRouter, UploadFile, File
import shutil

router = APIRouter(prefix="/files", tags=["File Uploads"])


@router.post("/upload")
def upload_file(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "File uploaded successfully"
    }