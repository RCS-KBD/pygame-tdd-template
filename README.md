# Pygame TDD Template

A comprehensive template for Pygame projects using Test-Driven Development (TDD) methodology.

## Features

- 🎮 Clean project structure with separation of concerns
- ✅ Pytest integration with fixtures and mocks
- 🔄 TDD workflow setup
- 🎨 Asset management system
- ⚙️ Configuration management
- 📁 Organized directory structure

## Project Structure

```
pygame-tdd-template/
├── run_game.py            # Entry point script
├── requirements.txt       # Python dependencies
├── pytest.ini            # Pytest configuration
├── .gitignore            # Git ignore file
├── game/                 # Main game package
│   ├── __init__.py
│   ├── main.py          # Game initialization and loop
│   ├── settings.py      # Game settings and constants
│   ├── assets/         # Asset management
│   │   ├── __init__.py
│   │   ├── images/
│   │   └── sounds/
│   ├── components/     # Game components
│   │   ├── __init__.py
│   │   ├── player.py
│   │   └── enemy.py
│   ├── scenes/        # Game scenes/states
│   │   ├── __init__.py
│   │   ├── menu.py
│   │   └── gameplay.py
│   └── utils/         # Utility functions
│       ├── __init__.py
│       └── helpers.py
└── tests/             # Test suite
    ├── __init__.py
    ├── conftest.py    # Pytest fixtures
    ├── test_player.py
    └── test_game.py
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/RCS-KBD/pygame-tdd-template.git
cd pygame-tdd-template
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the tests:
```bash
pytest
```

5. Run the game:
```bash
python run_game.py
```

## Test-Driven Development Workflow

1. Write a failing test for the feature you want to implement
2. Run the test to see it fail (Red phase)
3. Write the minimum code to make the test pass (Green phase)
4. Refactor the code while keeping tests green (Refactor phase)
5. Repeat for new features or improvements

## Best Practices

### Code Organization
- Keep game logic separate from rendering code
- Use classes to encapsulate related functionality
- Follow single responsibility principle
- Keep methods and functions focused and testable

### Testing
- Write tests before implementing features
- Use fixtures for common setup
- Mock external dependencies
- Test edge cases and error conditions
- Keep tests focused and descriptive

### Asset Management
- Store assets in appropriate subdirectories
- Use relative paths for asset loading
- Consider using asset loader utilities
- Handle missing assets gracefully

## Contributing

1. Fork the repository
2. Create a feature branch
3. Write tests for your changes
4. Implement your changes
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.