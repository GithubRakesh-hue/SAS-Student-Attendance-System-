while True:

    print("\n")
    print("="*55)
    print("      SAS STUDENT ATTENDANCE SYSTEM")
    print("="*55)
    print("1. Display All Students")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Total Present Students")
    print("5. Total Absent Students")
    print("6. Attendance Percentage of Student")
    print("7. Student Attendance Report")
    print("8. Students Above 75% Attendance")
    print("9. Top Attendance Student")
    print("0. Exit")
    print("="*55)

    choice = input("Enter Your Choice : ")

    if choice == '1':

        print("\n----- STUDENT LIST -----")
        for roll,name in students.items():
            print(f"Roll No : {roll} | Name : {name}")

    elif choice == '2':

        date=input("Enter the Date : ")
        attendance[date]={}

        for roll,name in students.items():
            mark=input(f'{name} (P/A): ')
            attendance[date][roll]=mark.upper()

        print("Attendance Marked Successfully")

    elif choice == '3':

        date=input("Enter the Date (dd-mm-yyyy): ")

        if date in attendance:

            print(f"\nAttendance for {date}")

            for roll,status in attendance[date].items():
                print(f"Roll No : {roll} | Status : {status}")

        else:
            print("Date Not Found")

    elif choice == '4':

        date=input("Enter the Date (dd-mm-yyyy): ")

        if date in attendance:

            count=0

            for status in attendance[date].values():

                if status=='P':
                    count+=1

            print(f"Total Present Students : {count}")

        else:
            print("Date Not Found")

    elif choice == '5':

        date=input("Enter the Date (dd-mm-yyyy): ")

        if date in attendance:

            count=0

            for status in attendance[date].values():

                if status=='A':
                    count+=1

            print(f"Total Absent Students : {count}")

        else:
            print("Date Not Found")

    elif choice == '6':

        roll=int(input("Enter Roll Number : "))

        if roll in students:

            present=0

            for data in attendance.values():

                for r,status in data.items():

                    if r==roll and status=='P':
                        present+=1

            per=(present/len(attendance))*100

            print(f"Student Name : {students[roll]}")
            print(f"Attendance Percentage : {round(per,2)} %")

        else:
            print("Student Not Found")

    elif choice == '7':

        print('-'*90)
        print('| ROLL NO | NAME | PRESENT | ABSENT | ATTENDANCE % |')
        print('-'*90)

        for id,name in students.items():

            present=0
            absent=0

            for data in attendance.values():

                for roll,presenty in data.items():

                    if roll==id:

                        if presenty=='P':
                            present+=1
                        else:
                            absent+=1

            per=round((present/len(attendance))*100)

            print(f"| {id} | {name} | {present} | {absent} | {per}% |")

        print('-'*90)

    elif choice == '8':

        print("\nStudents Having Attendance Above 75%")

        dic={}

        for id,name in students.items():

            present=0

            for data in attendance.values():

                for roll,presenty in data.items():

                    if roll==id and presenty=='P':
                        present+=1

            per=round((present/len(attendance))*100)
            dic[id]=per

        for roll,percentage in dic.items():

            if percentage>=75:

                print(f"Name : {students[roll]} | Roll No : {roll} | Attendance : {percentage}%")

    elif choice == '9':

        dic={}

        for roll,name in students.items():

            present=0

            for data in attendance.values():

                for id,presenty in data.items():

                    if id==roll and presenty=='P':
                        present+=1

            per=round((present/len(attendance))*100)
            dic[roll]=per

        topper=max(dic.values())

        print("\nTop Attendance Student")

        for roll,percentage in dic.items():

            if percentage==topper:

                print(f"Name : {students[roll]} | Roll No : {roll} | Attendance : {percentage}%")

    elif choice == '0':

        print("\nThank You For Using SAS Student Attendance System")
        break

    else:

        print("Invalid Choice! Please Try Again.")
