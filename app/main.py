from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router.ai_router import router as ai_router

app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(ai_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Welcome to Fast API Backend Boilerplate by @lutfiandri"}
