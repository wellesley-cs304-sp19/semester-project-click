#CS304 Project
#Dana, Erica, and Gabby

import sys
import MySQLdb

'''our clickdb connection'''
def getConn(db):
    conn = MySQLdb.connect(host='localhost',
                           user='ubuntu',
                           passwd='',
                           db=db)
    conn.autocommit(True)
    return conn


#get all student's skills from database    
<<<<<<< HEAD

import threading
from connection import getConn


=======
import threading
from connection import getConn
import re
>>>>>>> 83ff4049c0cd53beb03af46781f41625937ed593

'''Gets student's information (name, email) from database'''
def getStudent(conn, email):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''Select name, email, active from user where email = %s''', [email])
    return curs.fetchone()

'''Returns results of SQL query to get student's skills from the database'''   
def studentSkills(conn, email):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    #use inner join to get list of skills
    curs.execute('''select skill from skills inner join hasSkill using (sid)
    where hasSkill.email = %s''', [email])
    return curs.fetchall()
    
<<<<<<< HEAD

=======
#removes skill from student  
def removeSkill(conn, email, skill):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''Select sid from skills where skill = %s''', [skill])
    skillNum = curs.fetchone().values()[0]
    nr = curs.execute('''delete from hasSkill where sid = %s and email = %s''', [skillNum, email])
    return nr

#adds skill to student    
>>>>>>> 83ff4049c0cd53beb03af46781f41625937ed593
'''Removes skill from student'''  
def removeSkill(conn, email, skill):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    nr = curs.execute('''delete from hasSkill where sid = 
    (select sid from skills where skill = %s) and email = %s''', [skill, email])
    return nr

'''Adds skill to student'''    
<<<<<<< HEAD

=======
>>>>>>> 83ff4049c0cd53beb03af46781f41625937ed593
def addSkill(conn, email, skill):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)

    curs.execute('''Select sid from skills where skill = %s''', [skill])
<<<<<<< HEAD

=======
>>>>>>> 83ff4049c0cd53beb03af46781f41625937ed593
    skillNum = curs.fetchone()
    #if skill not in skills table, add it
    if skillNum == None:
        curs.execute('''insert into skills(skill) values (%s)''', [skill])
        curs.execute('''Select sid from skills where skill = %s''', [skill])
        skillNum = curs.fetchone()
    #continue with inserting email and skill into hasSkill table
    nr = curs.execute('''insert into hasSkill(email, sid) values (%s, %s)''', [email, skillNum.values()[0]])
    return nr
    
<<<<<<< HEAD

=======
>>>>>>> 83ff4049c0cd53beb03af46781f41625937ed593
    skillQuery = curs.fetchone() #stores results from query to get skills
    #if skill not in skills table, add it
    if skillQuery == None:
        curs.execute('''insert into skills(skill) values (%s)''', [skill])
        curs.execute('''select last_insert_id()''')
        skillNum = curs.fetchone()['last_insert_id()']
    else:
        skillNum = skillQuery['sid'] #set skillNum to sid from skillQuery
    #continue with inserting email and skill into hasSkill table
    nr = curs.execute('''insert into hasSkill(email, sid) values (%s, %s)''', [email, skillNum])
    return nr


########################GAB'S Functions
 
'''Update student's name, email, and/or active status'''
def updateStudentProfile(conn, oldEmail, newEmail, newName, newActive):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    nr = curs.execute('''update user
                    set email = %s, name = %s, active = %s where email = %s''',
                    [newEmail, newName, newActive, oldEmail])
    return nr
    
'''Get all jobs in the database'''
def getJobs(conn):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''select pid, name, minHours, pay, location from project''')
    return curs.fetchall()
    
def searchJobs(conn, search):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''select pid, name, minHours, pay, location from project
                    where name like %s''', ['%'+ search + '%'])
    return curs.fetchall()
<<<<<<< HEAD
    
=======
>>>>>>> 83ff4049c0cd53beb03af46781f41625937ed593

