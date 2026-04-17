# Lang Graph Code.

A collection of Jupyter notebooks and Python code examples.

## 🚀 Getting Started

### Prerequisites
- [Anaconda](https://www.anaconda.com/download) installed on your system

### How to Run the Code

#### Option 1: Using Jupyter Notebook (Recommended)

1. **Open Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

2. **Navigate** to the notebook file you want to run (e.g., `Hello_world.ipynb`)

3. **Select a Python Kernel:**
   - Click on a cell to run
   - If prompted to choose a kernel, select **"Python Environments..."**
   - Choose `base (Python 3.13.9) ~/anaconda3/bin/python` (your Anaconda environment)
   - Wait for the kernel to initialize (you'll see a green indicator when ready)

4. **Run Cells:**
   - Click on the cell you want to execute
   - Press `Shift + Enter` or click the ▶️ Run button
   - The output will appear below the cell

#### Option 2: Using JupyterLab

```bash
jupyter lab
```

Then open and run notebooks with `Shift + Enter`.

## 📁 Project Structure

```
lang-graph-code/
├── Hello_world.ipynb     # Your first notebook
├── README.md             # This file
└── ...                   # More notebooks coming soon
```

## 🛠️ Available Python Environments

When running notebooks, you can choose from:
- `base (Python 3.13.9)` - Anaconda's default environment (recommended)
- `Python 3.12.3` - System Python installations
- `Python 3.14.3` - Additional system Python

## 💡 Tips

- **Kernel Status:** Look for the kernel indicator in the top right (🟢 = ready, 🟡 = busy, ⚪ = not connected)
- **Running All Cells:** Use "Run All" from the menu to execute the entire notebook
- **Creating New Environments:** Use `conda create -n myenv python=3.12` to create custom environments

## 📚 Current Notebooks

- **Hello_world.ipynb** - A simple "Hello World" example to get started

## 🔧 Troubleshooting

**Problem:** No Python environments appear in the kernel selection
**Solution:** Install the IPython kernel:
```bash
pip install ipykernel
python -m ipykernel install --user --name=python3
```

**Problem:** Kernel won't connect
**Solution:** Restart Jupyter Notebook and try selecting the kernel again

---

Happy coding! 🎉
