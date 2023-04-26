from fastapi import FastAPI

app = FastAPI()

@app.get("/symetric/key")
async def root():
    return

@app.post("/symetric/key")
async def say_hello(name: str):
    return

@app.post("/symetric/encode")
async def root():
    return

@app.post("/symetric/decode")
async def say_hello(name: str):
    return

@app.get("/symetric/key")
async def root():
    return

@app.post("/symetric/key")
async def say_hello(name: str):
    return

############## ASYMETRIC #########################

@app.get("/asymetric/key")
async def say_hello(name: str):
    return

@app.get("/asymetric/key/ssh")
async def root():
    return

@app.post("/asymetric/key")
async def say_hello(name: str):
    return

@app.get("/asymetric/verify")
async def root():
    return

@app.post("/asymetric/sign")
async def say_hello(name: str):
    return

@app.get("/asymetric/encode")
async def root():
    return

@app.post("/asymetric/decode")
async def say_hello(name: str):
    return 