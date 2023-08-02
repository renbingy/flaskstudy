import json

wangmai_start_file_name = 'D:\\PP广告\迭代需求\\ads服务端\旺脉API对接\\'
ads_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\ads_information_video_ios.json'

file = wangmai_start_file_name + 'wangmai_information_video_ios.json'
print(file)
# file =

with open(file, encoding= 'utf-8') as fp:
    wangmai_start_data_total = json.load(fp)

    if 'image_src' in wangmai_start_data_total:
        print('cc')