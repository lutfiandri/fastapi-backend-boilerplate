from fastapi import APIRouter, HTTPException, UploadFile

from app.utils.gcs import upload_file

router = APIRouter(prefix="/api/ai", tags=["users"])


@router.post("/extract")
async def extract(files: list[UploadFile]):
    allowed_types = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "application/vnd.ms-excel",
        "text/csv",
    ]

    uploaded_urls: list[str] = []

    for file in files:
        if file.content_type not in allowed_types:
            raise HTTPException(
                status_code=400,
                detail="Only PDF, Excel and CSV files are allowed",
            )

        try:
            public_url = await upload_file(file)
            uploaded_urls.append(public_url)

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to upload file {file.filename}: {str(e)}",
            ) from e
