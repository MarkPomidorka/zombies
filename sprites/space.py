import pygame


class Space(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"assets\images\grass.png")
        self.image = pygame.transform.scale(self.image,(599,670))
        self.rect = self.image.get_rect()

        self.image1 = pygame.image.load(r"assets\images\grass.png")
        self.image1 = pygame.transform.scale(self.image1,(599,670))
        self.rect1 = self.image1.get_rect()

        surface = pygame.display.get_surface()
        self.rect.midbottom = surface.get_rect().midbottom
        self.rect1.midbottom = self.rect.midtop

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.image1, self.rect1)

    def update(self):
        self.rect.y += 5
        self.rect1.y += 5
        surface = pygame.display.get_surface()
        if self.rect.top > surface.get_rect().bottom:
            self.rect.midbottom = self.rect1.midtop

        if self.rect1.top > surface.get_rect().bottom:
            self.rect1.midbottom = self.rect.midtop