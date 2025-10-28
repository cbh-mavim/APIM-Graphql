# Azure GraphQL Platform Processor

A GraphQL server for processing Azure platform data.

## Installation

### Quick Install

The easiest way to install is using the provided installation script:

```bash
# Clone the repository
git clone https://github.com/yourusername/azure-graphql-platform-processor.git
cd azure-graphql-platform-processor

# Run the installation script
python install.py
```

This script will install the package in development mode and verify the installation.

### Manual Install

You can also install the package manually:

```bash
# Clone the repository
git clone https://github.com/yourusername/azure-graphql-platform-processor.git
cd azure-graphql-platform-processor

# Install the package
pip install -e .

# Verify the installation
python verify_installation.py
```

### Install as a Dependency

To use this package as a dependency in another project, add it to your project's requirements:

```bash
pip install git+https://github.com/yourusername/azure-graphql-platform-processor.git
```

Or add to your requirements.txt:

```
git+https://github.com/yourusername/azure-graphql-platform-processor.git
```

## Usage

### Running the Server

After installation, you can run the GraphQL server using the command-line entry point:

```bash
azure-graphql-server
```

This will start the server at http://127.0.0.1:8000/graphql.

### Importing in Your Code

You can import and use the module in your Python code:

```python
# Import the schema
from gql import schema
from strawberry.asgi import GraphQL
import uvicorn

# Create a GraphQL application
app = GraphQL(schema)

# Run the server with custom settings
if __name__ == "__main__":
    uvicorn.run(
        "your_module:app",
        host="127.0.0.1",
        port=8080,
        reload=True
    )
```

See `example_usage.py` for a complete example.

## Project Structure

- `gql/`: Main package containing GraphQL implementation
  - `schemas/`: GraphQL schema definitions
  - `types/`: GraphQL type definitions
  - `resolvers/`: GraphQL resolvers
  - `config/`: Configuration files
  - `utils/`: Utility functions

## Development

### Requirements

- Python 3.12 or higher
- Dependencies listed in pyproject.toml

### Setup Development Environment

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

### Verifying Installation

After installation, you can verify that the package is installed correctly by running:

```bash
python verify_installation.py
```

This script will check that all components can be imported correctly.

### Running Tests

```bash
# Run all tests
pytest

# Run specific tests
pytest tests/test_schema.py
```

## License

MIT
