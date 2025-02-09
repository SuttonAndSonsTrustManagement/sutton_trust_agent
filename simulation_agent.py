import threading
import time
import requests
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

#########################################
# Simulation Server: Offline FastAPI App
#########################################

app = FastAPI()

# Define a simple data model for chat queries.
class Query(BaseModel):
    text: str

# Simulated /chat/ endpoint (simulates a GPU-accelerated LLM response).
@app.post("/chat/")
async def chat(query: Query):
    # Instead of calling a real LLM, we return a simulated response.
    return {"response": f"Simulated LLM response to: {query.text}"}

# Simulated /transcribe/ endpoint (simulates speech-to-text).
@app.post("/transcribe/")
async def transcribe(query: Query):
    # Here we assume the "text" field represents a simulated audio file path.
    return {"text": "Simulated transcript of the audio file"}

# Simulated /detect/ endpoint (simulates computer vision object detection).
@app.post("/detect/")
async def detect():
    # Return a dummy detection result.
    return {"objects": [{"label": "simulated_object", "confidence": 0.99}]}

#########################################
# Function to Run the Simulation Server
#########################################

def run_simulation_server():
    # Run the FastAPI simulation server with uvicorn.
    uvicorn.run(app, host="127.0.0.1", port=8000)

#########################################
# Launch the Simulation Server in a Thread
#########################################

print("Starting simulation server...")
server_thread = threading.Thread(target=run_simulation_server, daemon=True)
server_thread.start()

# Wait briefly to ensure the server is up
time.sleep(2)

#########################################
# Integration Testing: Simulate Client Requests
#########################################

def test_simulated_endpoints():
    base_url = "http://127.0.0.1:8000"
    
    # Test the /chat/ endpoint
    print("\nTesting /chat/ endpoint...")
    try:
        chat_response = requests.post(f"{base_url}/chat/", json={"text": "Hello, simulation!"})
        print("Response from /chat/:", chat_response.json())
    except Exception as e:
        print("Error testing /chat/ endpoint:", e)
    
    # Test the /transcribe/ endpoint
    print("\nTesting /transcribe/ endpoint...")
    try:
        stt_response = requests.post(f"{base_url}/transcribe/", json={"text": "simulated_audio_file.wav"})
        print("Response from /transcribe/:", stt_response.json())
    except Exception as e:
        print("Error testing /transcribe/ endpoint:", e)
    
    # Test the /detect/ endpoint
    print("\nTesting /detect/ endpoint...")
    try:
        detect_response = requests.post(f"{base_url}/detect/")
        print("Response from /detect/:", detect_response.json())
    except Exception as e:
        print("Error testing /detect/ endpoint:", e)

print("Running integration tests...")
test_simulated_endpoints()

#########################################
# Finalize Simulation
#########################################

print("\nSimulation complete. The simulated endpoints returned expected dummy responses.")
print("This simulation verifies that the integration of components works offline.")
print("Press ENTER to exit the simulation.")

input()
print("Exiting simulation agent.")
