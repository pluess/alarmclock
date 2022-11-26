import machine

_adc = machine.ADC(26)

def read_sensor() -> int:
    return _adc.read_u16()