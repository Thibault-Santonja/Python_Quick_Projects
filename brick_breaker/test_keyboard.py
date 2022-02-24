from unittest import TestCase

import pygame

from brick_breaker import keyboard


class Test(TestCase):
    def test_event_handler(self):
        """pygame.K_LEFT: _handle_left,
        pygame.K_RIGHT: _handle_right,
        pygame.K_ESCAPE: _handle_escape"""
        self.assertEqual(keyboard.KEYBOARD_EVENT[pygame.K_LEFT](), (0, -1))
        self.assertEqual(keyboard.KEYBOARD_EVENT[pygame.K_RIGHT](), (0, 1))
        self.assertEqual(keyboard.KEYBOARD_EVENT[pygame.K_ESCAPE](), None)
