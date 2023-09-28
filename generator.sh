#!/bin/bash

# Set the path to your Python interpreter (modify this as needed)
PYTHON_INTERPRETER="C:\Users\Admin\.conda\envs\CGCAT01\python.exe"

# Set the path to your Python script (modify this as needed)
SCRIPT_PATH="process_jsonl.py"

# Set the paths to the input and output folders (modify these as needed)
INPUT_FOLDER="data\en-US.jsonl"
OUTPUT_FOLDER="output"

# Run the Python script with flags
$PYTHON_INTERPRETER $SCRIPT_PATH --input-folder $INPUT_FOLDER --output-folder $OUTPUT_FOLDER
