# Using locust 2.25 python 3.8.10
# Ref: https://www.cybrosys.com/blog/odoo-database-load-testing-using-locust
import random
import datetime
from locust import task, between
from OdooLocust.OdooLocustUser import OdooLocustUser


class Employee(OdooLocustUser):
    wait_time = between(0.1, 10)
       
    port = 8016
    database = "odoo16"
    login = "admin"
    password = "admin"
    protocol = "jsonrpc"

    @task(10)
    def attend(self):
        """Random employee attends"""
        # 1. Pick random employee
        emp_model = self.client.get_model('hr.employee')
        emp_ids = emp_model.search([])
        emp_id = random.choice(emp_ids)

        # 2. Attend
        att_model = self.client.get_model('hr.attendance')
        att_id = att_model.create({
            'employee_id': emp_id,
            'check_in': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            })


