from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root(name: str = "hello docker"):
    """Root endpoint. Optional query param `name` (default: PyCharm)."""
    return {"message": f"Hi, {name}"}


if __name__ == "__main__":
    # Allow running `python main.py` for quick local testing.
    uvicorn.run("main:app", host="0.0.0.0", port=8000)