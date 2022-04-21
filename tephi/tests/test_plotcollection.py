import tephi.tests as tests

import numpy as np
import pytest

import tephi
from tephi import Tephigram

_min = tephi.MIN_WET_ADIABAT
_max = tephi.MAX_WET_ADIABAT

def test_minimum_adiabat_respected():
    tephi.MAX_WET_ADIABAT = 0
    tephi.MIN_WET_ADIABAT = 20

    with pytest.raises(ValueError) as err:
        tephigram = Tephigram()
    assert "exceeds maximum threshold" in str(err.value)

    tephi.MAX_WET_ADIABAT = _max
    tephi.MIN_WET_ADIABAT = _min

def test_max_adiabat_is_0():
    pass
# `    tephi.MAX_WET_ADIABAT = 0
#     tephi.MIN_WET_ADIABAT = None

#     tephigram = Tephigram()

#     tephi.MAX_WET_ADIABAT = _max
#     tephi.MIN_WET_ADIABAT = _min`