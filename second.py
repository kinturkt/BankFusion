# Akshat Shah- 1002156388
# Kintur Shah- 1002178072

import datetime
import pymysql
from dateutil.relativedelta import *
# Database connection parameters for a remote MySQL server
db_params = {
    'host': 'academicmysql.mysql.database.azure.com',
    'user': 'ass6388',
    'password': 'Naakehvaay!28',
    'database': 'ass6388',
}
try:
    now=datetime.datetime.now()
    recent_access_time=now.strftime("%Y-%m-%d %H-%M-%S")

    connection = pymysql.connect(**db_params)
    cursor = connection.cursor()

    query_1="SELECT B.Bank_Id,B.B_Name,Br.City FROM BANK B JOIN Branch Br ON B.Bank_Id=Br.Bank_Id"
    cursor.execute(query_1)
    connection.commit()
    record = cursor.fetchall()

    print('Welcome To One Step Banking Solution')

    choice=int(input('What do you want to do today \n 1. Open A New Account And Deposit Money \n 2.Want to take a loan \n 3.Repay the due amount'))
    F_name=input('Enter Your first Name:')
    mid_ini=input('Enter Your Intial for Middle Name:')
    L_name=input('Enter Your Last Name:')
    Cus_SSN=input('Enter Your SSN Number:')
    if choice==1:
        print('For opening a new Account You have to enter the following values:')
        for values in record:
            print('Bank_Id:',values[0],',','Bank_Name:',values[1],',','City:',values[2])
        Bank_Id=int(input('Select the Bank From the Bank Id in which you want to open your account:'))
        Address=input('Enter Your Address:')
        Type_of_acc=int(input('Enter Which type of account you want (Just enter the choice number): \n 1.Individual \n 2.Business \n'))
        if Type_of_acc==1:
            Type_of_account='Individual'
            Type_of_I_acc=int(input('Enter which type of Individual Account you want (Just enter the choice number):\n 1.Checking \n 2.Savings'))
            Balance=float(input('How much money you want to deposit:'))
            if Type_of_I_acc==1:
                count=2
                account_subtype='Checking'
                Account_num='CHK3000'+str(26)
                Intrest_rate=1.5
                overdraft= None
                C_Flag=1
                S_Flag=None
                count+=1
            elif Type_of_I_acc==2:
                account_subtype='Savings'
                Account_num='SAV3000'+str(27)
                overdraft=(20*Balance)//100
                Intrest_rate=None
                S_Flag=1
                C_Flag=None
        else:
            countb=24
            countb=countb+1
            Type_of_account='Business'
            account_subtype='Business'
            Intrest_rate=None
            overdraft= None
            Account_num='BUS3000'+str(28)
            B_name=input('Enter the Name of your Business:')
            B_Address=input('Enter the address of your business place:')
            Balance=float(input('How much money you want to deposit:'))

        if Type_of_acc==1:
            insert_query_1 = "INSERT INTO CUSTOMERS (Bank_ID, C_SSN, F_name, Mid_Ini, L_Name, C_Address) VALUES (%s,%s,%s,%s,%s,%s)"
            insert_query_2 = "INSERT INTO ACCOUNT (Account_num, Balance, Last_Access_Date, Account_Type, OverDraft, Intrest_Rate) VALUES (%s,%s,%s,%s,%s,%s);"
            insert_query_3 = "INSERT INTO INDIVIDUALS (C_SSN,SavingsFlag,Intrest_Rate,CheckingFlag,OverDraft,Account_num,I_SSN) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(insert_query_1,(Bank_Id,Cus_SSN,F_name,mid_ini,L_name,Address))
            connection.commit()
            print('query-1 run')
            cursor.execute(insert_query_2,(Account_num,Balance,recent_access_time,account_subtype,overdraft,Intrest_rate))
            connection.commit()
            print('query-2 run')
            cursor.execute(insert_query_3,(Cus_SSN,S_Flag,Intrest_rate,C_Flag,overdraft,Account_num,Cus_SSN))
            connection.commit()
            print('query-3 run')

        elif Type_of_acc==2:
            insert_query_1 = "INSERT INTO CUSTOMERS (Bank_ID, C_SSN, F_name, Mid_Ini, L_Name, C_Address) VALUES (%s,%s,%s,%s,%s,%s)"
            insert_query_2 = "INSERT INTO ACCOUNT (Account_num, Balance, Last_Access_Date, Account_Type, OverDraft, Intrest_Rate) VALUES (%s,%s,%s,%s,%s,%s);"
            insert_query_3 = "INSERT INTO BUSINESS (C_SSN,Business_Name,Address,Account_num) VALUES (%s,%s,%s,%s)"
            cursor.execute(insert_query_1,(Bank_Id,Cus_SSN,F_name,mid_ini,L_name,Address))
            connection.commit()
            print('query-1 run')
            cursor.execute(insert_query_2,(Account_num,Balance,recent_access_time,account_subtype,overdraft,Intrest_rate))
            connection.commit()
            print('query-2 run')
            cursor.execute(insert_query_3,(Cus_SSN,B_name,B_Address,Account_num))
            connection.commit()
            print('query-3 run')
    
    if choice==2:
        l_num=17
        c_Id=117
        print('For getting a loan You have to enter the following values:')
        for values in record:
            print('Bank_Id:',values[0],',','Bank_Name:',values[1],',','City:',values[2])
        Bank_Id=int(input('Select the Bank From the Bank Id in which you want to open your account: '))

        Select_query_1=f"SELECT * FROM BRANCH WHERE Bank_Id={Bank_Id}"
        cursor.execute(Select_query_1)
        connection.commit()
        record_1 = cursor.fetchall()
        for i in record_1:
            print("Branch Name=",i[0],",","City=",i[1])
        
        Branch_city=input('Enter the city of the branch you want to take a loan')
        Select_query_3=f"SELECT * FROM BRANCH WHERE city='{Branch_city}'"
        cursor.execute(Select_query_3)
        connection.commit()
        record_4 = cursor.fetchall()
        for i in record_1:
            Branch_name=i[0]
        
        Loan_amt=float(input("Enter your Loan Amount: "))
        Loan_type=input("Enter Type Of Loan (EG: Home Loan,Car Loan etc..): ")
        Installmeants=int(input("In How many instalments you want to repay the loan"))
        Instalmenat_amount=(Loan_amt/Installmeants)
        Instalment_date=now + relativedelta(months=+1)
        payment_date=Instalment_date.strftime("%Y-%m-%d %H:%M:%S")

        Select_query_2=f"SELECT * FROM EMPLOYEES WHERE Bank_Id={Bank_Id} limit 1 "
        cursor.execute(Select_query_2)
        connection.commit()
        record_2 = cursor.fetchall()
        for i in record_2:
            Employee_ssn= i[0]
            p_banker= i[4]

        insert_query_1="INSERT INTO LOAN (Branch_name, Loan_Amount, Loan_Num, Loan_Type,C_SSN) VALUES (%s,%s,%s,%s,%s)"
        insert_query_2="INSERT INTO PERSONAL_BANKER (Loan_Num, E_SSN, Customer_ID) VALUES (%s,%s,%s)"
        insert_query_4="INSERT INTO LOAN_PAYMENT(Loan_Num, Amount, Payment_Num, Date) VALUES(%s,%s,%s,%s)"
        cursor.execute(insert_query_1,(Branch_name,Loan_amt,l_num,Loan_type,Cus_SSN))
        connection.commit()
        print('query-1 run')

        cursor.execute(insert_query_2,(l_num,Employee_ssn,c_Id))
        connection.commit()
        print('query-2 run')

        cursor.execute(insert_query_4,(l_num,Instalmenat_amount,l_num,payment_date))
        connection.commit()
        print('query-3 run')
        l_num+=1
        c_Id+=1

    if choice==4:
        Select_query_1=f"SELECT * FROM LOAN WHERE C_SSN='{Cus_SSN}'"
        cursor.execute(Select_query_1)
        connection.commit()
        record_1 = cursor.fetchall()

        for i in record_1:
            pay_num=i[2]
        
        Select_query_2=f"SELECT * FROM LOAN_PAYMENT WHERE PAYMENT_NUM={pay_num}"
        cursor.execute(Select_query_2)
        connection.commit()
        record_2 = cursor.fetchall()
        print('Your Name:',F_name+' '+mid_ini+' '+L_name,'\n','Your SSN Number:',Cus_SSN)
        for i in record_2:
            print('Loan_num=',i[0],'\n','payment_Due=',i[1],'\n','Due Date=',i[3])
        pay=int(input('You want to repay the full due amount (press 1 for yes and 2 for no):'))
        if (pay==1):
            Update_query_1=f"UPDATE LOAN_PAYMENT SET AMOUNT= 0 WHERE PAYMENT_NUM={pay_num}"
            cursor.execute(Update_query_1)
            connection.commit()
        else:
            print('Thankyou for contacting One Step Banking Solution')
        


except Exception as e:
    print(f"Error: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()


    
    # connection = pymysql.connect(**db_params)
    # cursor = connection.cursor()