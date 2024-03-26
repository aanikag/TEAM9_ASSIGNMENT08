#connect.py

import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')

cursor = conn.cursor()

cursor.execute('''
                SELECT 
                    [GroceryStoreSimulator].[dbo].[tEmpl].[LastName],
                    [GroceryStoreSimulator].[dbo].[tEmpl].[FirstName],
                    [GroceryStoreSimulator].[dbo].[tEmplTitle].[EmplTitle],
                    [GroceryStoreSimulator].[dbo].[tStore].[Store],
                    COUNT([GroceryStoreSimulator].[dbo].[tTransaction].[EmplID]) AS EmployeeTransactions
                FROM 
                    [GroceryStoreSimulator].[dbo].[tEmpl]
                    JOIN [GroceryStoreSimulator].[dbo].[tStore] ON [GroceryStoreSimulator].[dbo].[tEmpl].[StoreID] = [GroceryStoreSimulator].[dbo].[tStore].[StoreID]
                    JOIN [GroceryStoreSimulator].[dbo].[tEmplTitle] ON [GroceryStoreSimulator].[dbo].[tEmpl].[EmplTitleID] = [GroceryStoreSimulator].[dbo].[tEmplTitle].[EmplTitleID]
                    JOIN [GroceryStoreSimulator].[dbo].[tTransaction] ON [GroceryStoreSimulator].[dbo].[tTransaction].[EmplID] = [GroceryStoreSimulator].[dbo].[tEmpl].[EmplID]
                WHERE
                    [GroceryStoreSimulator].[dbo].[tStore].[Store] = 'Amelia'
                GROUP BY
                    [GroceryStoreSimulator].[dbo].[tStore].[Store], [GroceryStoreSimulator].[dbo].[tEmplTitle].[EmplTitle], [GroceryStoreSimulator].[dbo].[tEmpl].[LastName],[GroceryStoreSimulator].[dbo].[tEmpl].[FirstName]
                ORDER BY
                    COUNT([GroceryStoreSimulator].[dbo].[tTransaction].[EmplID])
                ''')