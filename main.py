def staircase(n):
  for i in range(1, n+1):
    print(" "*(n-i)+"#"*(i))
def staircase(n):
  for row in range(n):
    string=""
    for col in range(n):
      if col <= row:
        string += "#"
      else: 
        string= " " + string
    print(string)
    
def staircase(n, row=0, string=""):
  if n == row:
    return
  if n== len(string):
    print(string)
    return staircase(n, row+1)
  add = "#" if len(string) <= row else" "
  staircase(n, row, add+ string)        
      
  

