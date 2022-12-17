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