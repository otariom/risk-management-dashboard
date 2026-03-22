#!/bin/bash

# Start FastAPI in background
uvicorn src.api.server:app --host 0.0.0.0 --port 8000 &

# Start Streamlit on Render port
streamlit run src/ui/app.py --server.port $PORT --server.address 0.0.0.0