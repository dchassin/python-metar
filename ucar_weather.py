import requests
import re
from metar import Metar

def get(station):
	r = requests.get(f"http://weather.rap.ucar.edu/surface/index.php?metarIds={station}&hoursStr=most+recent+only&std_trans=standard&num_metars=number&submit_metars=Retrieve")
	if r.status_code != 200:
		raise Exception("request error (code={r.status_code})")
	match = re.search(f"{station} (.*)<",r.text)
	if not match:
		raise Exception("request error (no match)")
	obs = Metar.Metar(f'METAR {match.group(0)[:-1]}')
	if not obs:
		raise Exception("request error (no observation)")
	return obs.to_dict()
