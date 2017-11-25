from django.http import HttpResponse
import time
import json
# data={"data":[]}
data=[]
def read_settings():
    with open('movesensor/config.json','r') as f:
        settings=json.load(f)
    return settings

def save_settings(settings):
    with open('movesensor/config.json','w') as f:
        json.dump(settings,f)

def get_sensor_data(request):
    if request.method!='POST':
        return HttpResponse(status=405)
    print(str(request.body))
    acc=request.body.decode()
    # acc=acc[4:].split(',')
    # t['ax'],t['ay'],t['az']=acc
    t=json.loads(request.body.decode())
    t['type']='a'
    save_data(t,data)
    return HttpResponse(status=200)

def get_angular_v(request):
    if request.method!='POST':
        return HttpResponse(status=405)
    # print(str(request.body))
    acc=request.body.decode()
    # acc=acc[4:].split(',')
    # t['ax'],t['ay'],t['az']=acc
    t=json.loads(request.body.decode())
    t['type']='w'
    save_data(t,data)
    return HttpResponse(status=200)

def save_data(one_data,data):
    settings=read_settings()
    one_data['time']=time.time()
    # with open('data/'+settings['name']+'.json','r') as f:
    #     data=json.load(f)
    if settings['save']:
        settings['num']-=1
        print(str(settings['num'])+" rest")
        # data['data'].append(one_data)
        data.append(one_data)
        if settings['num']<=0:
            settings['save']=False
            settings['num']=0
            with open('data/'+settings['name']+'.json','w') as f:
                json.dump(data,f)
            data=[]
        save_settings(settings)

    # print(one_data)
    # print((data[-1]['time']-data[0]['time'])/len(data))




# read_settings()