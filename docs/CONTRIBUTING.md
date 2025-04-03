# Contributing Guide

## Getting Started

### Prerequisites
- Python 3.8+
- Pygame 2.5+
- Git

### Setup
1. Fork the repository
2. Clone your fork
3. Create virtual environment
4. Install dependencies

## Development Workflow

### 1. Create an Issue
- Describe the feature/bug
- Add relevant labels
- Link related issues

### 2. Create a Branch
```bash
# For features
git checkout -b feature/your-feature-name

# For bugs
git checkout -b bugfix/bug-description
```

### 3. Follow TDD
1. Write failing test
2. Implement feature
3. Refactor code
4. Ensure all tests pass

### 4. Code Style
- Use Black formatter
- Follow PEP 8
- Add type hints
- Write docstrings

### 5. Commit Guidelines
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation
- test: Adding tests
- refactor: Code refactoring

### 6. Pull Request Process
1. Update documentation
2. Run all tests
3. Update CHANGELOG.md
4. Submit PR
5. Address review comments

## Testing

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=game

# Run specific tests
pytest tests/test_player.py
```

### Writing Tests
```python
def test_feature_behavior():
    # Arrange
    component = Component()
    
    # Act
    result = component.do_something()
    
    # Assert
    assert result == expected_value
```

## Documentation

### Code Documentation
```python
def complex_function(param1: int, param2: str) -> bool:
    """Short description of function.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: Description of when this occurs
    """
```

### Update Docs
1. Update relevant .md files
2. Add examples where helpful
3. Keep README.md current

## Review Process

### Reviewer Guidelines
- Check code style
- Verify test coverage
- Review documentation
- Test functionality

### Author Guidelines
- Respond to feedback
- Make requested changes
- Update tests as needed

## Release Process

### Version Numbers
- Follow semantic versioning
- Update version in code
- Tag releases

### Changelog
- Add all changes
- Group by type
- Credit contributors

## Community

### Communication
- Use issue tracker
- Be respectful
- Follow code of conduct

### Recognition
- Credit contributors
- Maintain AUTHORS.md
- Thank reviewers

## Resources

### Documentation
- Python docs
- Pygame docs
- Project wiki

### Tools
- Black formatter
- Pytest
- Coverage.py

## Questions?

Open an issue or contact maintainers.
