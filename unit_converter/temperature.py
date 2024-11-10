from enum import Enum

class Temperature_unit(Enum):
    DEG_F = "\u00B0F"
    DEG_C = "\u00B0C"
    DEG_K = "\u00B0K"
    DEG_R = "\u00B0R"

# region Fahrenheit_Rankine
def convert_degf_degr(value: float | list[float], unit: Temperature_unit) -> list[float, Temperature_unit.DEG_R]:
    """
    This function converts temperature values from degree fahrenheit
    to degree rankine. It receives a value or list of values. 
    It returns a list of the converted value and an enum 
    representing the unit
    """
    # This handles list of values
    if type(value).__name__=="list":
        if unit == Temperature_unit.DEG_F:
            new_val = [val + 459.67 for val in value]
            return [new_val, Temperature_unit.DEG_R]
        elif unit == Temperature_unit.DEG_F:
            return [value, Temperature_unit.DEG_F]

    # This handles single values
    if unit == Temperature_unit.DEG_F:
        return [value + 459.67, Temperature_unit.DEG_R]
    elif unit == Temperature_unit.DEG_R:
        return [value, Temperature_unit.DEG_R]


def convert_degr_degf(value: float | list[float], unit: Temperature_unit) -> list[float, Temperature_unit.DEG_R]:
    """
    This function converts temperature values from degree rankine
    to degree Fahrenheit. It receives a value or list of values. 
    It returns a list of the converted value and an enum 
    representing the unit
    """
    # This handles list of values
    if type(value).__name__=="list":
        if unit == Temperature_unit.DEG_R:
            new_val = [val - 459.67 for val in value]
            return [new_val, Temperature_unit.DEG_F]
        elif unit == Temperature_unit.DEG_F:
            return [value, Temperature_unit.DEG_F]

    # This handles single values
    if unit == Temperature_unit.DEG_R:
        return [value - 459.67, Temperature_unit.DEG_F]
    elif unit == Temperature_unit.DEG_F:
        return [value, Temperature_unit.DEG_F]
    
#endregion


# region Fahrenheit_Celsius
def convert_degf_degc(value: float | list[float], unit: Temperature_unit) -> list[float, Temperature_unit.DEG_C]:
    """
    This function converts temperature values from degree Fahrenheit
    to degree celsius. It receives a value or list of values. 
    It returns a list of the converted value and an enum 
    representing the unit
    """
    # This handles list of values
    if type(value).__name__=="list":
        if unit == Temperature_unit.DEG_F:
            new_val = [(val - 32)*5/9 for val in value]
            return [new_val, Temperature_unit.DEG_C]
        elif unit == Temperature_unit.DEG_C:
            return [value, Temperature_unit.DEG_C]

    # This handles single values
    if unit == Temperature_unit.DEG_F:
        return [(value - 32)*5/9, Temperature_unit.DEG_C]
    elif unit == Temperature_unit.DEG_C:
        return [value, Temperature_unit.DEG_C]
    
def convert_degc_degf(value: float | list[float], unit: Temperature_unit) -> list[float, Temperature_unit.DEG_F]:
    """
    This function converts temperature values from degree Celsius
    to degree Fahrenheit. It receives a value or list of values. 
    It returns a list of the converted value and an enum 
    representing the unit
    """
    # This handles list of values
    if type(value).__name__=="list":
        if unit == Temperature_unit.DEG_C:
            new_val = [(val * 1.8)+32 for val in value]
            return [new_val, Temperature_unit.DEG_F]
        elif unit == Temperature_unit.DEG_F:
            return [value, Temperature_unit.DEG_F]

    # This handles single values
    if unit == Temperature_unit.DEG_C:
        return [(value * 1.8)+32, Temperature_unit.DEG_F]
    elif unit == Temperature_unit.DEG_F:
        return [value, Temperature_unit.DEG_F]

#endregion


# region Fahrenheit_Kelvin
def convert_degf_degk(value: float | list[float], unit: Temperature_unit) -> list[float, Temperature_unit.DEG_K]:
    """
    This function converts temperature values from degree Fahrenheit
    to degree kelvin. It receives a value or list of values. 
    It returns a list of the converted value and an enum 
    representing the unit
    """
    # This handles list of values
    if type(value).__name__=="list":
        if unit == Temperature_unit.DEG_F:
            new_val = [(val - 32)*5/9 + 273.15 for val in value]
            return [new_val, Temperature_unit.DEG_K]
        elif unit == Temperature_unit.DEG_K:
            return [value, Temperature_unit.DEG_K]

    # This handles single values
    if unit == Temperature_unit.DEG_F:
        return [(value - 32)*5/9 + 273.15, Temperature_unit.DEG_K]
    elif unit == Temperature_unit.DEG_K:
        return [value, Temperature_unit.DEG_K]
    
def convert_degk_degf(value: float | list[float], unit: Temperature_unit) -> list[float, Temperature_unit.DEG_F]:
    """
    This function converts temperature values from degree kelvin
    to degree Fahrenheit. It receives a value or list of values. 
    It returns a list of the converted value and an enum 
    representing the unit
    """
    # This handles list of values
    if type(value).__name__=="list":
        if unit == Temperature_unit.DEG_K:
            new_val = [(val - 273.15) * (9/5) + 32 for val in value]
            return [new_val, Temperature_unit.DEG_F]
        elif unit == Temperature_unit.DEG_F:
            return [value, Temperature_unit.DEG_F]

    # This handles single values
    if unit == Temperature_unit.DEG_K:
        return [(value - 273.15) * (9/5) + 32, Temperature_unit.DEG_F]
    elif unit == Temperature_unit.DEG_F:
        return [value, Temperature_unit.DEG_F]

#endregion


