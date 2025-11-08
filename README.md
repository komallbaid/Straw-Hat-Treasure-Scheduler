# Treasure Quest: The Straw Hat Crew Scheduler

A Python-based scheduling engine that models how the Straw Hat crew processes incoming treasures using:
- **Custom binary heaps**
- **Priority-based task scheduling**
- **Dynamic load balancing across crewmates**
- **Accurate completion-time simulation**

This project implements a full event-driven scheduling system where each incoming treasure is assigned to the least-loaded crewmate, and processed according to a strict priority rule defined by `(arrival_time + remaining_size)`. Remaining tasks are completed using a heap-driven simulation ensuring correct ordering and finish times.

---

## 🚀 Features

- **Custom Heap Implementation**
  - Supports insert, extract, top, and bottom-up initialization
  - Configurable comparator for max/min or custom priority

- **Crewmate Workload Balancing**
  - Real-time load projection  
  - Extracts the *least-loaded crewmate* at each treasure arrival

- **Treasure Processing Engine**
  - Priority based on minimizing `(arrival + remaining)`
  - Supports partial processing during time gaps
  - Maintains completion times for all treasures

- **Accurate Simulation via Event Handling**
  - Handles simultaneous arrivals
  - Finish-phase simulation using fresh heap copies
  - Ensures correct global ordering of completion times

---

## 📂 Project Structure
```
Straw Hat Treasure Scheduler/
│
├── crewmate.py
├── heap.py
├── straw_hat.py
├── treasure.py
├── main.py
│
├── tc_heap1.txt
├── tc_treasury1.txt
├── tc_treasury2.txt
│
├── .gitignore
└── README.md
```

---

## 🧠 Scheduling Logic Summary

### ✅ **Crewmate Selection Rule**
At each arrival time:
- Compute each crewmate’s **current load**  
- Assign the treasure to the **least-loaded crewmate**  
- Tie-break: lowest crew ID

### ✅ **Treasure Priority (Within Each Crewmate)**
A treasure’s priority is determined by:

`priority = minimize(arrival_time + remaining_size)`


This corresponds to maximizing the scheduling rule:

`(wait_time - remaining_size)`


### ✅ **Completion-Time Computation**
After all arrivals:
1. Already-finished treasures are collected.
2. Remaining treasures are simulated using a **temporary heap**.
3. Completion times are assigned in correct priority sequence.
4. Final output is sorted by treasure ID.

---

## ✅ Example Output

For sample tests:

Completion Time: [(1, 6), (2, 5), (3, 6)]


---

## 🛠️ How to Run

python main.py


Make sure your test files (tc_heap1.txt, tc_treasury1.txt, tc_treasury2.txt) are in the same directory.

