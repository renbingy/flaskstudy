import os
import json
except1 = ['成都', '青岛']
def get_key_value_from_json(folder_path, key):
    results = {}
    msg2 = {'监测数据': []}
    # 遍历指定文件夹下的所有文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        start = []
        click = []
        msg = {}
        for i in except1:
            if i in file_path:
                # 检查文件是否为JSON文件
                if filename.endswith('.json'):
                    with open(file_path, 'r') as file:
                        try:
                            # 解析JSON文件
                            data = json.load(file)
                            for i in range(3):
                                data1 = data['vast']['Ad'][0]['InLine']['Impression'][i]['cdata']
                                start.append(data1)
                            msg[filename + '曝光'] = start
                            for i in range(3):
                                data2 = data['vast']['Ad'][0]['InLine']['Creatives']['Creative'][0]['Linear']['VideoClicks']['ClickTracking'][i]['cdata']
                                click.append(data2)
                            msg[filename + '点击'] = click
                            msg2['监测数据'].append(msg)
                        except json.JSONDecodeError as e:
                            print(f"Error decoding JSON in file: {file_path} - {e}")
    output_file_path = os.path.join(folder_path, 'output.json')
    with open(output_file_path, 'a' ,encoding="utf-8") as output_file:
        json.dump(msg2, output_file, ensure_ascii=False)
        # output_file.write(data)
    # 将结果保存到新的JSON文件中
    # output_file_path = os.path.join(folder_path, 'output.json')
    # with open(output_file_path, 'w') as output_file:
    #     json.dump(results, output_file)

# 指定文件夹路径和键
folder_path = 'D:/PP广告/乐视HR/20230705'
key = 'cdata'

# 调用函数获取键的值并保存到新的JSON文件中
get_key_value_from_json(folder_path, key)


