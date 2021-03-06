#!/usr/bin/env python3

""" Module to test exercise2.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

# imports one per line
import pytest
from exercise2 import *


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("717951000841") is False
    assert checksum("453432902831") is False
    assert checksum("893243297634") is False


def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        checksum(1.0)
        checksum(786936224306)
        checksum(149389)

    with pytest.raises(ValueError):
        checksum("1")
        checksum("123456789023")
        checksum("dejection")


test_input()
test_checksum()