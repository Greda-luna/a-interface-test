import jsonpath
import requests

class Testdeviceall:
    def setup_class(self):
        self.login_url = 'http://127.0.0.1:8234/api/operator_login'
        self.add_url = 'http://127.0.0.1:8234/api/operator/devicemodel/add'
        self.dele_url = 'http://127.0.0.1:8234/api/operator/devicemodel/delete'
        self.update_url = 'http://127.0.0.1:8234/api/operator/devicemodel/modify'
        self.search_url = 'http://127.0.0.1:8234/api/operator/devicemodel/list?pagesize=5&pagenum=1&keywords='
        self.dtype = 1
        self.add_data = {
            "dtypeid": self.dtype,
            "name": "284678",
            "desc": "45678676"
        }

        self.headers = {
            "Authorization":'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOjEsInVzZXJuYW1lIjoiYnloeSIsImV4cCI6MTcxNjY1NDE4MX0.cUXhYxsHGwLIbGl--KX2e_hJjvNMDmUue0VK-HpJV2M'
        }

    def test_device_type_add(self):

        add_r = requests.post(self.add_url,json=self.add_data,headers=self.headers)
        print(add_r.json())
        self.id = add_r.json()["id"]
        self.update_data = {
            "dtypeid": 2,
            "name": "284678",
            "desc": "45678676",
            "id": self.id
        }
        assert add_r.status_code == 200
        update_r = requests.put(self.update_url,json=self.update_data,headers=self.headers)
        print(update_r.json())
        assert update_r.status_code == 200
        self.dele_data = {
            "id":self.id
        }
        delete_r = requests.delete(self.dele_url,json=self.dele_data,headers=self.headers)
        assert delete_r.status_code == 200