#adds a new user
def addUser(conn,email,password):
    curs=conn.cursor()
    newrow=curs.execute('''insert into user(email,password) values (%s,%s)''',[email,password])
    return newrow
    
<<<<<<< HEAD

#put rest of our functions here


#get info about a project 
def getProject(conn, pid):
=======
#put rest of our functions here


#get info about a posting 
def getPosting(conn, pid):
>>>>>>> 83ff4049c0cd53beb03af46781f41625937ed593
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''Select * from project where pid = %s''', [pid])
    return curs.fetchone()
   
#SQL query to get pid, name, pay, minimum hours, location from project table using the pid    

<<<<<<< HEAD
def search_project_pid(conn, pid): 
=======

def search_posting_pid(conn, pid): 

>>>>>>> 83ff4049c0cd53beb03af46781f41625937ed593
    curs = conn.cursor()
    curs.execute('''select pid,name,pay,minHours,
    location from project where pid = %s;''',
                    [pid])
    return curs.fetchone()  

<<<<<<< HEAD
#SQL code to insert project using pid, name, pay, minimum hours, location    
def insert_project(conn, pid, name, pay, minHours, location): 
    curs = conn.cursor()
    curs.execute('''insert into project(pid,name,minHours, location) values (%s,%s,%s, %s);''',
                    [pid,name,minHours,location])
    return curs
  

=======



#SQL code to insert posting using pid, name, pay, minimum hours, location    
def insert_posting(conn, pid, name, pay, minHours, location): 
    curs = conn.cursor()
    curs.execute('''insert into posting(pid,name,minHours, location)
values (%s,%s,%s, %s);''',
                    [pid,name,minHours,location])
    return curs
  
>>>>>>> 83ff4049c0cd53beb03af46781f41625937ed593
#SQL query to get a list of all current projects    
def find_allProjects(conn):
    curs = conn.cursor()
    curs.execute('''select pid,name,pay,minHours, 
    location from project;''')
    allProjects = curs.fetchall()
    return allProjects;

<<<<<<< HEAD
def getStudents(conn):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''select email, name, active, userType from project''')
    return curs.fetchall()
    
def searchStudents(conn, search):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('''select email, name, active, userType from project
                    where name like %s''', ['%'+ search + '%'])
    return curs.fetchall()
=======
#SQL query to get a list of all current postings    
def find_allPostings(conn):
    curs = conn.cursor()
    curs.execute('''select pid,name,pay,minHours, 
    location from project;''')
    allPostings = curs.fetchall()
    return allPostings;
>>>>>>> 83ff4049c0cd53beb03af46781f41625937ed593


#add a new job posting
def addProject(conn,project_dict):
    curs = conn.cursor()
    curs.execute('''insert into project (name,minHours,pay,location) values (%s,%s,%s,%s);''',[project_dict['name'],project_dict['minHours'],project_dict['pay'],project_dict['location']])
    curs.execute('''select last_insert_id();''')
    result=curs.fetchall()
    return(result[0][0])


#SQL query to get specifically email of a student with a given name 
def get_email(conn, name):
    curs = conn.cursor()
    curs.execute('''select email from user where name like %s;''', [name + '%'])
    email = curs.fetchone()
    return email[0]

<<<<<<< HEAD
=======
   
if __name__ == '__main__':
    conn = getConn('clickdb')
    #addSkill(conn, "student2@gmail.com", "editing")
    #print(removeSkill(conn, "student1@gmail.com", "math tutoring"))
    #studentSkills(conn, "student1@gmail.com")

>>>>>>> 83ff4049c0cd53beb03af46781f41625937ed593

   
if __name__ == '__main__':
    conn = getConn('clickdb')
    #addSkill(conn, "student2@gmail.com", "public speaking")
    #print(removeSkill(conn, "student1@gmail.com", "math tutoring"))
    #print(studentSkills(conn, "student1@gmail.com"))