# region Celsius_Kelvin
def convert_degc_degk(value: float | list[float], unit: Temperature_unit) -> list[float, Temperature_unit.DEG_K]:
    """
    This function converts temperature values from degree celsius
    to degree kelvin. It receives a value or list of values. 
    It returns a list of the converted value and an enum 
    representing the unit
    """
    # This handles list of values
    if type(value).__name__=="list":
        if unit == Temperature_unit.DEG_C:
            new_val = [val + 273.15 for val in value]
            return [new_val, Temperature_unit.DEG_K]
        elif unit == Temperature_unit.DEG_K:
            return [value, Temperature_unit.DEG_K]

    # This handles single values
    if unit == Temperature_unit.DEG_C:
        return [value + 273.15, Temperature_unit.DEG_K]
    elif unit == Temperature_unit.DEG_K:
        return [value, Temperature_unit.DEG_K]


def convert_degk_degc(value: float | list[float], unit: Temperature_unit) -> list[float, Temperature_unit.DEG_C]:
    """
    This function converts temperature values from degree kelvin
    to degree celsius. It receives a value or list of values. 
    It returns a list of the converted value and an enum 
    representing the unit
    """
    # This handles list of values
    if type(value).__name__=="list":
        if unit == Temperature_unit.DEG_K:
            new_val = [val - 273.15 for val in value]
            return [new_val, Temperature_unit.DEG_C]
        elif unit == Temperature_unit.DEG_C:
            return [value, Temperature_unit.DEG_C]

    # This handles single values
    if unit == Temperature_unit.DEG_K:
        return [value - 273.15, Temperature_unit.DEG_C]
    elif unit == Temperature_unit.DEG_C:
        return [value, Temperature_unit.DEG_C]
    
#endregion


# region Celsius_Rankine
def convert_degc_degr(value: float | list[float], unit: Temperature_unit) -> list[float, Temperature_unit.DEG_R]:
    """
    This function converts temperature values from degree celsius
    to degree rankine. It receives a value or list of values. 
    It returns a list of the converted value and an enum 
    representing the unit
    """
    # This handles list of values
    if type(value).__name__=="list":
        if unit == Temperature_unit.DEG_C:
            new_val = [(val + 273.15) * 9/5 for val in value]
            return [new_val, Temperature_unit.DEG_R]
        elif unit == Temperature_unit.DEG_R:
            return [value, Temperature_unit.DEG_R]

    # This handles single values
    if unit == Temperature_unit.DEG_C:
        return [(value + 273.15) * 9/5, Temperature_unit.DEG_R]
    elif unit == Temperature_unit.DEG_R:
        return [value, Temperature_unit.DEG_R]


def convert_degr_degc(value: float | list[float], unit: Temperature_unit) -> list[float, Temperature_unit.DEG_C]:
    """
    This function converts temperature values from degree rankine
    to degree celsius. It receives a value or list of values. 
    It returns a list of the converted value and an enum 
    representing the unit
    """
    # This handles list of values
    if type(value).__name__=="list":
        if unit == Temperature_unit.DEG_R:
            new_val = [(val - 491.67) * 5/9 for val in value]
            return [new_val, Temperature_unit.DEG_C]
        elif unit == Temperature_unit.DEG_C:
            return [value, Temperature_unit.DEG_C]

    # This handles single values
    if unit == Temperature_unit.DEG_R:
        return [(value - 491.67) * 5/9, Temperature_unit.DEG_C]
    elif unit == Temperature_unit.DEG_C:
        return [value, Temperature_unit.DEG_C]
    
#endregion


# region Rankine_Kelvin
def convert_degr_degk(value: float | list[float], unit: Temperature_unit) -> list[float, Temperature_unit.DEG_K]:
    """
    This function converts temperature values from degree rankine
    to degree kelvin. It receives a value or list of values. 
    It returns a list of the converted value and an enum 
    representing the unit
    """
    # This handles list of values
    if type(value).__name__=="list":
        if unit == Temperature_unit.DEG_R:
            new_val = [val * 5/9 for val in value]
            return [new_val, Temperature_unit.DEG_K]
        elif unit == Temperature_unit.DEG_K:
            return [value, Temperature_unit.DEG_K]

    # This handles single values
    if unit == Temperature_unit.DEG_R:
        return [value * 5/9, Temperature_unit.DEG_K]
    elif unit == Temperature_unit.DEG_K:
        return [value, Temperature_unit.DEG_K]
    
def convert_degk_degr(value: float | list[float], unit: Temperature_unit) -> list[float, Temperature_unit.DEG_R]:
    """
    This function converts temperature values from degree kelvin
    to degree rankine. It receives a value or list of values. 
    It returns a list of the converted value and an enum 
    representing the unit
    """
    # This handles list of values
    if type(value).__name__=="list":
        if unit == Temperature_unit.DEG_K:
            new_val = [val * 9/5 for val in value]
            return [new_val, Temperature_unit.DEG_R]
        elif unit == Temperature_unit.DEG_R:
            return [value, Temperature_unit.DEG_R]

    # This handles single values
    if unit == Temperature_unit.DEG_K:
        return [value * 9/5, Temperature_unit.DEGR]
    elif unit == Temperature_unit.DEG_R:
        return [value, Temperature_unit.DEGR]

#endregion



if __name__ == "__main__":
    # Accessing members
    print((Temperature_unit.DEG_F.value, Temperature_unit.DEG_C.value, Temperature_unit.DEG_K.value, Temperature_unit.DEG_R.value))   
    val = (99, Temperature_unit.DEG_F)
    print(f"{convert_degf_degr(val[0], val[1])= }")

    val1 = (558.67, Temperature_unit.DEG_R)
    print(f"{convert_degr_degf(val[0], val[1])= }")