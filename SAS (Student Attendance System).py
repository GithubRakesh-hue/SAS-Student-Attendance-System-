students={101:'Aarav',102:'Priya',103:'Rohit',104:'Sneha'}

attendance={'01-05-2026':{101:'P',102:'P',103:'P',104:'P'},
           '02-05-2026':{101:'P',102:'A',103:'A',104:'P'},
           '03-05-2026':{101:'P',102:'A',103:'P',104:'P'}}





#1] display all students
# def display():
#     for i , j in students.items():
#         print(i,j)

# display()




#2] Mark attendence
# def mark_attedance():
#     date=input("Enter the Date : ")
#     attendance[date]={}

#     for roll,name in students.items():
#         mark=input(f'{name} (P/A): ')
#         attendance[date][roll]=mark.upper()
#     print(attendance)

# mark_attedance()



# 3] view attendance
# def display():
#     date=input("Enter the data (formate : dd-mm-yyyy): ")
#     if date in attendance:
#         for roll,name in attendance[date].items():
#             print(roll,name)
#     else:
#         print('Date not found in database')

# display()


#4] total present student in specific date
# def total():
#     date=input("Enter the date (formate: dd-mm-yyyy) : ")
#     if date in attendance:
#         count=0
#         for i in attendance[date].values():
#             if i=='P':
#                 count+=1
#         print(f"Total no. of students present are : {count}")
#     else:
#         print("Plz try with another date")
        
# total()


#5] total absent student in specific date
# def total():
#     date=input("Enter the date (formate: dd-mm-yyyy) : ")
#     if date in attendance:
#         count=0
#         for i in attendance[date].values():
#             if i=='A':
#                 count+=1
#         print(f"Total no. of students absent are : {count}")
#     else:
#         print("Plz try with another date")
        
# total()

# #6] attendance percentage of student
# def att_per_st():
#     roll=int(input("Enter the roll number of student : "))
#     if roll in students:
#         present=0
#         for i in attendance.values():

#             for a,b, in i.items():

#                 if a == roll:
#                     if b == 'P':
#                         present+=1
#         per=present/len(attendance)*100
#         print(per)


#     else:
#         print("Student not found in database")

# att_per_st()




#7] student attendance report
# def report():
#     print('--------------------------------------------------------------------------------------')
#     print('|    ROLL NO     |   NAME    |   PRESENT   |   ABSENT    |   ATTENDANCE PERCENTAGE   |')
#     print('--------------------------------------------------------------------------------------')
#     for id,name in students.items():

#         present=0
#         absent=0

#         for data in attendance.values():
        
#             for roll,presenty in data.items():

#                 if roll == id:
                    
#                     if presenty=='P':
                        
#                         present+=1
                    
#                     else:

#                         absent+=1

#                     per = round ((present / len(attendance)) *100)

#         print(f"|     {id}        |   {name}   |      {present}      |      {absent}      |              {per} %         |")
#     print('--------------------------------------------------------------------------------------')
# report()




#8] students below 75 % attendance
# def policy(req_attendance):

#     dic={}
#     for id,name in students.items():

#         present=0
#         for data in attendance.values():

#             for roll, presenty in data.items():
                
#                 if roll == id :
#                     if presenty =='P':
#                         present+=1

#         per=round((present/len(attendance))*100)
#         dic[id]=per
#     print(f'students roll no. with attendance percentage ----- {dic}')

#     for roll,percentage in dic.items():

#         if percentage >= req_attendance:

#             print(f' Name : {students[roll]} , Roll No. : {roll} , Attendence : {percentage}')

# policy(75)




#9] top attendance student 

def top():
    dic={}
    for roll,name in students.items():
        present=0
        for data in attendance.values():
            
            for id,presenty in data.items():

                if id == roll:
                    if presenty=='P':
                        present+=1

 
        per=round((present/len(attendance))*100)
        dic[roll]=per
    
    
    topper=max(dic.values())
    

    for roll,percentage in dic.items():
        if percentage==topper :
            print(f'Name : {students[roll]} , roll : {roll}, per = {percentage}')

top()