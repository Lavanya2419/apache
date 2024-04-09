from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    # Your login logic here
    if username == "admin" and password == "password":
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid username or password"}
