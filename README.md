# In-Memory Key-Value Database with Transactions

## Overview
This project implements an in-memory key-value database that supports basic transaction functionality. The database allows operations like `put`, `get`, `begin_transaction`, `commit`, and `rollback`.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher must be installed. To verify:
  ```bash
  python --version
  ```

### Installation
1. Clone the repository or download the `in_memory_db.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the `in_memory_db.py` file.

### Running the Script
1. Execute the script using the following command:
   ```bash
   python in_memory_db.py
   ```
2. See the output, which includes test cases verifying the database's functionality.

Expected values:
``` 
None
No active transaction. Please start a transaction first.
5
6
No active transaction to commit.
No active transaction to rollback.
None
None
```

## Assignment Suggestions
To make this assignment an official task, the instructions could clarify how edge cases (ex operations on non-existent keys) should be handled. Also adding features like delete(key) and nested transactions could increase complexity/real-world applicability. Providing example outputs for all scenarios and automated testing scripts could also help with consistency and make grading easier. And a grading rubric that covers code structure, documentation, and test coverage could also improve the grading process and help students understand the expectations better.

## Resources
- [Database Transactions Guide](https://www.dbvis.com/thetable/database-transactions-101-the-essential-guide/)
- [Python Dictionary Documentation](https://www.geeksforgeeks.org/python-dictionary/)
