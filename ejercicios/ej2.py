def compareTriplets(a, b):  
  a1= 0
  b1= 0
  for i in range(0,3):
    if a[i]>b[i]:
      a1 += 1
    if a[i]<b[i]:
      b1 += 1
    return[a1,b1]
  
if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  a = list(map(int, input().rstrip().split()))
  b = list(map(int, input().rstrip().split()))
  result = compareTriplets(a, b)
  fptr.write(' '.join(map(str, result)))
  fptr.write('\n')
  fptr.close()
