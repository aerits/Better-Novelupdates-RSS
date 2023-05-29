import requests
import subprocess
import os

import requests
import subprocess
import os
os.system("chmod +x ./src/scripts/downloadPage.sh")
def getSeriesId(link):
    seriesid = subprocess.check_output(['sh', './src/scripts/downloadPage.sh', link])
    seriesid = str(seriesid).split('"')[1][:-6]
    return seriesid

import requests
import subprocess
import os
os.system("chmod +x ./src/scripts/downloadPage.sh")
def getSeriesId(link):
    seriesid = subprocess.check_output(['sh', './src/scripts/downloadPage.sh', link])
    seriesid = str(seriesid).split('"')[1][:-6]
    return seriesid
e = getSeriesId("https://www.novelupdates.com/series/two-faced-princess/")
print(e)
