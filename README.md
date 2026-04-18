# LangGraph Code Collection

A comprehensive collection of Jupyter notebooks demonstrating LangGraph concepts, patterns, and implementations from basic to advanced workflows.

## 📖 About LangGraph

[LangGraph](https://github.com/langchain-ai/langgraph) is a library for building stateful, multi-actor applications with LLMs, built on top of LangChain. It excels at creating:
- **Stateful agents** that maintain context across interactions
- **Multi-agent workflows** with complex coordination patterns
- **Conditional routing** based on dynamic decisions
- **Cyclic and looping processes** for iterative tasks

This collection provides hands-on examples to master these concepts progressively.

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

### Beginner Level

- **00_Hello_world.ipynb** - *Getting Started*
  - Simple hello world example to familiarize with Jupyter notebooks
  - No LangGraph concepts yet - just basic Python setup

- **01_Hello_world_agent.ipynb** - *Your First LangGraph Agent*
  - Introduction to basic LangGraph concepts
  - Creating a simple state and agent
  - Understanding nodes, edges, and graph compilation
  - Basic state management and transformations

### Intermediate Level

- **02_Multiple_Inputs.ipynb** - *Working with Complex State*
  - Handling multiple input parameters in agent state
  - Complex state structures with TypedDict
  - Managing data flow through multiple fields
  - Practical example with user information

- **03_Sequential_agent.ipynb** - *Sequential Workflows*
  - Building sequential agent workflows
  - Chaining multiple nodes in sequence
  - Understanding state evolution through pipeline
  - Real-world example: greeting + message composition

### Advanced Level

- **04_conditional_agent.ipynb** - *Conditional Routing*
  - Implementing conditional logic and routing
  - Dynamic decision-making with conditional edges
  - Router nodes that direct flow based on state
  - Mathematical operations example (addition vs subtraction)

- **05_looping_agent.ipynb** - *Looping and Iteration*
  - Creating loops and iterative processes
  - Self-referential edges for node looping
  - Counter-based termination conditions
  - Practical example: generating multiple random numbers

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

### Problem: Graph visualization not working

**Solution:** Make sure you have the required dependencies:
```bash
pip install ipython graphviz
```

### Problem: State not updating correctly

**Solution:** Remember to return the modified state:
```python
# ❌ Wrong - modifies state in place
def my_node(state: AgentState) -> AgentState:
    state["value"] = "new value"
    # Don't forget to return!

# ✅ Correct - returns modified state
def my_node(state: AgentState) -> AgentState:
    state["value"] = "new value"
    return state  # Always return the state
```

## 🎨 Common LangGraph Patterns

### Sequential Pattern
```python
graph.add_edge(START, "node1")
graph.add_edge("node1", "node2")
graph.add_edge("node2", END)
```

### Conditional Routing Pattern
```python
graph.add_conditional_edges(
    "router_node",
    routing_function,
    {
        "option_a": "node_a",
        "option_b": "node_b",
        "default": END
    }
)
```

### Looping Pattern
```python
graph.add_conditional_edges(
    "processing_node",
    should_continue_function,
    {
        "continue": "processing_node",  # Self-loop
        "done": END
    }
)
```

## 🎯 Learning Path

**Recommended progression for beginners:**

1. **Start with** `00_Hello_world.ipynb` → Get comfortable with Jupyter
2. **Move to** `01_Hello_world_agent.ipynb` → Understand basic LangGraph concepts
3. **Practice with** `02_Multiple_Inputs.ipynb` → Learn complex state management
4. **Build workflows** in `03_Sequential_agent.ipynb` → Master sequential processing
5. **Add decision logic** with `04_conditional_agent.ipynb` → Implement routing
6. **Create loops** in `05_looping_agent.ipynb` → Handle iterative processes

**Key Concepts You'll Master:**
- ✅ State management with TypedDict
- ✅ Node creation and function definition
- ✅ Edge configuration (normal, conditional, entry/exit)
- ✅ Graph compilation and execution
- ✅ Conditional routing and decision trees
- ✅ Looping patterns and iterative workflows
- ✅ Graph visualization with Mermaid diagrams

## 💡 Tips

- **Always activate the venv** before running Python scripts directly
- **Kernel Status:** Look for the kernel indicator (🟢 = ready, 🟡 = busy)
- **Import Issues:** If imports fail, check you're using the "langgraph-env" kernel
- **Dependencies:** Add new packages to `requirements.txt` for consistency
- **Graph Visualization:** Use `app.get_graph().draw_mermaid_png()` to visualize your workflows
- **Debugging:** Print state at each node to understand data flow
- **State Immutability:** Remember that state should be updated by returning modified copies, not in-place mutations

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

## 📖 Additional Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangGraph GitHub Repository](https://github.com/langchain-ai/langgraph)
- [LangChain Documentation](https://python.langchain.com/)
- [State Management Best Practices](https://langchain-ai.github.io/langgraph/concepts/low_level/#state)

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements or additional notebook examples.

## 📄 License

This project is licensed under the terms specified in the LICENSE file.

---

**Happy coding with LangGraph!** 🎉

*Last updated: 2025-04-17*
