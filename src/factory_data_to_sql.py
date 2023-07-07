#!/usr/bin/env python3

import json
from typing import List

def to_sql_values(values: List[int]):
  """
    Converts the values array to SQL quote notation and 
    casts each value to a string
  """
  return "\n  (" + ", ".join(map(str, values)) + ")"

f = open('data/seed_factory_data.json')
data = json.load(f)

all_values = []

lastId = 0
for item in data["factories"]:
  newId = lastId + 1
  data = item["factory"]["chart_data"]
  for i, _ in enumerate(data["time"]):
    all_values.append([
      newId, 
      data['sprocket_production_actual'][i], 
      data['sprocket_production_goal'][i], 
      data["time"][i]
    ])
  lastId = newId

statement = """INSERT INTO sprocket_factory
  (factory_id, production_actual, production_goal, timestamp) 
VALUES"""

sql_values = map(to_sql_values, all_values)
statement += ", ".join(sql_values)
print(statement)
