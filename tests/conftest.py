import os
import pytest
import pygame

@pytest.fixture(scope="session", autouse=True)
def pygame_init():
    """Initialize pygame for testing."""
    os.environ["SDL_VIDEODRIVER"] = "dummy"
    os.environ["SDL_AUDIODRIVER"] = "dummy"
    pygame.init()
    yield
    pygame.quit()

@pytest.fixture
def game_settings():
    """Create game settings for testing."""
    from game.settings import Settings
    return Settings()
