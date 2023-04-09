import re
import json


def read_template(file):
    with open(file) as f:
        return f.read().strip()


def parse_template(string):
    return re.findall(r'{([^}]+)}', string)


if __name__ == "__main__":
    path = "assets/example.txt"
    print("Welcome to Madlib")
    template = read_template(path)
    print(template)
    json_template = json.dumps(template)
    print(json_template)
    parsed_template = parse_template(json_template)
    print(parsed_template)
