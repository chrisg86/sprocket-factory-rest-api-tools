#!/usr/bin/env python3

import json
from typing import List

def to_sql_values(values: List[int]):
  """
    Converts the values array to SQL quote notation and 
    casts each value to a string
  """
  return "\n  (" + ", ".join(map(str, values)) + ")"

f = open('data/seed_sprocket_types.json')
data = json.load(f)

all_values = []

for item in data["sprockets"]:
  all_values.append([
    item['teeth'],
    item['pitch_diameter'],
    item["outside_diameter"],
    item["pitch"],
  ])

statement = """INSERT INTO sprocket
  (teeth, pitch_diameter, outside_diameter, pitch) 
VALUES"""

sql_values = map(to_sql_values, all_values)
statement += ", ".join(sql_values)
print(statement)
