def gradingStudents(grades):
  n= int(input().strip())
  for a in range(n):
    grade= int(input().strip())

    if grade >= 38:
      mod5 = grade % 5
      if mod5 >= 3:
        garde = grade + (5 - mod5)
  print(grade)

  
if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  grades_count = int(input().strip())
  grades = []
  for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)
  result = gradingStudents(grades)
  fptr.write('\n'.join(map(str, result)))
  fptr.write('\n')
  fptr.close()


  