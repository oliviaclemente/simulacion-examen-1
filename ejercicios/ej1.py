def simpleArraySum(ar):
  n= int(input("Dame una matrix 3x3:"))
  num= list(map(int, input().split))
  sum=0
  for n1 in num:
    sum += n1
  print(sum)

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  ar_count = int(input().strip())
  ar = list(map(int, input().rstrip().split()))
  result = simpleArraySum(ar)
  fptr.write(str(result) + '\n')
  fptr.close()