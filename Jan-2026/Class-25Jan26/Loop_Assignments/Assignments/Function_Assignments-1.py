'''1. The Smart Attendance Logger
The Goal: 
Manage a classroom attendance list and ensure no duplicate entries are recorded if a student taps their ID card twice.

Concepts:  set ,  function ,  while .

The Problem: Create a function  mark_attendance()  that keeps asking for student names until the user types "STOP". 
             Store names in a Set to automatically prevent duplicates.

Input: Multiple strings (names) entered one by one.

Output: The final count of unique students and the set itself.

Hint:
Expected Flow: Start an empty  set  Use a  while True  loop to take  input()   
if  name is "STOP",  breakelse  add name to set Finally, print  len(attendance_set) '''



def mark_attendance():
    input_stud_name = input("Enter the student name:");
    attendance_set = [];
    while input_stud_name != 'STOP':
        attendance_set.append(input_stud_name);
        print(set(attendance_set));
        print("Lenght of Attendance set is:", len(attendance_set))
        input_stud_name = input("Enter the student name:");

    print("Flow Stopped!!!");

mark_attendance();