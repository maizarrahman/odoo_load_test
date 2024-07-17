from locust import HttpUser, task
import random
import string

class TestLogin(HttpUser):
    @task
    def test_login(self):
        url = 'http://localhost:8016//web/session/authenticate'
        headers = {'Content-Type': 'application/json',}
        data = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'db': 'odoo16',
                'login': ''.join(random.choices(string.ascii_lowercase, k=8)),
                'password': ''.join(random.choices(string.ascii_lowercase, k=8)),
                }
            }
        self.client.post(url, json=data, headers=headers)

