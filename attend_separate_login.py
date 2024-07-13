# Using locust 2.25 python 3.8.10
# Ref: https://www.cybrosys.com/blog/odoo-database-load-testing-using-locust
import random
import datetime
import odoolib
from locust import task, between
from OdooLocust.OdooLocustUser import OdooLocustUser


class Employee(OdooLocustUser):
    wait_time = between(0.1, 10)
       
    def on_start(self):
        """Prevent login on startup"""
        return True

    @task(10)
    def attend(self):
        """Random user attends with separate login"""
        # 1. Pick random user from users.txt
        with open('users.txt', 'r') as afile:
            emails = afile.read()
        users = emails.split('\n')
        email = random.choice(users)
        while not email:
            email = random.choice(users)
        # 2. Login
        connection = odoolib.get_connection(hostname="localhost", database="odoo16", \
            login=email, password="17 Agustus 1945", protocol="jsonrpc", port=8016)
        # 3. Attend
        att_model = connection.get_model('hr.attendance')
        emp_model = connection.get_model('hr.employee')
        emp_ids = emp_model.search([('work_email', '=', email)])
        for emp_id in emp_ids:
            att_id = att_model.create({
                'employee_id': emp_id,
                'check_in': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                })


