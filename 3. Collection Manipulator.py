print("\nWelcome to the Student Data Organizer !")


STUDENT_ID = ''
STUDENT_NAME = ''
STUDENT_AGE = ''
STUDENT_GRADE = ''
STUDENT_DOB = ''
STUDENT_SUBJECT = ''

ALL_INFORMATION = [ ]
L1 = [ ]





while True :



    choice = int(input("""\n\n Select an options :  \n
            1. Add Students
            2. Display Students
            3. Update Students
            4. Delete Students
            5. Display Subject Offer  
            6. Exit  \n
            Enter your choice : """))



    if ( choice == 1 ) :



        while True :

            Student_ID = input("\n\n\t    Enter the Student ID : ")

            if ( Student_ID.isdigit() ) :

                STUDENT_ID = Student_ID
                break

            else :
                print("\n Please enter the valid Student ID !...")



        while True :

            Student_name = input("\n\n\t    Enter the Student Name : ")

            if ( Student_name.isalpha() ) :

                STUDENT_NAME = Student_name
                break

            else :
                print("\n Please enter the valid Student Name !...")



        while True :

            Student_age = input("\n\n\t    Enter the Student Age : ")

            if ( Student_age.isdigit() ) :

                STUDENT_AGE = Student_age
                break

            else :
                print("\n Please enter the valid Student Age !...")



        while True :

            Student_grade = input("\n\n\t    Enter the Student Grade : ")

            if ( Student_grade  in  ['A+' , 'A' , 'B+' , 'B' , 'C+' , 'C' , 'D' , 'F'] ) :

                STUDENT_GRADE = Student_grade
                break

            else :
                print("\n Please enter the valid Student Grade !...")



        while True :

            Student_dob = input("\n\n\t    Enter the Student DOB ( YYYY-MM-DD ) : ")

            STUDENT_DOB = Student_dob
            break



        while True : 

            Student_subject = input("\n\n\t    Enter the Student Subject ( 1.Math , 2. English , 3.Science ) : ")


            if ( Student_subject == '1' ) :

                Subject = 'Math'

                print("\n\n The Student is Successfully Added !...")
                print("\n\n" , "*" * 100)                
                break

            elif ( Student_subject == '2' ) :

                Subject = 'English'

                print("\n\n The Student is Successfully Added !...")
                print("\n\n" , "*" * 100)
                break

            elif ( Student_subject == '3' ) :

                Subject = 'Science'

                print("\n\n The Student is Successfully Added !...")
                print("\n\n" , "*" * 100)
                break

            elif ( Student_subject == '1,2' ) :

                Subject = 'Math and English'

                print("\n\n The Student is Successfully Added !...")
                print("\n\n" , "*" * 100)
                break

            elif ( Student_subject == '2,3' ) :

                Subject = 'English and Science'

                print("\n\n The Student is Successfully Added !...")
                print("\n\n" , "*" * 100)
                break

            elif ( Student_subject == '3,1' ) :

                Subject = 'Science and Math'

                print("\n\n The Student is Successfully Added !...")
                print("\n\n" , "*" * 100)
                break

            elif ( Student_subject == '1,2,3' ) :

                Subject = 'Math , English and Science'

                print("\n\n The Student is Successfully Added !...")
                print("\n\n" , "*" * 100)
                break

            else :

                print("\n Please enter the valid input !...")




        ALL_INFORMATION.append({
            'Student ID' : Student_ID ,
            'Student Name' : Student_name ,
            'Student Age' : Student_age ,
            'Student Grade' : Student_grade ,
            'Student DOB' : Student_dob , 
            'Student Subject' : Subject
            })




    elif ( choice == 2 ) :


        for i in ALL_INFORMATION :
            print("\n\n Student ID :" , i['Student ID'])
            print(" Student Name :" , i['Student Name'])
            print(" Student Age :" , i['Student Age'])
            print(" Student Grade :" , i['Student Grade'])
            print(" Student DOB :" , i['Student DOB'])
            print(" Student Subject :" , i['Student Subject'])

            print("\n\n" , "*" * 100)




    elif ( choice == 3 ) :


        Check_Student_ID = input("\n\n\t    Enter the Student ID which you want to Update : ")


        if ( Check_Student_ID.isdigit() ) :

            for i in ALL_INFORMATION :
                if ( i['Student ID'] == Check_Student_ID ) :


                    Update_student_ID = i['Student ID']
                    Update_student_name = i['Student Name']
                    Update_student_age = i['Student Age']
                    Update_student_grade = i['Student Grade']
                    Update_student_dob = i['Student DOB']
                    Update_student_subject = i['Student Subject']


                    while True : 

                        update_choice = input("""\n\n\t    Select an option : \n
                                1. Update Student ID
                                2. Update Student Name 
                                3. Update Student Age 
                                4. Update Student Grade 
                                5. Update Student DOB 
                                6. Update Student Subject
                                7. Exit    \n
                                Enter your choice : """)



                        if ( update_choice == '1' ) :

                            while True :

                                Update_student_ID = input("\n\n\t    Enter the Student ID to Update : ")

                                if ( Update_student_ID.isdigit() ) :

                                    # STUDENT_ID = Update_student_ID
                                    break

                                else :
                                    print("\n Please enter the valid Student ID !...")



                        elif ( update_choice == '2' ) :

                            while True :

                                Update_student_name = input("\n\n\t    Enter the Student Name to Update : ")

                                if ( Update_student_name.isalpha() ) :

                                    STUDENT_NAME = Update_student_name
                                    break

                                else :
                                    print("\n Please enter the valid Student Name !...")



                        elif ( update_choice == '3' ) :

                            while True :

                                Update_student_age = input("\n\n\t    Enter the Student Age to Update : ")

                                if ( Update_student_age.isdigit() ) :

                                    STUDENT_AGE = Update_student_age
                                    break

                                else :
                                    print("\n Please enter the valid Student Age !...")



                        elif ( update_choice == '4' ) :

                            while True :

                                Update_student_grade = input("\n\n\t    Enter the Student Grade to Update : ")

                                if ( Update_student_grade  in  ['A+' , 'A' , 'B+' , 'B' , 'C+' , 'C' , 'D' , 'F'] ) :

                                    STUDENT_GRADE = Update_student_grade
                                    break

                                else :
                                    print("\n Please enter the valid Student Grade !...")



                        elif ( update_choice == '5' ) :

                            while True :

                                Update_student_dob = input("\n\n\t    Enter the Student DOB ( YYYY-MM-DD ) to Update : ")

                                STUDENT_DOB = Update_student_dob
                                break



                        elif ( update_choice == '6' ) :

                            while True : 

                                Update_student_subject = input("\n\n\t    Enter the Student Subject ( 1.Math , 2. English , 3.Science ) to Update : ")


                                if ( Update_student_subject == '1' ) :

                                    Subject = 'Math'               
                                    break

                                elif ( Update_student_subject == '2' ) :

                                    Subject = 'English'
                                    break

                                elif ( Update_student_subject == '3' ) :

                                    Subject = 'Science'
                                    break

                                elif ( Update_student_subject == '1,2' ) :

                                    Subject = 'Math and English'
                                    break

                                elif ( Update_student_subject == '2,3' ) :

                                    Subject = 'English and Science'
                                    break

                                elif ( Update_student_subject == '3,1' ) :

                                    Subject = 'Science and Math'
                                    break

                                elif ( Update_student_subject == '1,2,3' ) :

                                    Subject = 'Math , English and Science'
                                    break

                                else :

                                    print("\n Please enter the valid input !...")



                        elif ( update_choice == '7' ) :
                            print("\n\n The Student is Successfully Added !...")
                            print("\n\n" , "*" * 100)
                            break



                        else :
                            print("\n Please enter the valid input !...")

                    break


            else :
                print("\n\n This Studen ID is not define !...")


        else :
            print("\n\n Please enter the valid input !...")



        ALL_INFORMATION.append({
            'Student ID' : Update_student_ID ,
            'Student Name' : Update_student_name ,
            'Student Age' : Update_student_age ,
            'Student Grade' : Update_student_grade ,
            'Student DOB' : Update_student_dob , 
            'Student Subject' : Update_student_subject 
        })




    elif ( choice == 4 ) :


        Delete_Student = input("\n\n\t    Enter the Student ID to delete : ")


        if ( Delete_Student.isdigit() ) :

            for i in ALL_INFORMATION :
                if  ( i['Student ID'] == Delete_Student ) :

                    ALL_INFORMATION.remove(i)
                    print("\n\n The Student successfully Deleted !... ")


                    All_Student_Delete = input("\n\n\t    Do you want to Delete the All Students Data ( 1.yes , 2.no ) : ")


                    if ( All_Student_Delete.isdigit() ) :
                    
                        if ( All_Student_Delete == '1' ) :

                            ALL_INFORMATION.clear()
                            print("\n The All Students Data is successfully Deleted !...")
                            print("\n\n" , "*" * 100)

                        elif ( All_Student_Delete == '2' ) :
                            print("\n\n" , "*" * 100)
                            exit

                        else :
                            print("\n Please enter the valid input !...")

                    else :
                        print("\n Please enter the valid input !...")


                break

            else :
                print("\n\n This Student is not define !...")
                print("\n\n" , "*" * 100)

        else :
            print("\n\n Please enter the valid input !...")
            print("\n\n" , "*" * 100)




    elif ( choice == 5 ) :


        Subject_offer =  """\n\t\t1. Math
                2. English
                3. Science"""


        print(Subject_offer)

        print("\n\n These Three Subjects are offer for Students !...")
        print("\n\n" , "*" * 100)




    elif ( choice == 6 ) :

        print("\n Thank You for Student Data Organizer !...")
        break




    elif ( choice == 7 ) :

        print("\n Please enter the valid input !...")