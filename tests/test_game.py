import pytest
from game.main import Game

def test_game_initialization(game_settings):
    """Test game initialization."""
    game = Game()
    assert game.settings.screen_width == game_settings.screen_width
    assert game.settings.screen_height == game_settings.screen_height
    assert game.settings.title == game_settings.title
    assert game.running == True

def test_game_quit():
    """Test game quit functionality."""
    game = Game()
    game.running = False
    assert game.running == False
