#!/bin/bash
PROJECT_DIR="/home/laurobeck/AzureSQl"
cd $PROJECT_DIR

echo "--- STARGATE CLUSTER: SESSION INITIALIZATION ---"

# 1. Activate Environment
source $PROJECT_DIR/stargate_venv/bin/activate

# 2. Execute C++ Core
if [ -f "./stargate_core" ]; then
    ./stargate_core
else
    echo "Error: stargate_core not found. Compile it first."
fi

# 3. Execute Python Visualizer
python3 Stargate_Execution_Core.py

echo "--- SESSION COMPLETE: Assets saved to $PROJECT_DIR ---"
