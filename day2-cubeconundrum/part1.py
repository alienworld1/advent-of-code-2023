file_name = 'main.txt'
id_sum = 0

max_cubes = {'red': 12, 'green': 13, 'blue': 14}

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
    isValid = True
    
    for game_set in details['sets']:
      
      for key, value in game_set.items():
        if value > max_cubes[key]:
          isValid = False
          break
        
      if not isValid:
        break
    
    else:
      id_sum += details['id']

print(f'Sum = {id_sum}')    
    