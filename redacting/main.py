from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def redact_image():
	return {"message": "Attach an image"}
