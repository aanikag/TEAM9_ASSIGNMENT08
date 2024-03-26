# Name: Aanika Garre, Cian Roopnarine, & Connor Laughlin
# email: garreaa@mail.uc.edu, roopnacn@mail.uc.edu, laughlcd@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/28/2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment focuses on collaboration, using GitHub, and connecting to a database in Microsoft
#SQL Server Studio.

# Brief Description of what this module does: This module focuses on accessing data in SQL Server Studio and running SQL queries to output data
#in Eclipse.
# Citations:
# Anything else that's relevant:

#main.py

from connectPackage.connect import *

if __name__ == "__main__":
    print("The below employees work in the Amelia store location and are ordered by their total transactions from least to greatest:")
    for LastName, FirstName, EmployeeTransactions in employeeList:
        print("Name:", FirstName + " " + LastName + "; " + "Total Transactions:", EmployeeTransactions)
