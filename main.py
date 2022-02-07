#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

import sys
from typing import Callable

import config


def _handle_unknown(argument: str) -> Callable[[], None]:
    def print_error():
        print(f"Unknown argument : {argument}")
    return print_error


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        project_handler = config.ARGUMENT_MAPPING.get(arg, _handle_unknown(arg))
        project_handler()
