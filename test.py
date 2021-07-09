import ucar_weather
from pprint import PrettyPrinter
pprint = PrettyPrinter(indent=4).pprint

pprint(ucar_weather.get("KSFO"))
