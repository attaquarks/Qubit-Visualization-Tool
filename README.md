# Qubit Visualization Tool

Qubit Visualization Tool is a small C++ and Python project for experimenting with quantum-state visualization. It provides a compact codebase for exploring how qubit states can be represented and visualized programmatically.

## What It Demonstrates

- Basic quantum-state representation.
- C++ implementation for low-level state logic.
- Python support script for visualization or experimentation.
- A minimal project structure suitable for learning and extending quantum computing concepts.

## Tech Stack

| Area | Tools |
|---|---|
| Core logic | C++ |
| Scripting / visualization | Python |
| Assets | `logo.ico` |

## Repository Structure

```text
main.cpp      C++ entry point
project.py    Python helper / visualization script
logo.ico      Application icon asset
```

## Getting Started

### Prerequisites

- A C++ compiler such as `g++`
- Python 3.8+

### Build the C++ Program

```bash
g++ main.cpp -o qubit-visualizer
```

Run it:

```bash
./qubit-visualizer
```

On Windows PowerShell:

```powershell
g++ main.cpp -o qubit-visualizer.exe
.\qubit-visualizer.exe
```

### Run the Python Script

```bash
python project.py
```

## Suggested Improvements

- Add screenshots or generated sample visualizations.
- Document the mathematical representation used for qubit states.
- Add command-line arguments for common states and gates.
- Add tests for state normalization and transformation logic.

## Project Status

This is an early educational/experimental repository. It is useful as a compact starting point for quantum visualization ideas and can be expanded into a richer interactive simulator.
