from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route that responds to GET requests at the root URL ("/")
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

