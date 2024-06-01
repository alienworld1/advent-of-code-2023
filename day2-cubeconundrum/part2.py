file_name = 'main.txt'
power_sum = 0 
colors = ('red', 'green', 'blue')

def classify(string: str) -> dict:
  details = string.split()
  game_details = {
    'id': int(details[1][:-1]),
    'sets': [],
    }

  set_details = {}
  for i in range(2, len(details)):
    if details[i].isdigit():
      n = int(details[i])
      
    else:
      color = details[i][:-1] if details[i].endswith(';') or details[i].endswith(',') else details[i]
      set_details[color] = n

      if not details[i].endswith(','):
        game_details['sets'].append(set_details)
        set_details = {}
  
  return game_details
  
with open(file_name) as file:
  for line in file:
    details = classify(line)
    min_cubes = {'red': 0, 'blue': 0, 'green': 0}
    
    for set in details['sets']:
      for color in colors:
        if set.get(color, 0) > min_cubes.get(color):
          min_cubes[color] = set.get(color)
      
    power_sum += min_cubes['red'] * min_cubes['blue'] * min_cubes['green']

print(f'Sum = {power_sum}')    
    