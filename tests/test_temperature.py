import pytest
from unit_converter import convert_degf_degr, convert_degr_degf, Temperature_unit


def test_convert_degf_degr():
    val = (99, Temperature_unit.DEG_F)
    result = convert_degf_degr(val[0], val[1])
    result[0] = round(result[0], 4)
    expected = [558.67, Temperature_unit.DEG_R]
    assert result == expected


def test_convert_degr_degf():
    val = (558.67, Temperature_unit.DEG_R)
    result = convert_degr_degf(val[0], val[1])
    result[0] = round(result[0], 4)
    expected = [99, Temperature_unit.DEG_F]
    assert result == expected
    
    

