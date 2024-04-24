import requests


res = requests.post("http://172.18.0.3:5000/send_data",
                    params={"temparature": "12",
                          "sensor_name": "431",
                          "timestamp": "234234",
                          "stress_level": "45etgw"})
