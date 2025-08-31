# Step1: Setup FastAPI backend
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from main import graph, SYSTEM_PROMPT, parse_response
app = FastAPI()


# CRITICAL: Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Step2: Receive and validate request from Frontend
class Query(BaseModel):
    message: str



@app.post("/ask")
async def ask(query: Query):
    inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", query.message)]}
    #inputs = {"messages": [("user", query.message)]}
    stream = graph.stream(inputs, stream_mode="updates")
    tool_called_name, final_response = parse_response(stream)

    # Step3: Send response to the frontend
    return {"response": final_response,
            "tool_called": tool_called_name}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)







