#################################################
#
# MultiUserComputationProgram Threader
#
# Developed by Mikey Herbert 08oct19 - xxxxxxx
# State: PRE-ALPHA 0.1
#################################################

import urllib.request  as ur
import urllib.parse as up
import json
import threading

class calcThread():
    def __init__(self, number):
        self.number = number
        self.active = False
        self.num1 = 0
        self.num2 = 0
        self.operator = ''
        self.result = 0
        self.currentClient = None
        self.responseReady = 0
        self.response = ''

    def calc(self):
        if self.operator == 'sqr':
            self.result = num1**num1
        elif self.operator == 'cub':
            self.result = num1**num1**num1
        elif self.operator == 'add':
            self.result = num1 + num2
        elif self.operator == 'sub':
            self.result = num1-num2
        elif self.operator == 'mul':
            self.result = num1 * num2
        elif self.operator == 'div':
            self.result == num1 / num2
        else:
            return None

    def sendResult(self, endpoint):
        self.url = "http://development.sherbernog.ml/mucp_backend/brick.php" + endpoint
        self.urlresponse = ur.urlopen(self.url).read().decode("UTF-8")
        jsonresponse = json.loads(self.urlresponse)
        print(jsonresponse)

    def jobThread(self, job_func, endpoint):
        job_thread = threading.Thread(target=job_func, args=(endpoint, ))
        job_thread.start()

job_thread = calcThread(1)
