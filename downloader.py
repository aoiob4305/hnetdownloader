#-*- coding: utf-8 -*-

import sys
import subprocess

links = {
    'xxx': {
        'link': http://vod.cdn.hunet.co.kr/eLearning/Hunet/vod코드/{0:02d}.mp4",
        'start': 1,
        'end': 34
        },
    }

def downloadvod(link, start, end):
    for idx in range(start, end + 1):
        args = ['.//avconv//avconv.exe',
                '-i', link.format(idx),
                '-acodec', 'copy',
                '-vcodec', 'copy',
                '{0:02d}.mp4'.format(idx)]
        proc = subprocess.Popen(args)
        proc.wait()

if __name__ == '__main__':
    if len(sys.argv) == 4 or len(sys.argv) == 2:
        try:
            link = links[sys.argv[1]]
            if len(sys.argv) == 4:
                downloadvod(link['link'], int(sys.argv[2]), int(sys.argv[3]))
            else:
                downloadvod(link['link'], link['start'], link['end'])
        except KeyError:
            print("subjectname was wrong")
        except ValueError:
            print("some value was wrong")
            
    else:
        print("usage1: {0} subjectname \nusage2: {0} subjectname startnum endnum".format(sys.argv[0]))
        print(links.keys())
