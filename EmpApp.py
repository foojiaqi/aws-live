from flask import Flask, render_template, request
from pymysql import connections
import os

import re
import boto3
from config import *

app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'employee'


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('AddEmp.html')


@app.route("/about", methods=['POST'])
def about():
    return render_template('www.intellipaat.com')


@app.route("/addemp", methods=['POST', 'GET'])
def AddEmp():
    emp_id = request.form['emp_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    pri_skill = request.form['pri_skill']
    location = request.form['location']
    emp_image_file = request.files['emp_image_file']

    insert_sql = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

    if emp_image_file.filename == "":
        return "Please select a file"



    cursor.execute(insert_sql, (emp_id, first_name, last_name, pri_skill, location))
    db_conn.commit()
        # Uplaod image file in S3 #

#put here for copied code


    cursor.close()

    print("all modification done...")
    return render_template('AddEmpOutput.html', name=emp_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

@app.route("/updateemp", methods=['POST'])
def update():
    emp_id = request.form['emp_id']
    update_sql = "UPDATE emp_id FROM employee WHERE emp_id(%s)"
    cursor = db_conn.cursor()
    cursor.execute(update_sql, (emp_id))
    emp_id = re.subs('\W+','', str(cursor.fetchall()))
    first_name = request.form['first_name']
    update_sql = "UPDATE first_name FROM employee WHERE emp_id(%s)"
    cursor = db_conn.cursor()
    cursor.execute(update_sql, (emp_id))
    first_name = re.subs('\W+','', str(cursor.fetchall()))
    last_name = request.form['last_name']
    update_sql = "UPDATE last_name FROM employee WHERE emp_id(%s)"
    cursor = db_conn.cursor()
    cursor.execute(update_sql, (emp_id))
    last_name = re.subs('\W+','', str(cursor.fetchall()))
    pri_skill = request.form['pri_skill']
    update_sql = "UPDATE pri_skill FROM employee WHERE emp_id(%s)"
    cursor = db_conn.cursor()
    cursor.execute(update_sql, (emp_id))
    pri_skill = re.subs('\W+','', str(cursor.fetchall()))
    location = request.form['location']
    update_sql = "UPDATE update_sql FROM employee WHERE emp_id(%s)"
    cursor = db_conn.cursor()
    cursor.execute(update_sql, (emp_id))
    location = re.subs('\W+','', str(cursor.fetchall()))
    emp_image_file = re.subs('\W+','', str(cursor.fetchall()))
    db_conn.commit()
    cursor.close()
    return render_template('')

#below
@app.route("/applyleave", methods=['GET', 'POST'])
def ApplyLeave():
    start_date = request.form['leave_start_date']
    end_date = request.form['leave_end_date']
    reason = request.form['leave_reason']
    eid = request.form['emp_id']
    updateLeave = "update employee set leave_start_date = %s, leave_end_date = %s, leave_reason =%s, leave_status=%s  where emp_id=%s"
    cursor = db_conn.cursor()
    cursor.execute(updateLeave,(start_date,end_date,reason,'pending',eid))
    db_conn.commit()
    return render_template('AddEmp.html')


#below
@app.route("/viewleave", methods=['GET', 'POST'])
def ViewLeave():
    view_leave_emp_id = request.form['view_leave_emp_id']
    view_leave = "Select emp_id, first_name, last_name, leave_start_date, leave_end_date, leave_reason, leave_status from employee where emp_id=%s"
    cursor = db_conn.cursor()
    cursor.execute(view_leave,(view_leave_emp_id))
    view_records = cursor.fetchall()
    db_conn.commit()

    (emp_id, first_name, last_name, leave_start_date, leave_end_date, leave_reason, leave_status)=view_records[0]
    return render_template('ViewApplyLeave.html', emp_id=emp_id, first_name=first_name,last_name=last_name,leave_start_date=leave_start_date, leave_end_date=leave_end_date, leave_reason=leave_reason, leave_status=leave_status)

#below
@app.route("/approveleave", methods=['GET', 'POST'])
def ApproveLeave():
    eid = request.form['emp_id']
    approve_va=request.form['action']
    if approve_va=='Approve':
        lestatus='Approve'
    else:
        lestatus='Reject'
      
    approve_leave = "Update employee set leave_status=%s where emp_id=%s"
    cursor = db_conn.cursor()
    cursor.execute(approve_leave,(lestatus,eid))
    db_conn.commit()
    return render_template('ApproveLeave.html',first_name=approve_va)