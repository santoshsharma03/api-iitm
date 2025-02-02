# main.py
from fastapi import FastAPI
from typing import List, Dict
import json

app = FastAPI()

# Load the student marks from the provided JSON file
with open("q-vercel-python.json") as f:
    students_data = json.load(f)

# Convert the list of dictionaries into a dictionary with student names as keys
students_marks = {student['name']: student['marks'] for student in students_data}

@app.get("/api")
def get_marks(names: List[str]) -> Dict[str, int]:
    result = {}
    for name in names:
        if name in students_marks:
            result[name] = students_marks[name]
        else:
            result[name] = None  # If the student doesn't exist in the records
    return result
