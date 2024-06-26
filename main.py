from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('Hashing API')

from fastapi import FastAPI
from hashes.sha256 import create_hash

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:9001", "http://127.0.0.1:9001", "http://localhost:9000", "http://127.0.0.1:9000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HashRequest(BaseModel):
    text: str


@app.get("/")
async def root():
    return {"message": "Backend is running"}


@app.post("/api/hashes/sha256")
async def get_sha256(request: HashRequest):
    hash_result = create_hash(request.text)
    return {"text": request.text, "hash": hash_result}
