"""make a readable json file readable by adding indentation."""
import json
filename = '16data/eq_data_1_day_m1.json'
with open(filename) as f:
	all_eq_data = json.load(f)
reader = '16data/reader.json'
with open(reader, 'w') as f:
	json.dump(all_eq_data, f, indent=4)
