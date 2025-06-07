#!/bin/bash

# Exit if any command fails
set -e

# Install required Python packages
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi
source .venv/bin/activate
pip install -r requirements.txt


# Optionally check if the CLI is available
if ! command -v weasyprint &> /dev/null; then
    echo "WeasyPrint not found. Installing with Homebrew..."
    brew install weasyprint
fi
export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib:$DYLD_FALLBACK_LIBRARY_PATH

# Run Python scripts in a specific order
python3 scripts/csv_to_json.py
python3 scripts/append_order_url.py
python3 scripts/generate_passes.py

echo "All Python scripts completed."

echo "**************************************************************************"
echo "Starting the server: http://localhost:8000/docs/search.html"
echo "**************************************************************************"
python3 -m http.server 8000