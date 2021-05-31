import mysql.connector
  
global mydb,cursor
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "praveen@51",
  database = "assessment2"
) 
  
mycursor = mydb.cursor()

def clear():
    for _ in range(2):
        print()


#   function name       : students_details
#   purpose             : To Display Student Details
def students_details():
  clear()
  mycursor.execute('SELECT * FROM  studentdetails')
  for row in mycursor.fetchall():
    print(row)

  mycursor.execute('SELECT SUM(Student_Fees)FROM studentdetails')
  Total_Fees=mycursor.fetchall()[0][0]
  clear()
  print('Total Fees Collected From Students :',Total_Fees)


#   function name       : staff_details
#   purpose             : To Display Staff Details
def staff_details():
  clear()
  mycursor.execute('SELECT * FROM  staffdetails')
  for row in mycursor.fetchall():
    print(row)
    clear()

  mycursor.execute('SELECT SUM(Num_Absent)FROM staffdetails')
  Num_absent=mycursor.fetchall()[0][0]
  
  sql ="update staffdetails set LOP_Amt='500' where Num_Absent='1'"
  mycursor.execute(sql)
  mydb.commit()

  sql ="update staffdetails set LOP_Amt='1000' where Num_Absent='2'"
  mycursor.execute(sql)
  mydb.commit()   


  sql ="update staffdetails set LOP_Amt='0' where Num_Absent='0'"
  mycursor.execute(sql)
  mydb.commit()   
  print("RECORD UPDATED SUCCESSFULLY")

  print('Total Absent Days:',Num_absent)
  print('LOP_Amt:',Num_absent*500)
 


#   function name       : students_Attendance
#   purpose             : To Display Students Attendance

def Student_Attendance():
  clear()
  print("----STUDENT ATTENDANCE FOR 10 DAYS----")
  mycursor.execute('SELECT * FROM  studentattendance')
  for row in mycursor.fetchall():
    print(row)

    clear()
  mycursor.execute('SELECT SUM(AbsentDays)FROM studentattendance')
  Num_absent=mycursor.fetchall()[0][0]
  print('Total Num of Absents Taken By Students:',Num_absent)
  print('Fine Amt:',Num_absent*100)
  

  
#   function name       : payment_details
#   purpose             : To Display Payment Details
def payment_details():
  Fine = int(input("Enter Total Fine Amt:"))
  LOP = int(input("Enter the Total LOP Amount:"))
  mycursor.execute('SELECT SUM(Student_Fees)FROM studentdetails')
  Total_Fees=mycursor.fetchall()[0][0]
  StudentAmount =Total_Fees + Fine +LOP
  print("Total Amount Collected: ",StudentAmount)
  EstimatedSalary = StudentAmount/5
  print("Estimated Salary:",EstimatedSalary)
  
  sql ="update paymentdetail set Staff_Salary ='5640' where Staff_LOP='0'"
  mycursor.execute(sql)
  mydb.commit()   
  
  sql ="update paymentdetail set Staff_Salary ='5140' where Staff_LOP='500'"
  mycursor.execute(sql)
  mydb.commit()

  sql ="update paymentdetail set Staff_Salary ='4640' where Staff_LOP='1000'"
  mycursor.execute(sql)
  mydb.commit()
  print("Salary updated Successfully")
  clear()

def main_menu():
    while True:
        clear()
        print('M A I N   M E N U')
      
        print('1.   Student Details')
        print('2.   Staff Details')
        print('3.   Student Attendance')
        print('4.   Payment Details')
        print('5.   Exit')
        choice = int(input('\n\nEnter your choice (1..5): '))   

        if choice==1:
          students_details()
        if choice==2:
          staff_details()
        if choice==3:
          Student_Attendance() 
        if choice==4:
          payment_details()  
        if choice==5:
            break


if __name__=="__main__":
  clear()
  main_menu()
