# Testing Guide

## Overview
This guide explains the testing approach used in this Pygame project, focusing on Test-Driven Development (TDD) practices.

## Test Structure

### Directory Layout
```
tests/
├── __init__.py
├── conftest.py        # Shared fixtures
├── test_game.py       # Core game tests
└── test_components/   # Component-specific tests
```

## Writing Tests

### TDD Workflow
1. **Red Phase**
   - Write a failing test that defines the desired behavior
   - Run tests to confirm failure
   ```python
   def test_player_movement():
       player = Player(x=0, y=0)
       player.move_right()
       assert player.x == player.speed  # Should fail initially
   ```

2. **Green Phase**
   - Implement minimal code to make the test pass
   - Run tests to confirm success

3. **Refactor Phase**
   - Improve code while maintaining test coverage
   - Ensure all tests still pass

### Test Categories

#### Unit Tests
- Test individual components in isolation
- Mock dependencies when needed
- Focus on single responsibility

#### Integration Tests
- Test component interactions
- Verify game state changes
- Test scene transitions

### Using Fixtures
```python
# In conftest.py
@pytest.fixture
def game_window():
    """Provide a test game window."""
    return pygame.display.set_mode((800, 600))

# In your test
def test_render(game_window):
    sprite = GameSprite()
    sprite.render(game_window)
```

### Mocking in Tests
```python
# Example of mocking Pygame input
def test_player_input(monkeypatch):
    # Mock keyboard state
    mock_keys = {pygame.K_RIGHT: 1, pygame.K_LEFT: 0}
    monkeypatch.setattr(pygame.key, 'get_pressed',
                        lambda: mock_keys)
```

## Running Tests

### Basic Test Run
```bash
pytest
```

### With Coverage
```bash
pytest --cov=game
```

### Specific Test Categories
```bash
pytest tests/test_components  # Run component tests
pytest -k "player"           # Run tests with 'player' in name
```

## Best Practices

### Test Naming
- Use descriptive names: `test_player_moves_right_when_right_key_pressed`
- Group related tests in classes: `TestPlayerMovement`

### Test Independence
- Each test should be independent
- Use fixtures for setup/teardown
- Avoid test interdependence

### Test Coverage
- Aim for high coverage (>80%)
- Focus on critical game logic
- Don't sacrifice test quality for coverage

### Documentation
- Document test purpose
- Explain complex test setups
- Include examples in docstrings

## Troubleshooting

### Common Issues
1. **Pygame Display Issues**
   - Use dummy video driver in conftest.py
   - Initialize display in fixtures

2. **Test Isolation**
   - Reset game state between tests
   - Use fresh fixtures for each test

3. **Performance**
   - Mock heavy operations
   - Use appropriate fixture scopes
