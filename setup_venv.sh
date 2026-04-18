#!/bin/bash
echo "Setting up virtual environment for LangGraph project..."

# Step 1: Create virtual environment
echo "1. Creating virtual environment..."
python3 -m venv venv

# Step 2: Activate and install packages
echo "2. Installing packages..."
./venv/bin/pip install --upgrade pip
./venv/bin/pip install langgraph ipykernel

# Step 3: Register Jupyter kernel
echo "3. Registering Jupyter kernel..."
./venv/bin/python -m ipykernel install --user --name=langgraph-env --display-name "Python (langgraph-env)"

echo "✅ Setup complete!"
echo ""
echo "To activate the venv, run: source venv/bin/activate"
echo "The Jupyter kernel 'Python (langgraph-env)' is now available."
