

"""
The program is trying to display the number of grades, the average grade, and the
percentage of grades that are above the average grades using
The number of grades: 24
Average grade: 83.25
Percentage of grades above average: 54.17%

Required also to write a main() function to initialize (kickstart) the application, and a
calculate_percent_above_average() function to calculate the percentage of grades that
are above the average grade.
"""

"""
##Analyze grades on a final examination.
infile = open("Final.txt", 'r')
grades = [line.rstrip() for line infile]
infile.close()
for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0    # number of grades above average
for grade in grades:
    if grade > average:
        num += 1
print("Number of grades:", len(grades))
print("Average grade:", average)
print("Percentage of grades above average: {0:.2f}%"
                    .format(100 * num / len(grades)))

main():
    initialize (kickstart)
    calculate_percent_above_average()
"""
def total, average as double
def numGrades, AvgCount as integer
def standard grades() As string
If numGrades > 0 Then
  average = total / numGrades
   AvgCount = 0
    For itr As Integer = 0 To stdGrades.Length - 1
       If tmpGrades(itr) > average Then
           AvgCount += 1
        End if
main():
    initialize (kickstart)
    calculate_percent_above_average()
