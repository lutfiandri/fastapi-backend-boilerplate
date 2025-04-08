import os
import tempfile
from datetime import datetime

from fastapi import UploadFile
from google.cloud import storage

from app.core.config import settings

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = settings.GOOGLE_CLOUD_STORAGE_KEY
client = storage.Client()
bucket_name = settings.GOOGLE_CLOUD_STORATE_BUCKET


async def upload_file(file: UploadFile, folder: str = "uploads") -> str:
    """
    Upload a file to Google Cloud Storage

    Args:
        file (UploadFile): The file to upload
        folder (str): The folder in the bucket to upload to

    Returns:
        str: The public URL of the uploaded file
    """

    try:
        bucket = client.bucket(bucket_name)
        prefix = datetime.now().strftime("%Y%m%d_")

        destination_blob_name = f"{folder}/{prefix}{file.filename}"
        blob = bucket.blob(destination_blob_name)

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            content = await file.read()
            temp_file.write(content)
            temp_file.flush()

            blob.upload_from_filename(temp_file.name)

        os.unlink(temp_file.name)

        blob.make_public()
        return blob.public_url

    except Exception as e:
        raise Exception(f"Failed to upload file: {str(e)}") from e
