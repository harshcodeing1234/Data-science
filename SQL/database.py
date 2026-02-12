import mysql.connector #type:ignore
import pandas as pd #type:ignore
try:
    # Connect to sql
    conn = mysql.connector.connect(
        host= 'localhost',
        username= 'root',
        password='welcome@123',
        database='collage'
    )

     
    cursor = conn.cursor(buffered=True)
    print('Database connected successfully')


    # create table
    table = """
    create table if not exists students (
    std_id int auto_increment primary key,
    name varchar(50),
    age int,
    course varchar(50),
    cgpa float not null
    );
    """

    cursor.execute(table)
    conn.commit()

    
    while True:
        print("-------Student database menue:--------\n")
        print('1.Insert Record')
        print('2.View Record')
        print('3:Update Record')
        print('4.Delete Record')
        print('5.Exit')

        choice = input('Enter choice:')

        # insert record 
        if choice == '1':
            Name = input('Name:')
            Age = int(input('Age:'))
            Course = input('Course:')
            Cgpa = float(input('Cgpa:'))

            sql = "insert into students (name,age,course,cgpa) values(%s,%s,%s,%s)"
            values = (Name,Age,Course,Cgpa)

            cursor.execute(sql,values)
            conn.commit()

            print('Record Insert successfully')
        
        # View Record
        elif choice == '2':
            cursor.execute('SELECT * FROM students;')
            records = cursor.fetchall()

            df = pd.DataFrame(records,columns=['ID','Name','Age','Course','Cgpa'])
            df.to_excel('student_information.xlsx',index=False)
            print(df)
            

            print('\n\n\n')
        
        # Update Record
        elif choice == '3':
            Id = input('Enter std_id:')
            name = input('Enter your updated Name if not update write same name:')
            age = int(input('Enter your updated age if not update write same age:'))
            course = input('Enter your updated course if not update write same course:')
            cgpa = float(input('Enter your cgpa if not update write same cgpa:'))

            update = "update students set name=%s, age=%s, course=%s, cgpa=%s where std_id = %s"
            value = (name,age,course,cgpa,Id)

            cursor.execute(update,value)
            conn.commit()

            print('Record update successfully\n')
        
        # Delete Record
        elif choice == '4':
            Id = int(input('Enter std_id:'))
            cursor.execute('delete from students where std_id = %s',(Id,))
            conn.commit()

            print('Record delete successfully\n')


        # Exit from loop
        elif choice == '5':
            break 

        else:
            print('Invalid choice')
except Exception as e:
    print(e)