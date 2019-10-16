#################################################
#                                               #
# MultiUserComputationProgram Threader          #
#                                               #
# Developed by Mikey Herbert 08oct19 - xxxxxxx  #
# State: PRE-ALPHA 0.2                          #
#################################################

import urllib.request  as ur
import urllib.parse as up
import json
import threading

def get_calcs():
    url = "http://development.sherbernog.ml/mucp_backend/brick.php"
    payload = up.urlencode({'reason':'newcalcs'}).encode("UTF-8")
    url_response = ur.urlopen(url, payload).read().decode("UTF-8")
    json_response = json.loads(url_response)
    return json_response

def split_calcs(to_split):
    a=1
    for index in range(0,len(to_split)):
        if a == 1:
            job_thread1.queue.append(to_split[0])
            to_split.pop(0)
            a=2
        elif a == 2:
            job_thread2.queue.append(to_split[0])
            to_split.pop(0)
            a=3
        elif a == 3:
            job_thread3.queue.append(to_split[0])
            to_split.pop(0)
            a=4
        elif a == 4:
            job_thread4.queue.append(to_split[0])
            to_split.pop(0)
            a=1

class CalcThread:
    def __init__(self, number):
        self.number = number
        self.active = False
        self.num1 = 0
        self.num2 = 0
        self.operator = ''
        self.result = 0
        self.currentClient = 0
        self.responseReady = 0
        self.response = None
        self.queue = []
        self.calcID = ''

    def calc(self):
        if self.operator == 'sqr':
            self.result = self.num1**2
            print('Result: ' + str(self.result))
            self.send_response()
            self.queue.remove[0]
            self.interpret_next_queued()
        elif self.operator == 'cub':
            self.result = self.num1**3
            print('Result: ' + str(self.result))
            self.send_response()
            self.queue.remove[0]
            self.interpret_next_queued()
        elif self.operator == 'add':
            self.result = self.num1 + self.num2
            print('Result: ' + str(self.result))
            self.send_response()
            self.queue.remove[0]
            self.interpret_next_queued()
        elif self.operator == 'sub':
            self.result = self.num1-self.num2
            print('Result: ' + str(self.result))
            self.send_response()
            self.queue.remove[0]
            self.interpret_next_queued()
        elif self.operator == 'mul':
            self.result = self.num1 * self.num2
            print('Result: ' + str(self.result))
            self.send_response()
            self.queue.remove[0]
            self.interpret_next_queued()
        elif self.operator == 'div':
            self.result = self.num1/self.num2
            print('Result: ' + str(self.result))
            self.send_response()
            self.queue.remove[0]
            self.interpret_next_queued()
        else:
            return None

    def interpret_next_queued(self):
        next_p = self.queue[0]
        self.operator = next_p['operator']
        self.currentClient = next_p['clientID']
        self.num1 = float(next_p['num1'])
        self.num2 = float(next_p['num2'])
        self.calcID = next_p['calcID']
        self.print_vals()
        self.calc()

    def print_vals(self):
        print('calcID: '+self.calcID)
        print('num1: '+str(self.num1))
        print('num2: '+str(self.num2))
        print('op: '+str(self.operator))
        print('clientID: '+str(self.currentClient))

    def send_response(self):
        url = "http://development.sherbernog.ml/mucp_backend/brick.php"
        sql = 'UPDATE MUCP SET result='+str(self.result)+', resolved=1 WHERE calcID='+self.calcID
        print(sql)
        payload = up.urlencode({'reason':'sendresponse', 'sql':sql}).encode("UTF-8")
        url_response = ur.urlopen(url, payload).read().decode("UTF-8")
        print(url_response)
        json_response = json.loads(url_response)
        return json_response
        
        
job_thread1 = CalcThread(1)
job_thread2 = CalcThread(2)
job_thread3 = CalcThread(3)
job_thread4 = CalcThread(4)

if __name__ == '__main__':
    if job_thread1.queue == []:
        split_calcs(get_calcs())
    


