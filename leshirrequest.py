import os
import json
import time
import requests

def requestt_leshi_hr(ip_json, folder_path, deal = '2024371'):
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    params = [
        ('adzone', '50'),
        ('ark', ''),
        ('vid', '1145503'),
        ('cid', '0'),
        ('res', 'json'),
        ('t', int(time.time() * 1000)),
        ('platform', '1'),
        ('duration', '15'),
        ('ct', '2'),
        ('oid', '141311'),
        ('cpr', ''),
        ('type', '0'),
        ('tags', '2'),
        ('vvid', '4beaca7d729e7d4c10bd3172b97af4711688538990388'),
        ('devicetype', '0'),
        ('adjust_index', '1'),
        ('cp', '[LETV_V_URL]'),
        ('needH265', '1'),
        ('cuid', '2b350ee88c6f04a895953e680159bcd5'),
        ('areaid', '1156110000,1156110000,1156000000'),
        ('mediatype', '2'),
        ('leadreqtid', 'e64138e0-2ae8-4cc2-bb18-5b2352e4895c-0705-143630'),
        ('from', '4'),
        ('oaid', 'de46b46a-1aa2-46e5-b90a-b46fd587f070'),
        ('aaid', ''),
        ('bmk', 'aefc1d07-99d0-4edf-8103-2959bfdf0fcb'),
        ('umk', '1577984869.570000000'),
        ('amv', '130101300'),
        ('a', 'letvVideo_10.6.3'),
        ('b', ''),
        ('c', ''),
        ('d', ''),
        ('e', '08c770dc9924b581'),
        ('f', 'HONOR'),
        ('g', 'YAL-AL00'),
        ('h', 'android'),
        ('i', '10'),
        ('k', '2'),
        ('l', '0'),
        ('m', ''),
        ('n', 'A28197C73D36'),
        ('oaid', 'de46b46a-1aa2-46e5-b90a-b46fd587f070'),
        ('o', '1080'),
        ('p', '2232'),
        ('ver', '10.6.3'),
        ('bundle', 'com.letv.android.client'),
        ('carrier', '0'),
        ('deal', deal)
    ]

    for ip_name,ip_value in ip_json.items():
        url = 'https://ark.letv.com/adx2'
        url2 = url + '?uip=' + ip_value
        content = requests.get(url2, params=params, headers=headers)
        content_json = json.loads(content.content)
        if content_json['vast']['Ad']:
            k = content_json['vast']['Ad'][0]['InLine']['Impression'][0]['cdata'][27:44]
            creative_url = content_json['vast']['Ad'][0]['InLine']['Creatives']['Creative'][0]['Linear']['MediaFiles']['MediaFile']['cdata']
            print(f'IP值等于{ip_name} {ip_value} 对应的k值为{k}')
            print(creative_url)
            output_file_path = os.path.join(folder_path, f'{ip_name}.json')
            with open(output_file_path, 'a', encoding="utf-8") as output_file:
                json.dump(content_json, output_file, ensure_ascii=False)
        else:
            print(f'IP值等于{ip_name} {ip_value} 返回广告空')

ip_json = {
	'上海': '101.227.131.220',
	'北京': '14.127.123.15',
	'深圳': '14.127.123.15',
	'广州': '113.108.182.52',
	'杭州': '115.239.212.133',
	'成都': '117.136.15.78',
	'重庆': '61.128.128.68',
	'长春': '222.27.95.255',
	'沈阳': '211.137.32.178',
	'南京': '221.226.1.30',
	'西安':'124.115.6.19',
	'青岛':'112.224.164.114',
	'武汉':'27.18.198.204',
	'合肥':'218.22.32.186',
	'天津':'221.198.0.22',
	'昆明':'116.54.146.17',
	'哈尔滨':'125.223.124.111',
	'大连':'175.162.7.44',
	'济南':'140.255.4.89',
	'宁波':'60.179.231.195'
}
deal_data = {'deal':'2024371',
                'deal2':'2024174'
               }
folder_path = 'D:/PP广告/乐视HR/20230713'

requestt_leshi_hr(ip_json,folder_path,deal_data['deal'])