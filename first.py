# Akshat Shah- 1002156388
# Kintur Shah- 1002178072

import pymysql
# Database connection parameters for a remote MySQL server
db_params = {
    'host': 'academicmysql.mysql.database.azure.com',
    'user': 'ass6388',
    'password': 'Naakehvaay!28',
    'database': 'ass6388',
}
try:
    connection = pymysql.connect(**db_params)
    cursor = connection.cursor()
    #Question 5(1)
    insert_query_1 = "INSERT INTO CUSTOMERS (Bank_ID, C_SSN, F_name, Mid_Ini, L_Name, C_Address) VALUES (2,'030-30-3033','Adriana','D','Shah','404 Border Apt,Arlington');"
    insert_query_1 = "INSERT INTO ACCOUNT (Account_num, Balance, Last_Access_Date, Account_Type, OverDraft, Intrest_Rate) VALUES ('BUS300021',500000.00,'2024-08-26 15:00:00','Business',NULL,NULL);"
    insert_query_1 = "INSERT INTO BUSINESS (C_SSN, Business_Name, Address, Account_num) VALUES ('030-30-3033','Adriana Enterprise','404 E Boder street','BUS300021');"

    cursor.execute(insert_query_1)
    connection.commit()

    # Question 5(2)
    # insert_query_2 = "INSERT INTO CUSTOMERS (Bank_ID, C_SSN, F_name, Mid_Ini, L_Name, C_Address) VALUES (2,'040-40-4044','Akshat','S','Shah','4040 Border Apt,Arlington');"
    # insert_query_2 = "INSERT INTO ACCOUNT (Account_num, Balance, Last_Access_Date, Account_Type, OverDraft, Intrest_Rate) VALUES ('SAV100022',1000.00,'2024-08-26 16:00:00','Savings',200,NULL);"
    # insert_query_2= "INSERT INTO INDIVIDUALS (C_SSN, SavingsFlag, Intrest_Rate, CheckingFlag, OverDraft, Account_num, I_SSN) VALUES ('040-40-4044', '1', NULL, '0', 500.00, 'SAV100022', '040-40-4044')"

    # cursor.execute(insert_query_2)
    # connection.commit()

    #Question 5(3)
    # insert_query_3= "INSERT INTO LOAN(Branch_name, Loan_Amount, Loan_Num, Loan_Type,C_SSN) VALUES ('Perth Central Branch',20000.00,21,'Housing Loan','020-20-2022');"

    # cursor.execute(insert_query_3)
    # connection.commit()

    print("Data uploaded successfully.")
    
except Exception as e:
    print(f"Error: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()