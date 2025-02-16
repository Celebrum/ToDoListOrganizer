# Developer Guide

## Setting Up the Development Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Celebrum/ToDoListOrganizer.git
   cd ToDoListOrganizer
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Code Style and Conventions

- Follow the PEP 8 style guide for Python code.
- Use meaningful variable and function names.
- Write docstrings for all functions and classes.
- Keep functions small and focused on a single task.
- Use comments to explain complex logic and important decisions.

## Adding New Features

1. **Create a new branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Implement the feature**:
   - Add new files or modify existing files as needed.
   - Write unit tests for the new feature.

3. **Run tests**:
   ```bash
   python -m unittest discover
   ```

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add your feature description"
   ```

5. **Push your changes**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a pull request**:
   - Go to the GitHub repository.
   - Create a pull request to merge your changes into the main branch.

## Writing and Running Tests

1. **Write unit tests**:
   - Create test files in the `tests` directory.
   - Use the `unittest` framework to write test cases.

2. **Run tests**:
   ```bash
   python -m unittest discover
   ```

3. **Check test coverage**:
   - Use a tool like `coverage.py` to check test coverage.
   - Ensure that all new code is covered by tests.

4. **Fix any failing tests**:
   - If any tests fail, fix the issues and run the tests again.

## Note on FfeD Algorithm

Please protect the FfeD algorithm but share as much knowledge on the phi framework. The rest is all free to be shared, but because of the FfeD framework, it cannot be used for selling this tool. It is free to use, install, and share, but no profit can be made without my consent. Free open source can use this tool to build other tools but cannot include the code part with the FfeD algorithm I developed. Anyone who wants to use the algorithm needs to contact and communicate with neural_network@brain.scrde.ca. Otherwise, everything else is free to use or sell, including the mathematics in the phi framework.
