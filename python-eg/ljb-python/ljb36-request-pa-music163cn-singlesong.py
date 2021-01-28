import requests
import os
 
def develop(path,url):
    song_url = url
    song_id = song_url[32:]
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        if not os.path.exists(path + song_id + '.mp3'):
            r = requests.get('https://link.hhtjim.com/163/' + song_id + '.mp3')
            with open(path + 'music' + song_id + '.mp3', 'wb') as f:
                f.write(r.content)
                f.close()
                print('下载成功')
        else:
            print('歌曲已存在')
    except:
        print("异常")
 
if __name__ == '__main__':
    develop('C:/电子书/','https://music.163.com/#/song?id=1365898499')