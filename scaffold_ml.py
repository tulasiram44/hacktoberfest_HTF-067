import os

base_dir = r"C:\Users\Neha\OneDrive\Desktop\SIH\SIH WINNERS\ml-service"
os.makedirs(os.path.join(base_dir, "app"), exist_ok=True)

files = {
    "requirements.txt": """fastapi==0.103.1
uvicorn==0.23.2
scikit-learn==1.3.0
pandas==2.1.0
numpy==1.25.2
""",
    "Dockerfile": """FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
""",
    "app/main.py": """from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(title="SAHAYA ML Service", description="AI Demand Forecasting and Allocation API")

class ForecastRequest(BaseModel):
    zone: str
    date: str

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "ML Service is running"}

@app.post("/forecast")
def predict_demand(req: ForecastRequest):
    # Simulated ML Model Output for SIH Prototype
    services = ["Plumbing", "Electrical", "Cleaning", "Carpentry"]
    predictions = []
    
    for service in services:
        demand = random.choice(["Low", "Medium", "High"])
        workers_needed = random.randint(1, 5) if demand == "High" else 0
        
        predictions.append({
            "service": service,
            "demand": demand,
            "recommended_allocation": workers_needed
        })
        
    return {
        "zone": req.zone,
        "date": req.date,
        "forecast": predictions
    }
"""
}

for path, content in files.items():
    with open(os.path.join(base_dir, path), "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

print("ML Service scaffolded.")
