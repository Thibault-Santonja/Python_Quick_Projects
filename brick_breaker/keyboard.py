from typing import Optional
import pygame


def _handle_left(*args, **kwargs) -> Optional[tuple]:
    """

    @return:
    """
    return 0, -1


def _handle_right(*args, **kwargs) -> Optional[tuple]:
    """

    @return:
    """
    return 0, 1


def _handle_escape(*args, **kwargs) -> Optional[tuple]:
    """

    @param move_x:
    @param move_y:
    @return:
    """
    return None


KEYBOARD_EVENT = {
    pygame.K_LEFT: _handle_left,
    pygame.K_RIGHT: _handle_right,
    pygame.K_ESCAPE: _handle_escape
}


def get_keyboard_action(event: pygame.event.Event) -> Optional[tuple]:
    """
    Get keyboard action

    @return:
    """
    # fixme : to log on DEBUG mode `print(event)`
    # Quit the UI
    if event.type == pygame.QUIT:
        return None
    elif event.type == pygame.KEYDOWN:
        event_handler = KEYBOARD_EVENT.get(event.key, None)
        if event_handler:
            return event_handler()

    return 0, 0  # Return null movement
