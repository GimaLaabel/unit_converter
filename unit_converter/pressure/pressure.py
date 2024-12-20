from enum import Enum, auto

class Pressure_unit(Enum):
    PSIA = "psia"
    PSIG = "psig"


# region Psia_Psig
def convert_psia_psig(value: float | list[float], unit: Pressure_unit) -> list[float, Pressure_unit.PSIG]:
    """
    This function converts pressure values from psia to psig. 
    It receives a value or list of values. It returns a list 
    of the converted value and an enum representing the unit
    """

    if type(value).__name__=="list":
        if unit == Pressure_unit.PSIA:
            new_val = [max(0, val-14.7) for val in value]
            return [new_val, Pressure_unit.PSIG]
        elif unit == Pressure_unit.PSIG:
            return [value, Pressure_unit.PSIG]

    if unit == Pressure_unit.PSIA:
        return [max(0, value - 14.7), Pressure_unit.PSIG]
    elif unit == Pressure_unit.PSIG:
        return [value, Pressure_unit.PSIG]
    
def convert_psig_psia(value: float | list[float], unit: Pressure_unit) -> list[float, Pressure_unit.PSIA]:
    """
    This function converts pressure values from psig to psia. 
    It receives a value or list of values.  It returns a list 
    of the converted value and an enum representing the unit
    """
    if type(value).__name__=="list":
        if unit == Pressure_unit.PSIG:
            new_val = [val+14.7 for val in value]
            return [new_val, Pressure_unit.PSIA]
        elif unit == Pressure_unit.PSIA:
            return [value, Pressure_unit.PSIA]

    if unit == Pressure_unit.PSIG:
        return [value + 14.7, Pressure_unit.PSIG]
    elif unit == Pressure_unit.PSIA:
        return [value, Pressure_unit.PSIA]

#endregion

if __name__ == "__main__":
    var1 = (10, Pressure_unit.PSIA)
#     var2 = (34, Pressure_unit.PSIG)
#     vars1 = ([23,45,78,90], Pressure_unit.PSIA)
#     vars2 = ([23,45,78,90], Pressure_unit.PSIG)

    
    result_var1 = convert_psia_psig(var1[0], var1[1])
#     result_var2 = convert_psig_psia(var2[0], var2[1])

#     result_vars1 = convert_psia_psig(vars1[0], vars1[1])
#     result_vars2 = convert_psig_psia(vars2[0], vars2[1])

    print(f"{convert_psia_psig.__name__}, {result_var1 = }")
#     print(f"{convert_psig_psia.__name__}, {result_var2 = }")
#     print(f"{convert_psia_psig.__name__}, {result_vars1 = }")
#     print(f"{convert_psig_psia.__name__}, {result_vars2 = }")