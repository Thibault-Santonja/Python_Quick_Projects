#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

import sys
import config


def _handle_unknown(argument: str) -> None:
    print(f"Unknown argument : {argument}")


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        project_handler = config.ARGUMENT_MAPPING.get(arg, _handle_unknown(arg))
        project_handler()
