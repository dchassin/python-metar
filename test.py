import ucar_weather
from pprint import PrettyPrinter
pprint = PrettyPrinter(indent=4).pprint

ucar_weather.debug = True

pprint(ucar_weather.stations())
pprint(ucar_weather.get("KSFO"))
