from enum import Enum, auto

class Density_unit(Enum):
    LB_FT3 = "lb/ft3"
    KG_M3 = "kg/m3"

def convert_lbf3_kgm3(value: float, unit: Density_unit):
    if unit == Density_unit.LB_FT3:
        pass
    elif unit == Density_unit.KG_M3:
        pass






