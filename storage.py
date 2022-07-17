import argparse
import os
import tempfile
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="key name")
parser.add_argument("--val", help="value")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


try:
    if os.path.exists(storage_path) and os.path.isfile(storage_path):
        if args.val:
            with open(storage_path, 'r') as f:
                json_data = json.load(f)
                if args.key in json_data:
                    json_data[args.key].append(args.val)
                else:
                    json_data[args.key] = [args.val]
                print(json_data)
            
            with open(storage_path, "w") as f:
                json.dump(json_data, f) 
        else:
            with open(storage_path, 'r') as f:
                json_data = json.load(f)
                print(', '.join(json_data.get(args.key)))
    else:
        print("error")    
except:
    json_data = {}
    with open(storage_path, 'w') as f:
        json.dump(json_data, f)
    