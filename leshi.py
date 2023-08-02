import os
import json
def get_key_value_from_json(folder_path):
    results = {'监测数据': []}
    # 遍历指定文件夹下的所有文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        start_data = []
        click_data = []
        alone_city_result = {}
        # 检查文件是否为JSON文件
        if filename.endswith('.json'):
            with open(file_path, 'r') as file:
                try:
                    # 解析JSON文件
                    data = json.load(file)
                    for i in range(3):
                        data1 = data['vast']['Ad'][0]['InLine']['Impression'][i]['cdata']
                        start_data.append(data1)
                    alone_city_result[filename + '曝光'] = start_data
                    for i in range(3):
                        data2 = data['vast']['Ad'][0]['InLine']['Creatives']['Creative'][0]['Linear']['VideoClicks']['ClickTracking'][i]['cdata']
                        click_data.append(data2)
                    alone_city_result[filename + '点击'] = click_data
                    results ['监测数据'].append(alone_city_result)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in file: {file_path} - {e}")
    # 将结果保存到新的JSON文件中
    output_file_path = os.path.join(folder_path, 'output.json')
    with open(output_file_path, 'a' ,encoding="utf-8") as output_file:
        json.dump(results, output_file, ensure_ascii=False)
        # output_file.write(data)

# 指定文件夹路径和键
folder_path = 'D:/PP广告/乐视HR/20230705'

# 调用函数获取键的值并保存到新的JSON文件中
get_key_value_from_json(folder_path)


