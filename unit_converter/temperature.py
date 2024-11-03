from enum import Enum

class temperature_unit(Enum):
    DEGF = "\u00B0F"
    DEGC = "\u00B0c"



if __name__ == "__main__":
    # Accessing members
    print(temperature_unit.F.name)   # Output: ACTIVE
    print(temperature_unit.F.value)  # Output: ACTIVE
    print(type(temperature_unit.F.value))  # Output: ACTIVE