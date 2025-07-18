#!/bin/bash
# Setup and run the meta_agent web chat with Gunicorn
set -e

# 1. Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# 2. Activate virtual environment and install requirements
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
if [ -f "meta_agent/requirements.txt" ]; then
  pip install -r meta_agent/requirements.txt
fi

# 3. Run Gunicorn for meta_agent.web_chat:app on port 5002
exec .venv/bin/gunicorn --workers 3 --bind 0.0.0.0:5002 meta_agent.web_chat:app
