import execjs
import codecs
import requests
from urllib.parse import urlencode

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'dnt': '1',
    'priority': 'u=1, i',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAA5tFAhdpZtNyiilaQ5uo0fbcSxZruzpnckrpzpkCc0oDBkkt1hGg7GGPkyKka4U0N',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
}

params = {
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'sec_user_id': 'MS4wLjABAAAA5tFAhdpZtNyiilaQ5uo0fbcSxZruzpnckrpzpkCc0oDBkkt1hGg7GGPkyKka4U0N',
    'max_cursor': '0',
    'locate_query': 'false',
    'show_live_replay_strategy': '1',
    'need_time_list': '1',
    'time_list_query': '0',
    'whale_cut_token': '',
    'cut_version': '1',
    'count': '18',
    'publish_video_strategy_type': '2',
    'update_version_code': '170400',
    'pc_client_type': '1',
    'version_code': '290100',
    'version_name': '29.1.0',
    'cookie_enabled': 'true',
    'screen_width': '1920',
    'screen_height': '1080',
    'browser_language': 'zh-CN',
    'browser_platform': 'Win32',
    'browser_name': 'Edge',
    'browser_version': '125.0.0.0',
    'browser_online': 'true',
    'engine_name': 'Blink',
    'engine_version': '125.0.0.0',
    'os_name': 'Windows',
    'os_version': '10',
    'cpu_core_num': '16',
    'device_memory': '8',
    'platform': 'PC',
    'downlink': '10',
    'effective_type': '4g',
    'round_trip_time': '150',
    'webid': '7347893254858638874',
    'verifyFp': 'verify_lwgblovy_l6tALna2_Re1W_4doB_8sbu_tpg3hbfDNRs2',
    'fp': 'verify_lwgblovy_l6tALna2_Re1W_4doB_8sbu_tpg3hbfDNRs2',
    'msToken': 'OPt0eGQlzBCr3GYDVNh_ngFHDgkr0TATF0HIA8OJAjhkBIOTLhcTzd88aZLbv5pVBzwUVZVnGVbt1WaUOgMQAOfxQ8PzLjaOs-gcTD9Y4zJlhuSDQRsX',
    }


def a_bougus(params):
    encoded_params = urlencode(params) #对参数进行编码
    with codecs.open('a_bogus.js', 'r', encoding='gb2312') as file:
        js_code = file.read()
    node_runtime = execjs.get(execjs.runtime_names.Node)
    context = node_runtime.compile(js_code,cwd=r"C:/Users/***/AppData/Roaming/npm/node_modules")
    arg = [ 0, 1, 0, encoded_params, "",headers['user-agent']] 
    a_bougus = context.call('get_a_bogus', arg)
    return a_bougus

print(a_bougus(params))
