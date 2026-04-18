# LangGraph Code Collection

A collection of Jupyter notebooks demonstrating LangGraph concepts and implementations.

## 🚀 Getting Started

### Prerequisites
- Python 3.14+ installed on your system
- Jupyter Notebook or VS Code with Jupyter extension

### Quick Setup (Recommended)

#### Step 1: Create Virtual Environment

```bash
# Navigate to project directory
cd path/to/lang-graph-code

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Step 2: Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# Or install manually:
pip install langgraph ipykernel
```

#### Step 3: Register Jupyter Kernel

```bash
# Register the virtual environment as a Jupyter kernel
./venv/bin/python -m ipykernel install --user --name=langgraph-env --display-name "Python (langgraph-env)"
```

### How to Run the Code

#### Option 1: Using VS Code (Recommended)

1. **Open VS Code**
2. **Open the project folder**
3. **Open any notebook** (e.g., `01_Hello_world_agent.ipynb`)
4. **Select the kernel:**
   - Click on the kernel selector in the top-right corner
   - Choose **"Python (langgraph-env)"**
5. **Run cells:** Press `Shift + Enter` to execute each cell

#### Option 2: Using Jupyter Notebook

```bash
# Make sure to activate the venv first
source venv/bin/activate

# Launch Jupyter
jupyter notebook
```

Then navigate to and open any notebook file.

## 📁 Project Structure

```
lang-graph-code/
├── venv/                      # Virtual environment (auto-created)
├── 00_Hello_world.ipynb       # Basic hello world example
├── 01_Hello_world_agent.ipynb # Hello world with agent
├── 02_Multiple_Inputs.ipynb   # Handling multiple inputs
├── 03_Sequential_agent.ipynb  # Sequential agent workflow
├── 04_conditional_agent.ipynb # Conditional branching
├── 05_looping_agent.ipynb     # Looping agents
├── 05_looping_graph.png       # Looping graph diagram
├── requirements.txt           # Python dependencies
├── setup_venv.sh             # Automated setup script
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## 📚 Available Notebooks

- **00_Hello_world.ipynb** - Basic hello world example
- **01_Hello_world_agent.ipynb** - Hello world with LangGraph agent
- **02_Multiple_Inputs.ipynb** - Working with multiple input parameters
- **03_Sequential_agent.ipynb** - Building sequential agent workflows
- **04_conditional_agent.ipynb** - Implementing conditional logic and routing
- **05_looping_agent.ipynb** - Creating loops and iterative processes

## 🔧 Troubleshooting

### Problem: ModuleNotFoundError: No module named 'langgraph'

**Solution:** Make sure you've selected the correct kernel:
1. Click the kernel selector (top-right in VS Code)
2. Choose **"Python (langgraph-env)"**
3. Restart the kernel if needed

### Problem: Kernel not connecting

**Solution:** 
```bash
# Recreate the kernel
./venv/bin/python -m ipykernel install --user --name=langgraph-env --display-name "Python (langgraph-env)" --force
```

### Problem: Virtual environment issues

**Solution:** Start fresh:
```bash
# Remove old venv
rm -rf venv

# Recreate from scratch
./setup_venv.sh
```

## 💡 Tips

- **Always activate the venv** before running Python scripts directly
- **Kernel Status:** Look for the kernel indicator (🟢 = ready, 🟡 = busy)
- **Import Issues:** If imports fail, check you're using the "langgraph-env" kernel
- **Dependencies:** Add new packages to `requirements.txt` for consistency

## 🛠️ Advanced Setup

### Automated Setup

Run the provided setup script:
```bash
chmod +x setup_venv.sh
./setup_venv.sh
```

This will automatically:
1. Create the virtual environment
2. Install all dependencies
3. Register the Jupyter kernel

### Manual Setup

If you prefer manual setup:
```bash
# 1. Create venv
python3 -m venv venv

# 2. Activate and install
source venv/bin/activate
pip install langgraph ipykernel

# 3. Register kernel
python -m ipykernel install --user --name=langgraph-env --display-name "Python (langgraph-env)"
```

---

Happy coding with LangGraph! 🎉
