file_name = 'day1-trebuchet.txt'
s = 0

digit_starting_letters = 'otfsen'
digit_ending_letters = 'eorxnt'

valid_digits = {
  'one' : 1,
  'two' : 2,
  'three' : 3,
  'four' : 4,
  'five' : 5,
  'six' : 6,
  'seven' : 7,
  'eight' : 8,
  'nine' : 9,
}

with open(file_name) as file:
  data = file.readlines()
  for line in data:
    digit = ''
    digit_right = ''
    
    left, right = 0, -1,
    tens, ones = 0, 0
    
    while tens == 0 or ones == 0:
      
      if tens == 0:
        if line[left].isdigit():
          tens = int(line[left]) 
            
        elif line[left] in digit_starting_letters:

          for scan in range(left, len(line)):
            if line[scan].isdigit():
              break
            
            digit += line[scan]

            if digit in valid_digits:
              tens = valid_digits[digit]
              break
          
          digit = ''
        
        left += 1

      if ones == 0:
        
        if line[right].isdigit():
          ones = int(line[right])
      
        elif line[right] in digit_ending_letters:
          for scan in range(right, -1 * len(line) - 1, -1):
            if line[scan].isdigit():
              break
            
            digit_right = line[scan] + digit_right
            
            if digit_right in valid_digits:
              ones = valid_digits[digit_right]
              break
            
          digit_right = ''
        
        right -= 1      

    s += 10 * tens + ones
          
print(f'Sum = {s}')
      
      