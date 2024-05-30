file_name = 'day1-trebuchet.txt'
s = 0

with open(file_name) as file:
  data = file.readlines()

  for line in data:
    left, right = 0, -1

    while True:
      if line[left].isdigit():
        if line[right].isdigit():
          s += int(line[left]) * 10 + int(line[right])
          break
        else:
          right -= 1
          
      else:
        if line[right].isdigit():
          left += 1

        else:
          left += 1
          right -= 1
          
print(f'Sum = {s}')
      
      