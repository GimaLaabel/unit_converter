from unit_converter import convert_psia_psig, convert_psig_psia, Pressure_unit
import pytest

def test_convert_psia_psig_val():
    val = (34, Pressure_unit.PSIA)
    result = convert_psia_psig(val[0], val[1])
    assert result == (19.3, Pressure_unit.PSIG)

def test_convert_psia_psig_list():
    val_list = ([23,45,78,90], Pressure_unit.PSIA)
    result = convert_psia_psig(val_list[0], val_list[1])
    assert result == ([8.3, 30.3, 63.3, 75.3], Pressure_unit.PSIG)

# def test_convert_psia_psig_value_error():
#     val = (-2, Pressure_unit.PSIA)
#     result = convert_psia_psig(val[0], val[1])
#     assert result == (0, Pressure_unit.PSIG)
    # with pytest.raises(ValueError):
    #     convert_psia_psig(val[0], val[1])
    

def test_convert_psig_psia_val():
    val = (34, Pressure_unit.PSIG)
    result = convert_psig_psia(val[0], val[1])
    assert result == (48.7, Pressure_unit.PSIG)

def test_convert_psig_psia_list():
    val_list = ([23,45,78,90], Pressure_unit.PSIG)
    result = convert_psig_psia(val_list[0], val_list[1])
    assert result == ([37.7, 59.7, 92.7, 104.7], Pressure_unit.PSIA)


