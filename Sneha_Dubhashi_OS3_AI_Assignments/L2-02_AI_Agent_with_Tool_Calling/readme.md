# AI Agent with Tool Calling

## Project Overview

This project implements a simple AI Agent capable of selecting and invoking different tools based on the user's intent. The agent analyzes the user's query, determines the appropriate tool, executes it, and returns the result. It also handles invalid inputs and tool failures gracefully.

---

## Features

- Intent-based tool selection
- Calculator tool for mathematical expressions
- File Lookup tool for reading text files
- Graceful error handling
- Simple and modular Python implementation

---

## Project Structure

```
AI-Agent-With-Tool-Calling/
│
├── agent.py          # Main AI Agent implementation
├── sample.txt        # Sample text file for testing
├── README.md         # Project documentation
```

---

## Requirements

- Python 3.8 or above

No external libraries are required.

---

## Tools Implemented

### 1. Calculator Tool

Performs arithmetic calculations.

Supported operations:

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

Example:

Input:

```
calculate 20 + 30
```

Output:

```
Result: 50
```

---

### 2. File Lookup Tool

Reads the contents of a text file.

Example:

Input:

```
read sample.txt
```

Output:

```
This is a sample file.
```

If the file does not exist:

```
File Error: File not found.
```

---

## How the Agent Works

1. Accepts a user query.
2. Analyzes the query.
3. Selects the appropriate tool.
4. Extracts the required input.
5. Executes the selected tool.
6. Returns the output or an error message.

---

## Tool Selection Logic

| User Query | Tool Selected |
|------------|--------------|
| calculate 10+5 | Calculator |
| 25*6 | Calculator |
| read sample.txt | File Lookup |
| open file.txt | File Lookup |
| hello | No Tool |

---

## Error Handling

### Calculator Errors

Example:

```
calculate 10/
```

Output:

```
Calculator Error: invalid syntax
```

### File Errors

Example:

```
read test.txt
```

Output:

```
File Error: File not found.
```

### Unknown Queries

Example:

```
Hello
```

Output:

```
I cannot determine the correct tool to use.
```

---

## Sample Executions

### Example 1

Input:

```
calculate 12*8
```

Output:

```
[Tool Used: calculator]

Result: 96
```

---

### Example 2

Input:

```
read sample.txt
```

Output:

```
[Tool Used: file_lookup]

This is a sample file.
```

---

### Example 3

Input:

```
read abc.txt
```

Output:

```
[Tool Used: file_lookup]

File Error: File not found.
```

---

### Example 4

Input:

```
calculate 20/
```

Output:

```
[Tool Used: calculator]

Calculator Error: invalid syntax
```

---

### Example 5

Input:

```
Hello Agent
```

Output:

```
I cannot determine the correct tool to use.
```

---

## Running the Project

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd AI-Agent-With-Tool-Calling
```

Run the program:

```bash
python agent.py
```

Enter a query when prompted.

Example:

```
Enter your Query: calculate 50+25
```

Output:

```
[Tool Used: calculator]

Result: 75
```

---

## Future Improvements

- Replace `eval()` with a safer expression parser.
- Use NLP or an LLM for better intent detection.
- Support more tools such as:
  - Weather API
  - Web Search
  - Current Date & Time
- Improve filename parsing for complex file names.

---

## Author

**Sneha Shrinivas Dubhashi**

---