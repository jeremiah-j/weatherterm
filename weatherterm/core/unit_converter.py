from .unit import Unit


class UnitConverter:
    def __init__(self, parser_default_unit, dest_unit=None):
        self._parser_default_unit = parser_default_unit
        # dest_unit property has no '_' in the book then they immediately
        # try to return _dest_unit in self.dest_unit() so I changed it to _dest_unit
        self._dest_unit = dest_unit

        self._convert_functions = {
            Unit.CELCIUS: self._to_celsius,
            Unit.FAHRENHEIT: self._to_fahrenheit,
        }

    @property
    def dest_unit(self):
        return self._dest_unit

    @dest_unit.setter
    def dest_unit(self, dest_unit):
        self._dest_unit = dest_unit

    def convert(self, temp):

        try:
            temperature = float(temp)
        except ValueError:
            return 0

        if (self._dest_unit == self._parser_default_unit or
                self._dest_unit is None):
            return self._format_results(temperature)

        func = self._convert_functions[self._dest_unit]
        result = func(temperature)

        return self._format_results(result)

    def _format_results(self, value):
        return int(value) if value.is_integer() else f'{value:.f}'

    def _to_celsius(self, fahrenheit_temp):
        result = (fahrenheit_temp - 32) * 5/9
        return result

    def _to_fahrenheit(self, celsius_temp):
        result = (celsius_temp * 9/5) + 32
        return result