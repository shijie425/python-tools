import requests
import logging

def get_city_state_by_backup_api(zip_code, timeout=3):
    """
    使用备用API (zippopotam.us) 获取城市和州信息

    Args:
        zip_code: 邮政编码
        timeout: 请求超时时间（秒）

    Returns:
        (city, state)元组，如果请求失败则返回(None, None)
    """
    backup_url = f'http://api.zippopotam.us/us/{zip_code}'

    try:
        response = requests.get(backup_url, timeout=timeout)

        if response.status_code == 200:
            json_data = response.json()
            if json_data.get('places') and len(json_data['places']) > 0:
                city = json_data['places'][0].get('place name')
                state = json_data['places'][0].get('state abbreviation')

                if city and state:
                    logging.info(f"通过备用API成功获取邮政编码信息: {zip_code} - {city} - {state}")
                    return city, state
                else:
                    logging.warning(f"备用API返回的城市或州信息为空: {zip_code}")
            else:
                logging.warning(f"备用API返回的数据格式不正确: {zip_code}")
        else:
            logging.warning(f"备用API请求失败: {zip_code}, 状态码: {response.status_code}")

    except Exception as e:
        logging.error(f"备用API请求出错: {zip_code}, 错误: {str(e)}")

    logging.error(f"备用API获取邮政编码 {zip_code} 的信息失败")
    return None, None

if __name__ == '__main__':
    all_zip = ['22936','30223','39367','22903','48647','33176','28743','24426','96037','77320','97634','31788','97479','30253','22473','97394','77351','39702','29945','16830','39567','39581','39773','33161','36340','94533','38828','55790','77905','49749','39455','98908','33809','10312','95954','36301','29418','77705','30238','21822','11784','33470','93907','31210','93591','93552','92377','24714','33411','30224','91306','56535','30291','30215','24401','55720','92545','78410','70122','30295','49749','30236','11798','92411','92503','74467','98947','78410','30014','77979','93535','98908','22473','11967','28630','29945','92407','29407','33417','25411','94954','38128','96007','14760','30434','28562','95222','95726','77364','48506','59301','30213','33430','23803','56537','30014','77905',]
    for i in all_zip:
        res_text = get_city_state_by_backup_api(i)
        print(i+'：', res_text)