# Asyncio Basics

A simple demonstration of different asyncio patterns in Python, showing how to implement concurrent programming with various approaches.

## Overview

This repository contains examples of:
- Sequential execution (no concurrency)
- Concurrent execution using tasks
- Concurrent execution using `asyncio.gather()`
- Concurrent execution using `asyncio.TaskGroup()` (Python 3.11+)

## Running the Examples

```bash
python basic-asyncio.py
```

## Patterns Demonstrated

### 1. Sequential Execution
Shows how coroutines execute one after another when not properly scheduled for concurrency.

### 2. Task-based Concurrency
Uses `asyncio.create_task()` to run coroutines concurrently, allowing for better control over individual tasks.

### 3. Gather Pattern
Uses `asyncio.gather()` to run multiple coroutines concurrently and collect results, though error handling can be challenging.

### 4. Task Group Pattern
Uses `asyncio.TaskGroup()` (available in Python 3.11+) for better error handling and resource management in concurrent operations.

## Requirements

- Python 3.7+ (Python 3.11+ required for TaskGroup examples)