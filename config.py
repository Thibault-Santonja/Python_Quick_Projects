#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def trigger_arg(sys_args: list) -> dict:
    args = {}
    for arg in sys_args:
        try:
            attribute, value = arg.split("=")
            args.update({attribute: value})
        except ValueError:
            pass
    return args


def _handle_snake(**kwargs) -> None:
    from snake import main as snake
    snake.launch_game()


def _handle_astar(**kwargs) -> None:
    from astar_pathfinding import astar_pathfinding
    astar_pathfinding.launch_astar()


def _handle_brick_breaker(**kwargs) -> None:
    from brick_breaker import main as brick_breaker
    brick_breaker.launch_game()


def _handle_fibonacci(**kwargs) -> None:
    from fibonacci import fibonacci

    n = int(trigger_arg(kwargs.get("sys_args")).get("n", 0))
    print(f"Fibonacci for n={n} : {fibonacci.fib(n)}")


ARGUMENT_MAPPING = {
    "snake": _handle_snake,
    "astar": _handle_astar,
    "brick_breaker": _handle_brick_breaker,
    "fibonacci": _handle_fibonacci
}
