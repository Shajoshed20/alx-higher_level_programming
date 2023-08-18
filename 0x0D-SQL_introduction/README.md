# 0x0D. SQL - Introduction

## General Learning Outcomes

* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does DDL and DML stand for
* How to CREATE or ALTER a table
* How to SELECT data from a table
* How to INSERT, UPDATE or DELETE data
* What are subqueries
* How to use MySQL functions

## Tasks

* Task 0 - Write a script that lists all databases of your MySQL server.

* Task 1 - Write a script that creates the database hbtn_0c_0 in your MySQL server.
    * If the database hbtn_0c_0 already exists, your script should not fail
    * You are not allowed to use the SELECT or SHOW statements

* Task 2 - Write a script that deletes the database hbtn_0c_0 in your MySQL server.
    * If the database hbtn_0c_0 doesn’t exist, your script should not fail
    * You are not allowed to use the SELECT or SHOW statements

* Task 3 - Write a script that lists all the tables of a database in your MySQL server.
    * The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)

* Task 4 - Write a script that creates a table called first_table in the current database in your MySQL server.
        - first_table description:
        - id INT
        - name VARCHAR(256)
    * The database name will be passed as an argument of the mysql command
    * If the table first_table already exists, your script should not fail
    * You are not allowed to use the SELECT or SHOW statements

* Task 5 - Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
    * The database name will be passed as an argument of the mysql command
    * You are not allowed to use the DESCRIBE or EXPLAIN statements

* Task 6 - Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
    * All fields should be printed
    * The database name will be passed as an argument of the mysql command

* Task 7 - Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
    * New row:
        * id = 89
        * name = Best School
    * The database name will be passed as an argument of the mysql command

* Task 8 - Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
    * The database name will be passed as an argument of the mysql command

* Task 9 - Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

* Task 10 - Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
    * Results should display both the score and the name (in this order)
    * Records should be ordered by score (top first)
    * The database name will be passed as an argument of the mysql command

* Task 11 - Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
    * Results should display both the score and the name (in this order)
    * Records should be ordered by score (top first)
    * The database name will be passed as an argument of the mysql command

* Task 12 - Write a script that updates the score of Bob to 10 in the table second_table.
    * You are not allowed to use Bob’s id value, only the name field
    * The database name will be passed as an argument of the mysql command

* Task 13 - Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
    * The database name will be passed as an argument of the mysql command

* Task 14 - Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.
    * The result column name should be average
    * The database name will be passed as an argument of the mysql command

* Task 15 - Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
    * The result should display:
        * the score
        * the number of records for this score with the label number
    * The list should be sorted by the number of records (descending)
    * The database name will be passed as an argument to the mysql command

* Task 16 - Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
    * Don’t list rows without a name value
    * Results should display the score and the name (in this order)
    * Records should be listed by descending score
    * The database name will be passed as an argument to the mysql command

* Task 17 - Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

* Task 18 - Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

* Task 19 - Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

* Task 20 - Write a script that displays the max temperature of each state (ordered by State name).