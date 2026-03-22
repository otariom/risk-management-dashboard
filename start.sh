#!/bin/bash

# Start FastAPI in background
uvicorn src.api.server:app --host 0.0.0.0 --port 8000 &

# Start Streamlit (this must be last)
streamlit run src/ui/app.py --server.port 10000 --server.address 0.0.0.0