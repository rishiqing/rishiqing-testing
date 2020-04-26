# 1. 登录
import framework.common.network.http_request as  httpRequest
import rishiqing.constants.url as url


def login(j_username = "gs01@qq.com", j_password = "123456"):
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"j_username\"\r\n\r\n" + j_username + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"j_password\"\r\n\r\n" + j_password + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    response = httpRequest.post(url.LOGIN, payload)
    body = httpRequest.getJson(response)
    print("登录结果:"+str(body))
    return body
