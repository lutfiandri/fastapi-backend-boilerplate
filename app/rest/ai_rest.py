from pydantic import BaseModel


class AISummaryResponse(BaseModel):
    laba_rugi: str
