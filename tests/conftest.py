#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for georastertools.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    - https://docs.pytest.org/en/stable/fixture.html
    - https://docs.pytest.org/en/stable/writing_plugins.html
"""

# import pytest


def pytest_addoption(parser):
    parser.addoption("--compare", action="store_true",
                     help="compare files generated by tests "
                          "with reference files: it may cause test errors "
                          "due to numeric accuracy problems")
    parser.addoption("--save_gen_as_ref", action="store_true",
                     help="store the files generated by the tests as new reference")


def pytest_generate_tests(metafunc):
    if "compare" in metafunc.fixturenames:
        if metafunc.config.getoption("compare"):
            compare = True
        else:
            compare = False
        metafunc.parametrize("compare", [compare])
    if "save_gen_as_ref" in metafunc.fixturenames:
        if metafunc.config.getoption("save_gen_as_ref"):
            save_gen_as_ref = True
        else:
            save_gen_as_ref = False
        metafunc.parametrize("save_gen_as_ref", [save_gen_as_ref])
