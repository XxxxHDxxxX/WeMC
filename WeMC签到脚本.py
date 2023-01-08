#http://mcpanel.lightvm.cn/ 此链接的签到脚本没有注册需要进群找机器人注册
#青龙变量ApiKey
#进入http://mcpanel.lightvm.cn/#/private 获取Api密钥输入到青龙的变量ApiKey
#export ApiKey=""
#建议将定时设置成一个小时一次，因为签到不是0点清零的所以每小时滚一次可以获得更多收益，如果你感觉你行可以一分钟一次或者半小时一次
# 0 0 */1 * * ?
from cgitb import text
import json
import time
import requests as r
import requests
import re
import json
import os

if os.environ.get("ApiKey"):
    dvm = os.environ["ApiKey"]
    if dvm != '':
        if "@" in dvm:
            Coo = dvm.split("@")
        elif "&" in dvm:
            Coo = dvm.split('&')
        else:
            Coo = dvm.split('\n')
    adv=1
    for i in Coo:
        headers = {
            "User-Agent":"Mozilla/5.0 (Linux; Android 11; M2012K11AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
            "Accept":"application/json, text/plain, */*",
            "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Encoding":"gzip, deflate",
            "If-Modified-Since":"Wed, 19 Oct 2022 15:45:56 GMT",
            "X-Requested-With":"XMLHttpRequest",
            "Connection":"keep-alive",
        }
        print(f'登录第{adv}个账号')
        adv=adv+1

        url = "http://mc1.lightstart.online:1024/Signin?ApiKey="+i
        url2 = "http://mc1.lightstart.online:1024/GetUser?ApiKey="+i
        resp = requests.get(url, headers=headers)
        xx = json.loads(resp.text)
        if xx["Status"] == True:
            print("签到成功")
        else:
            print("签到失败应该是没到签到的时间")
        
        jf = requests.get(url2, headers=headers)
        s5 = re.compile(r'.*?"Integral":(?P<zs>.*?),.*?', re.S)
        ss5 = s5.findall(jf.text)
        print(f'目前积分：{ss5}分')
        time.sleep(2)
        
