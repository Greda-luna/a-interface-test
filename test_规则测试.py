import json

import requests

class TestRuleTestAll:
    def setup_class(self):
        self.add_url = 'http://127.0.0.1:8234/api/operator/svcrule/add'
        self.update_url = 'http://127.0.0.1:8234/api/operator/svcrule/modify'
        self.dele_url = 'http://127.0.0.1:8234/api/operator/svcrule/delete'
        self.search_url = 'http://127.0.0.1:8234/api/operator/svcrule/list?pagesize=5&pagenum=1&keywords='
        self.headers = {
            "Authorization": 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOjEsInVzZXJuYW1lIjoiYnloeSIsImV4cCI6MTcxNjY1NDE4MX0.cUXhYxsHGwLIbGl--KX2e_hJjvNMDmUue0VK-HpJV2M',
            'Content-Type':'application/json',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
            'Content-Length':"216"
        }
        #增加规则类型为预付费-下发业务量
        self.charge_rule_data1 = {
                                    "minFee": 10,
                                    "estFee": 100,
                                    "feeRates": [
                                        {
                                          "svcCode": "",
                                          "unitName": "千克",
                                          "unitPrice": 1
                                        }
                              ]
                            }
        self.charge_rule_str1 = json.dumps(self.charge_rule_data1)
        self.add_data_1 = {
            "charge_rule":self.charge_rule_str1,
            "desc":"这是第一个业务规则",
            "name":"下发业务量",
            "rule_type_id":1
        }
        #增加规则类型为预付费-下发费用
        self.charge_rule_data2 = {
                            "minFee": 20,
                            "estFee": 200
                  }
        self.charge_rule_str2 = json.dumps(self.charge_rule_data2)
        self.add_data_2 = {
            "name": "下发费用",
            "rule_type_id": 2,
            "charge_rule":self.charge_rule_str2,
            "desc": "这是第二个业务规则"
        }
        # 增加规则类型为后付费-上报业务量
        self.charge_rule_data3 = {
            "feeRates": [
                {
                    "svcCode": "31",
                    "unitName": "厘米",
                    "unitPrice": 3.1
                },
                {
                    "svcCode": "32",
                    "unitName": "分米",
                    "unitPrice": 3.2
                }
            ]
        }
        self.charge_rule_str3 = json.dumps(self.charge_rule_data3)
        self.add_data_3 = {
            "desc": "这是第三个业务规则",
            "name": "上报业务量",
            "rule_type_id": 3,
            "charge_rule":self.charge_rule_str3
        }

    def test_ruleall(self):
        add_r1 = requests.post(self.add_url,json=self.add_data_1,headers=self.headers)
        assert add_r1.status_code == 200
        add_r2 = requests.post(self.add_url,json=self.add_data_2, headers=self.headers)
        self.id = add_r2.json()["id"]
        print(add_r2.text)
        assert add_r2.status_code == 200
        add_r3 = requests.post(self.add_url,json=self.add_data_3, headers=self.headers)
        self.dele_id = add_r3.json()["id"]
        assert add_r3.status_code == 200
        self.charge_rule_data2_new = {
                            "minFee": 80,
                            "estFee": 800
                  }
        self.charge_rule_str2_new = json.dumps(self.charge_rule_data2_new)
        self.update_data = {
            "name": "下发费用",
            "rule_type_id": 2,
            "charge_rule":self.charge_rule_str2_new,
            "desc": "这是更新后的业务规则",
            "id":self.id
        }
        update_r = requests.put(self.update_url,json=self.update_data,headers=self.headers)
        assert update_r.status_code == 200
        self.dele_data = {
            "id":self.dele_id
        }
        dele_r = requests.delete(self.dele_url,json=self.dele_data,headers=self.headers)
        assert dele_r.status_code == 200


