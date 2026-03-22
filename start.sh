#!/bin/bash

# 🔥 IMPORTANT FIX
export PYTHONPATH=/opt/render/project/src

# Start FastAPI
uvicorn src.api.server:app --host 0.0.0.0 --port 8000 &

# Start Streamlit
streamlit run src/ui/app.py --server.port $PORT --server.address 0.0.0.0