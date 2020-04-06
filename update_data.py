# coding=utf-8
import requests
import json
import datetime
import time

def get_data(url,filename):

    with requests.get(url) as r:
        if r.status_code == 200:
            data = r.json()  
            try:
                with open(filename,'w') as f:
                    json.dump(data,f,ensure_ascii=False)
            except :
                print(url,' fail') 
        else:
            print(url,' fail') 
    return
    
    
def get_sina_api():

    url = 'https://interface.sina.cn/news/wap/fymap2020_data.d.json'
    filename = 'data/sina.json'    
    get_data(url,filename)

    data = json.load(open("data/sina.json"))
    dic = data['data']['otherlist']
    lis = []
    
    for i in range(len(dic)): 
        name = dic[i]['name']
        citycode = dic[i]['citycode']
        url = 'https://gwpre.sina.cn/interface/news/wap/ncp_foreign.d.json?citycode='+citycode
        filename = 'data/country/'+citycode+'.json'
        get_data(url,filename)
        
    
if __name__ == '__main__': 

    print("start")
    starttime = datetime.datetime.now()
    
    get_sina_api()    
    
    print("finish")
    endtime = datetime.datetime.now()
    print('total time: ',endtime-starttime)