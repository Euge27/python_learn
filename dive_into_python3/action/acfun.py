import re
import os
import sys
import json
import time
import urllib.request
import lxml.etree
from pyquery import PyQuery as pyq

def findApiId(url):
  doc = pyq(url=r'{}'.format(url))
  text = doc('#area-player div.hidden').text()
  result = re.search('\d+', text).group()
  return result

def findVid(url):
  data = urllib.request.urlopen(url).read()
  string = data.decode('utf-8')
  jobj = json.loads(string)
  return jobj['vid']

def analyzePlaylist(url):
  data = urllib.request.urlopen(url).read()
  tree = lxml.etree.fromstring(data)
  return [ele.text for ele in tree.findall('durl/url')]

def getPlaylist(url):
  acId = findApiId(url)
  vid = findVid('http://www.acfun.tv/api/player/vids/{}.aspx'.format(acId))
  list = analyzePlaylist('http://v.iask.com/v_play.php?vid={}&dtime={}'.format(vid, round(time.time() * 1000)))
  return list

def play(list):
  for url in list:
    os.system('mplayer "{}"'.format(url))

if __name__ == '__main__':
  list = getPlaylist(sys.argv[1])
  play(list)
