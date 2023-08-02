import json
# def traverse_json(data, parent_key=''):
#     if isinstance(data, dict):
#         for key, value in data.items():
#             new_key = f"{parent_key}.{key}" if parent_key else key
#             traverse_json(value, new_key)
#     elif isinstance(data, list):
#         for index, item in enumerate(data):
#             new_key = f"{parent_key}[{index}]"
#             traverse_json(item, new_key)
#     else:
#         print(f"Key: {parent_key} - Value: {data}")
#
# # 读取 JSON 文件
# file_path = 'D:/PP广告/乐视HR/20230705/A1上海.json'
# with open(file_path, 'r') as file:
#     json_data = json.load(file)

# 调用函数遍历 JSON 数据

# traverse_json(json_data)


from urllib.parse import urlparse, parse_qs

def compare_url_params(url1, url2):
    # 解析 URL，获取参数字典
    params1 = parse_qs(urlparse(url1).query)
    params2 = parse_qs(urlparse(url2).query)

    # 比较参数并找到不同之处
    diff_params = {}

    for param in set(params1.keys()) | set(params2.keys()):
        if params1.get(param) != params2.get(param):
            diff_params[param] = (params1.get(param), params2.get(param))

    return diff_params

# 两个 URL
url1 = "http://ark.letv.com/adx2?adzone=50&ark=&vid=25960253&cid=0&res=json&t=1689214695&platform=1&duration=15&ct=2&oid=140922&uip=112.224.164.114&cpr=&type=0&tags=2&vvid=4beaca7d729e7d4c10bd3172b97af4711689214696076&devicetype=0&adjust_index=0&cp=[LETV_V_URL]&deal=2024371&needH265=1&cuid=2b350ee88c6f04a895953e680159bcf3&areaid=1156110000,1156110000,1156000000&mediatype=2&leadreqtid=101cf687-8ac2-4bc6-bb82-3c7a25f5b3d6-0713-101815&from=4&oaid=de46b46a-1aa2-46e5-b90a-b46fd587f029&aaid=&bmk=aefc1d07-99d0-4edf-8103-2959bfdf0fcb&umk=1577984869.570000000&amv=130201301&a=letvVideo_10.6.3&b=&c=&d=&e=08c770dc9924b581&f=HONOR&g=YAL-AL00&h=android&i=10&k=2&l=0&m=&n=A28197C73D36&oaid=de46b46a-1aa2-46e5-b90a-b46fd587f029&o=1080&p=2232&ver=10.6.3&bundle=com.letv.android.client&carrier=0"
url2 = "https://ark.letv.com/adx2?adzone=50&ark=&vid=1145503&cid=0&res=json&t=1689158126287&platform=1&duration=15&ct=2&oid=141311&cpr=&type=0&tags=2&vvid=4beaca7d729e7d4c10bd3172b97af4711688538990388&devicetype=0&adjust_index=1&cp=%5BLETV_V_URL%5D&deal=2024371&needH265=1&cuid=2b350ee88c6f04a895953e680159bcd5&areaid=1156110000%2C1156110000%2C1156000000&mediatype=2&leadreqtid=e64138e0-2ae8-4cc2-bb18-5b2352e4895c-0705-143630&from=4&oaid=de46b46a-1aa2-46e5-b90a-b46fd587f070&aaid=&bmk=aefc1d07-99d0-4edf-8103-2959bfdf0fcb&umk=1577984869.570000000&amv=130101300&a=letvVideo_10.6.3&b=&c=&d=&e=08c770dc9924b581&f=HONOR&g=YAL-AL00&h=android&i=10&k=2&l=0&m=&n=A28197C73D36&oaid=de46b46a-1aa2-46e5-b90a-b46fd587f070&o=1080&p=2232&ver=10.6.3&bundle=com.letv.android.client&carrier=0&uip=112.224.164.114"

# 比较 URL 参数并找到不同之处
diff_params = compare_url_params(url1, url2)

# 打印不同之处的参数和值
for param, values in diff_params.items():
    print(f"Parameter: {param}")
    print(f"URL 1 Value: {values[0]}")
    print(f"URL 2 Value: {values[1]}")
    print()

