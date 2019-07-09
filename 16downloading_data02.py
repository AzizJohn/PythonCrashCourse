"""make a readable json file readable by adding indentation."""
import json
filename = '16data/eq_data_1_day_m1.json'
with open(filename) as f:#f is a file object.
	all_eq_data = json.load(f)#all_eq_data is a json object.
reader = '16data/reader.json'
with open(reader, 'w') as f:
	json.dump(all_eq_data, f, indent=4)
#The json.dump() function takes a JSON data object and a file object, and
#writes the data to that file
#The indent=4 argument tells dump() to format the data using indentation
#that matches the data’s structure.
