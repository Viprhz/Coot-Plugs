#coding=utf8
import re, time, requests, http, json, datetime, random
from urllib.request import urlopen
from urllib.parse import urlencode
from threading import Timer

def api(url):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    timeout = random.choice(range(80, 180))
    data = requests.get(url, headers=header, timeout=timeout)

    return data.json()

def sendweather(city):
    # 需要把 {yourKEY} 替换为你自己申请的 API KEY，注册地址：https://dev.heweather.com
    url = 'https://free-api.heweather.com/s6/weather/forecast?location='+city+'&key={yourKEY}'
    PMurl = 'https://free-api.heweather.com/s6/air/now?parameters&location='+city+'&key={yourKEY}'
    lifeurl = 'https://free-api.heweather.com/s6/weather/lifestyle?location='+city+'&key={yourKEY}'
    
    temp = api(url)
    temp = temp['HeWeather6'][0]
    update = temp['update']
    now = temp['daily_forecast'][0]
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    pm = api(PMurl)
    pm = pm['HeWeather6'][0]
    airnow = pm['air_now_city']

    life = api(lifeurl)
    
    life = life['HeWeather6'][0]
    life = life['lifestyle']
    result =  city + '\n'\
    +' ------------------------------------------' + '\n'\
    + '    今天天气：'+ now['cond_txt_d'] + ' 转 ' + now['cond_txt_n'] + '\n'\
    + '    今天温度：'+ now['tmp_min'] + '°C ~ ' + now['tmp_max'] + '°C' + '\n'\
    + '    风向：'+ now['wind_dir'] + ' ' + now['wind_sc'] + '级 '+ now['wind_spd'] + '公里/小时'+ '\n'\
    + '    相对湿度：'+ now['hum'] + '%' + '\n'\
    + '    降水量：'+ now['pcpn'] + 'ml' + '，降水概率：'+ now['pop'] + '%' + '\n'\
    + '    能见度：'+ now['vis'] + '公里' + '\n'\
    + '------------------------------------------' + '\n'\
    + '今天空气质量：'+'\n'\
    + '    空气质量指数：'+ airnow['aqi']+'\n'\
    + '    空气质量：'+ airnow['qlty']+'\n'\
    + '    二氧化氮指数：'+ airnow['no2']+'\n'\
    + '    二氧化硫指数：'+ airnow['so2']+'\n'\
    + '    一氧化碳指数：'+ airnow['co']+'\n'\
    + '    pm10指数：'+ airnow['pm10']+'\n'\
    + '    pm25指数：'+ airnow['pm25']+'\n'\
    + '    臭氧指数：'+ airnow['o3'] +'\n'\
    + '------------------------------------------' + '\n'\
    + '1. '+ life[0]['txt']+'\n\n'\
    + '2. '+ life[1]['txt']+'\n\n'\
    + '3. '+ life[2]['txt']+'\n\n'\
    + '😄😊😉😍😘😚😜😝😳😁'+'\n\n'\
        
    result =  result + '发送时间：' +  nowTime + '\n'
    print(result)
    return result

