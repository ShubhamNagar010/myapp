from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Example marks data
marks_data = {
    'X': 10,
    'Y': 20,
    # Add more students here
}

class MarksRequest(BaseModel):
    names: List[str]

@app.get("/api")
async def get_marks(names: str = None):
    if names:
        names_list = names.split(',')
        marks = [marks_data.get(name) for name in names_list if name in marks_data]
        return {"marks": marks}
    else:
        return {"error": "No names provided"}

# To deploy this, ensure you have FastAPI and uvicorn installed:
# pip install fastapi uvicorn
