import re

from weatherterm.core import ForecastType
from weatherterm.core import Forecast
from weatherterm.core import Request
from weatherterm.core import Unit
from weatherterm.core import UnitConverter


class WeatherComParser:
    def __init__(self):
        self._forecast = {
            ForecastType.TODAY: self._today_forecast,
            ForecastType.FIVEDAYS: self._five_days_forecast,
            ForecastType.TENDAYS: self._ten_days_forecast,
            ForecastType.WEEKEND: self._weekend_forecast,
        }
        self._base_url = 'http://weather.com/weather/{forecast}/1/{area}'
        self._requests = Request(self._base_url)

        self._temp_regex = re.compile('([0-9]+)\D{,2}([0-9]+)')
        self._only_digits_regex = re.compile('[0-9]+')

        self._unit_converter = UnitConverter(Unit.FAHRENHEIT)

    def _today_forecast(self, args):
        raise NotImplementedError

    def _five_days_forecast(self, args):
        raise NotImplementedError

    def _ten_days_forecast(self, args):
        raise NotImplementedError

    def _weekend_forecast(self, args):
        raise NotImplementedError

    def run(self, args):
        self._forecast_type = args.forecast_option
        forecast_function = self._forecast[args.forecast_option]
        return forecast_function(args)

    def _get_data(self, container, search_items):
        scraped_data = {}

        for key, value in search_items.items():
            result = container.find(value, class_=key)

            data = None if result is None else result.get_text()
