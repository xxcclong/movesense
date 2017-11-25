from django.http import HttpResponse
import time
import json
data=[]

def get_sensor_data(request):
    if request.method!='POST':
        return HttpResponse(status=405)
    print(str(request.body))
    acc=request.body.decode()
    acc=acc[4:].split(',')
    t={}
    t['ax'],t['ay'],t['az']=acc
    # t=json.loads(request.body.decode())
    t['time']=time.time()
    data.append(t)
    # request.b
    # print(data)
    print((data[-1]['time']-data[0]['time'])/len(data))
    return HttpResponse(status=200)