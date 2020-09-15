import os
import tempfile
import json
import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='key')
    parser.add_argument('--val', help='value')
    args = parser.parse_args()
    key = args.key
    value = args.value
    return key, value

def u_dict(dict, key, value):
    if key not in dict:
        dict[key] = value
    else:
        n_value = [dict[key]]
        n_value.append(value)
        dict[key] = n_value
    return  dict


def main():
    key, value = parse()
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if os.path.isfile('storage.py') is True:
        if value is None:
            with open('storage.data', 'r') as f:
                x = json.load(f)
                if type(x[key]) is list:
                    x = [i for i in x[key]]
                    print(', '.join(x))
                else:
                    print(x[key])
        else:
            with open('storage.data', 'w') as f:
                json.dump(dict(), f)

            with open('storage.data', 'r') as f:
                x = json.load(f)
                x = u_dict(x, key, value)

            with open('storage.data', 'w') as f:
                json.dump(x, f)

            if value is None:
                print(None)

main()

