from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router.user_router import router as user_router

app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Welcome to Fast API Backend Boilerplate by @lutfiandri"}
