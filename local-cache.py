"""Build a local cache of Pokémon type data for types 1 through 19."""

import json
import time
from pathlib import Path
from urllib.request import Request, urlopen


API_URL = "https://pokeapi.co/api/v2/type/"
CACHE_FILE = Path(__file__).with_name("type-cache.json")
REQUEST_INTERVAL = 2


def load_cache():
	if not CACHE_FILE.exists():
		return {}
	try:
		with CACHE_FILE.open("r", encoding="utf-8") as cache_file:
			data = json.load(cache_file)
		return data if isinstance(data, dict) else {}
	except (OSError, json.JSONDecodeError):
		return {}


def fetch_type(type_number):
	request = Request(
		API_URL + str(type_number),
		headers={"User-Agent": "pokemon-weakness-notifier/1.0"},
	)
	with urlopen(request, timeout=30) as response:
		return json.load(response)


def main():
	cache = load_cache()
	last_request = None

	for type_number in range(1, 20):
		key = str(type_number)
		if key in cache:
			continue

		print(type_number, flush=True)
		if last_request is not None:
			time.sleep(max(0, REQUEST_INTERVAL - (time.monotonic() - last_request)))
		cache[key] = fetch_type(type_number)
		last_request = time.monotonic()

		with CACHE_FILE.open("w", encoding="utf-8") as cache_file:
			json.dump(cache, cache_file, indent=2, sort_keys=True)


if __name__ == "__main__":
	main()
