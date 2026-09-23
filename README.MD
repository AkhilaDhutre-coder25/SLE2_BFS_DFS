# SLE-2: BFS vs DFS Performance Analysis

## Project Overview

This repository contains the SLE-2 profiling work for **02AML204 – Introduction to Artificial Intelligence**. It compares **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** on the same 20-node graph.

The experiment measures:
- Execution time
- Average execution time
- Nodes expanded
- Performance using repeated searches
- Attempted profiling with py-spy

## Algorithms

### BFS

Breadth-First Search explores a graph level by level using a queue.

### DFS

Depth-First Search explores a path deeply before backtracking using a stack.

## Problem Setup

- Graph: 20 nodes
- Start node: `0`
- Goal node: `19`
- Repetitions: `50,000`
- Timing runs: `3`

The same problem conditions were used for both algorithms.

## Experimental Results

### BFS

| Metric | Result |
|---|---:|
| Run 1 | 141.0040 ms |
| Run 2 | 142.9329 ms |
| Run 3 | 124.8213 ms |
| **Average** | **136.2527 ms** |
| Nodes expanded | **20** |
| Repetitions | **50,000** |

### DFS

| Metric | Result |
|---|---:|
| Run 1 | 186.3295 ms |
| Run 2 | 223.1545 ms |
| Run 3 | 187.1891 ms |
| **Average** | **198.8910 ms** |
| Nodes expanded | **16** |
| Repetitions | **50,000** |

## Comparison

| Metric | BFS | DFS |
|---|---:|---:|
| Average time for 50,000 searches | 136.2527 ms | 198.8910 ms |
| Nodes expanded in one search | 20 | 16 |

For this particular graph, implementation, and recorded experiment, BFS had the lower measured total execution time, while DFS expanded fewer nodes before reaching the goal.

These values are experimental and can vary with the computer, Python version, implementation, and execution conditions.

## Running the Programs

```bash
python bfs.py