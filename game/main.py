import pygame
from game.settings import Settings

class Game:
    """Main game class."""

    def __init__(self):
        """Initialize game."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.title)
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        """Handle game events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        """Update game state."""
        pass

    def draw(self):
        """Draw the game screen."""
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

    def run(self):
        """Main game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.settings.fps)

        pygame.quit()
