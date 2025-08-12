# Asyncio Basics

A comprehensive demonstration of asyncio patterns in Python, covering concurrency, synchronization, and advanced async programming techniques.

## Overview

This repository contains examples of:
- Sequential execution (no concurrency)
- Concurrent execution using tasks
- Concurrent execution using `asyncio.gather()`
- Concurrent execution using `asyncio.TaskGroup()` (Python 3.11+)
- Future objects for asynchronous results
- Synchronization primitives (locks and semaphores)

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

### 5. Future Objects
Demonstrates how to use futures for handling results that will be available at some point in the future, independent of task completion.

### 6. Synchronization

#### Locks
Shows how to use `asyncio.Lock()` to protect shared resources from concurrent modification, ensuring thread-safe operations.

#### Semaphores
Demonstrates `asyncio.Semaphore()` for controlling access to resources with limited capacity, allowing multiple coroutines to access a resource concurrently up to a specified limit.

#### Events
Uses `asyncio.Event()` for coordination between coroutines, allowing one coroutine to wait for a signal from another coroutine before continuing execution.

## Requirements

- Python 3.7+ (Python 3.11+ required for TaskGroup examples)