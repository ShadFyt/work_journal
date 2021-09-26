import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get("/")
def index():
    return {
        "name": "Ryan"
    }

if __name__ == "__main__":
    uvicorn.run(app)