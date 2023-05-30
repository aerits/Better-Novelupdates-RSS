import requests
import subprocess
import os
import sys

import requests
import subprocess
import os
import sys
os.system("chmod +x ./src/scripts/downloadPage.sh")
def getSeriesId(link):
    seriesid = subprocess.check_output(['sh', './src/scripts/downloadPage.sh', link, '0'])
    seriesid = str(seriesid).split('"')[1][:-6]
    return seriesid

import requests
import subprocess
import os
import sys
os.system("chmod +x ./src/scripts/downloadPage.sh")
def getSeriesId(link):
    seriesid = subprocess.check_output(['sh', './src/scripts/downloadPage.sh', link, '0'])
    seriesid = str(seriesid).split('"')[1][:-6]
    return seriesid
e = getSeriesId("https://www.novelupdates.com/series/two-faced-princess/")
print(e)

import requests
import subprocess
import os
import sys
import requests
import subprocess
import os
import sys
os.system("chmod +x ./src/scripts/downloadPage.sh")
def getSeriesId(link):
    seriesid = subprocess.check_output(['sh', './src/scripts/downloadPage.sh', link, '0'])
    seriesid = str(seriesid).split('"')[1][:-6]
    return seriesid

def markRead(form, series, chapter):
  seriesid = getSeriesId(series)
  if(form>0):
  # get latest chapter
    chapter = subprocess.check_output(['sh', './src/scripts/downloadPage.sh', series, '1'])
    return 1
  url = "https://www.novelupdates.com/readinglist_update.php?rid="+chapter+"&sid="+seriesid+"&checked=yes"
  # response = requests.get(url)
  # print(response.status_code)
  # print(response.text)
  # print(url)
  subprocess.call(['w3m', url, '-dump'])

if(sys.argv[2] == '0'):
    markRead(1, sys.argv[1], 0)
else:
    chapter = sys.argv[2].split("/")
    # print(chapter[4])
    markRead(0, sys.argv[1], chapter[4])
