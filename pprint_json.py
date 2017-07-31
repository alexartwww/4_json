import sys
import json


def load_data(filepath):
    file_descriptor = open(filepath, "r")
    file_contents = file_descriptor.read()
    file_descriptor.close()
    return file_contents


def pretty_print_json(json_contents):
    print(json.dumps(json.loads(json_contents), sort_keys=True, indent = 4, encoding="utf-8", ensure_ascii=False, separators = (',', ': ')))


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] == '--help':
        print('JSON Pretty Print')
        print('Usage python pprint_json.py filename')
        sys.exit(0)

    json_contents = load_data(sys.argv[1])
    pretty_print_json(json_contents)
    sys.exit(0)
