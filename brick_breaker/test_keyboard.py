from unittest import TestCase

import pygame

from brick_breaker import keyboard


class Test(TestCase):
    def test_event_handler(self):
        self.assertEqual(keyboard.KEYBOARD_EVENT[pygame.K_LEFT](), (0, -1))
        self.assertEqual(keyboard.KEYBOARD_EVENT[pygame.K_RIGHT](), (0, 1))
        self.assertEqual(keyboard.KEYBOARD_EVENT[pygame.K_ESCAPE](), None)

    def test_get_keyboard_action(self):
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=2, pos=(5, 5))
        self.assertEqual(keyboard.get_keyboard_action(event), (0, 0))

        event = pygame.event.Event(pygame.QUIT)
        self.assertEqual(keyboard.get_keyboard_action(event), None)

        event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_LEFT})
        self.assertEqual(keyboard.get_keyboard_action(event), (0, -1))
        event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_RIGHT})
        self.assertEqual(keyboard.get_keyboard_action(event), (0, 1))
        event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_ESCAPE})
        self.assertEqual(keyboard.get_keyboard_action(event), None)
        event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_4})
        self.assertEqual(keyboard.get_keyboard_action(event), (0, 0))
