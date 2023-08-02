import json
#position =1 开屏和banner,position==2信息流
position =2
not_list = []
#安卓开屏
# wangmai_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\wangmai_start.json'
# ads_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\ads_start.json'
# wangmai_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\wangmai_start_video.json'
# ads_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\ads_start_video.json'

# #安卓banner2
# wangmai_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\wangmai_banner.json'
# ads_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\ads_banner.json'
#安卓information
# wangmai_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\wangmai_information.json'
# ads_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\ads_information.json'
#安卓information_video
# wangmai_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\wangmai_information_video.json'
# ads_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\ads_information_video.json'

#ios开屏
# wangmai_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\wangmai_start_ios.json'
# ads_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\ads_start_ios.json'
# wangmai_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\wangmai_start_video_ios.json'
# ads_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\ads_start_video_ios.json'
#ios   banner2
# wangmai_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\wangmai_bbanner_ios.json'
# ads_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\ads_banner_ios.json'
#ios   informaiton
# wangmai_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\wangmai_information_ios.json'
# ads_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\ads_information_ios.json'
wangmai_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\wangmai_information_video_ios.json'
ads_start_file_name = r'D:\PP广告\迭代需求\ads服务端\旺脉API对接\ads_information_video_ios.json'

with open(wangmai_start_file_name, encoding= 'utf-8') as fp:
    wangmai_start_data_total = json.load(fp)
    # data = wangmai_start_data_total.get('wxad') #
    wangmai_wxad = wangmai_start_data_total['wxad']

    creative_type = wangmai_wxad.get('creative_type')
    print('旺脉creative_type返回值为：{}'.format(creative_type))
    ad_title = wangmai_wxad.get('ad_title')
    if 'brand_name' in wangmai_start_data_total:
        brand_name = wangmai_wxad.get('brand_name')
    # print('$$$$$$$$$$$$$$$$$$$$$$$$'+brand_name)
    description = wangmai_wxad.get('description')
    if 'image_src' in wangmai_wxad:
        image_src = wangmai_wxad.get('image_src')
    material_width = wangmai_wxad.get('material_width')
    material_height = wangmai_wxad.get('material_height')
    interaction_type = wangmai_wxad.get('interaction_type')
    win_notice_url = wangmai_wxad.get('win_notice_url')   #返回列表，需要组合位"|"连接的字符串
    win_notice_url_start = '|'.join(win_notice_url)
    click_url = wangmai_wxad.get('click_url')    #返回列表，需要组合位"|"连接的字符串
    click_url_click = '|'.join(click_url)
    dp_success_track_urls = wangmai_wxad.get('dp_success_track_urls')[0]  #返回列表，需要提取
    landing_page_url = wangmai_wxad.get('landing_page_url')
    deep_link = wangmai_wxad.get('deep_link')
    if creative_type == 6:
        wangmai_video = wangmai_wxad.get('video')
        duration = wangmai_video.get('duration')
        v_url = wangmai_video.get('v_url')
        v_type = wangmai_video.get('v_type')
        start_url = wangmai_video.get('v_tracking').get('v_progress_tracking_event')[0]['url'][0]
        end_url =  wangmai_video.get('v_tracking').get('v_progress_tracking_event')[1]['url'][0]

with open(ads_start_file_name, encoding= 'utf-8') as fp:
    ads_start_data_total = json.load(fp)
    material = ads_start_data_total[0]['material'][0]
    deeplink = material['deeplink']
    link = material['link']
    deeplinkTrackUrls = material['deeplinkTrackUrls']
    height = material['height']
    width = material['width']
    text = material['text']
    click_all = ads_start_data_total[0]['monitor']['click']
    click_list = click_all.split('|')
    del click_list[0]
    click = '|'.join(click_list)
    linkType = material['linkType']
    if linkType:
        linkType = int(material['linkType'])
    if position == 2:
        stat_all = ads_start_data_total[0]['monitor']['start']
        stat_list = stat_all.split('|')
        del stat_list[0]
        stat = "|".join(stat_list)
        ads_video = material['video']
        img =  material['img']
        brandText = material['brandText']
        subTitle = material['subTitle']
        end_all = ads_start_data_total[0]['monitor']['end']
        end_list = end_all.split('|')
        del end_list[0]
        end = '|'.join(end_list)
    else:
        stat = ads_start_data_total[0]['monitor']['start']
        end = ads_start_data_total[0]['monitor']['end']
        src = material['src']


if description == text:
    print('description和text对应正确')
else:
    print('description和text对应异常')
    print('旺脉description为:{}'.format(description))
    print('ads  text为:{}'.format(text))
    not_list.append('text')

if material_width == width:
    print('material_width和width对应正确')
else:
    print('material_width和width对应异常')
    print('旺脉material_width为:{}'.format(material_width))
    print('ads  width为:{}'.format(width))
    not_list.append('width')
if material_height == height:
    print('material_height和height对应正确')
