def countApplesAndOranges(s, t, apple, orange, apples, oranges):
  applecount= 0
  orangecount= 0
  for i in range(len(apples)):
    temp = apple + apples[i]
    if(temp in range(s,t+1)):
      applecount += 1
  for i in range(len(oranges)):
    temp= orange + oranges[i]
    if(temp in range(s,t+1)):
      orangecount += 1
  print(applecount)
  print(orangecount)

if __name__ == '__main__':
  first_multiple_input = input().rstrip().split()
  s = int(first_multiple_input[0])
  t = int(first_multiple_input[1])
  second_multiple_input = input().rstrip().split()
  apple = int(second_multiple_input[0])
  orange = int(second_multiple_input[1])
  third_multiple_input = input().rstrip().split()
  m = int(third_multiple_input[0])
  n = int(third_multiple_input[1]
  countApplesAndOranges(s, t, apple, orange, apples, oranges)