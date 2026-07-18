# call_api.py 简易requests练习Demo
import requests

def simple_chat(query):
    # 公共测试接口，仅练习GET请求语法
    params = {"msg": query}
    res = requests.get("https://httpbin.org/get", params=params)
    return res.json()["args"]["msg"]

if __name__ == "__main__":
    question = "通信原理Day2 requests代码练习"
    result = simple_chat(question)
    print("返回内容：", result)