else:
    print('material_height和height对应异常')
    print('旺脉material_height为:{}'.format(material_height))
    print('ads  height为:{}'.format(height))
    not_list.append('height')
if linkType:
    if interaction_type == linkType:
        print('interaction_type和linkType对应正确')
    else:
        print('interaction_type和linkType对应异常')
        print('旺脉interaction_type为:{}'.format(interaction_type))
        print('ads  linkType为:{}'.format(linkType))
        not_list.append('linkType')
if click_url_click == click:
    print('click_url_click和click对应正确')
else:
    print('click_url_click和click对应异常')
    print('旺脉click_url_click为:{}'.format(click_url_click))
    print('ads  click为:{}'.format(click))
    not_list.append('click')
if dp_success_track_urls == deeplinkTrackUrls:
    print('dp_success_track_urls和deeplinkTrackUrls对应正确')
else:
    print('dp_success_track_urls和deeplinkTrackUrls对应异常')
    print('旺脉dp_success_track_urls为:{}'.format(dp_success_track_urls))
    print('ads  deeplinkTrackUrls为:{}'.format(deeplinkTrackUrls))
    not_list.append('deeplinkTrackUrls')
if deep_link == deeplink:
    print('deep_link和deeplink对应正确')
else:
    print('deep_link和deeplink对应异常')
    print('旺脉deep_link为:{}'.format(deep_link))
    print('ads  deeplink为:{}'.format(deeplink))
    not_list.append('deeplink')
if landing_page_url == link:
    print('landing_page_url和link对应正确')
else:
    print('landing_page_url和link对应异常')
    print('旺脉landing_page_url为:{}'.format(landing_page_url))
    print('ads  link为:{}'.format(link))
    not_list.append('link')

if position == 2:
    if 'brand_name' in wangmai_start_data_total:
        if brand_name == brandText:
            print('brand_name和brandText对应正确')
        else:
            print('brand_name和brandText对应异常')
            print('旺脉brand_name为:{}'.format(brand_name))
            print('ads  brandText为:{}'.format(brandText))
            not_list.append('brandText')
    if ad_title == subTitle:
        print('ad_title和subTitle对应正确')
    else:
        print('ad_title和subTitle对应异常')
        print('旺脉ad_title为:{}'.format(ad_title))
        print('ads  subTitle为:{}'.format(subTitle))
        not_list.append('subTitle')
    # if brand_name == brandText:
    #     print('brand_name和brandText对应正确')
    # else:
    #     print('brand_name和brandText对应异常')
    #     print('旺脉brand_name为:{}'.format(brand_name))
    #     print('ads  brandText为:{}'.format(brandText))
    #信息流：creative_type = 6，则img从image_src获取，video从video.v_url获取
    if 'image_src' in wangmai_wxad:
        if image_src == img:
            print('image_src和img对应正确')
        else:
            print('image_src和img对应异常')
            print('旺脉image_src为:{}'.format(image_src))
            print('ads  img为:{}'.format(img))
            not_list.append('img')
    else:
        print('###################################################旺旺没有返回信息流图片')
    if creative_type == 6:
        if v_url == ads_video:
            print('v_url和video对应正确')
        else:
            print('v_url和video对应异常')
            print('旺脉v_url为:{}'.format(v_url))
            print('ads  video为:{}'.format(ads_video))
            not_list.append('ads_video')
######################
if position == 1:
    #开屏和banner2：creative_type=6，则src从video.v_url获取，creative_type == 3从image_src获取
    if creative_type == 3:
        if image_src == src:
            print('image_src和src对应正确')
        else:
            print('image_src和src对应异常')
            print('旺脉image_src为:{}'.format(image_src))
            print('ads  src为:{}'.format(src))
            not_list.append('src')
    if creative_type == 6:
        if v_url == src:
            print('v_url和src对应正确')
        else:
            print('v_url和src对应异常')
            print('旺脉v_url为:{}'.format(v_url))
            print('ads  src为:{}'.format(src))
            not_list.append('src')
###################3
if creative_type == 6:
    #millisec=0或1000的对应material中的monitor.start字段
    #millisec=duration*1000的对应material中的monitor.end字段
    if start_url == stat:
        print('start_url和stat对应正确')
    else:
        print('start_url和stat对应异常')
        print('旺脉start_url为:{}'.format(start_url))
        print('ads  stat为:{}'.format(stat))
        not_list.append('stat')
    if end_url == end:
        print('end_url和end对应正确')
    else:
        print('end_url和end对应异常')
        print('旺脉end_url为:{}'.format(end_url))
        print('ads  end为:{}'.format(end))
        not_list.append('end')
else:
    if win_notice_url_start == stat:
        print('win_notice_url_start和stat对应正确')
    else:
        print('win_notice_url_start和stat对应异常')
        print('旺脉win_notice_url_start为:{}'.format(win_notice_url_start))
        print('ads  stat为:{}'.format(stat))
        not_list.append('stat')


print('异常字段为{}'.format(not_list))
