import requests
import time
import urllib.request
import os
import random


img_name=str(input("Enter Product Name:"))

def subString(mainTxt,spos,sTag,eTag):
    
    subStr = ""
    subStr = mainTxt
    global subStrValue

    try:
        tagStartPos = int(subStr.index(sTag,(int(spos))))
        tagEndPos = int(subStr.find(eTag,(int(tagStartPos)+int(len(sTag)))))
        subStrValue = ""
        subStrValue = subStr[tagStartPos+int(len(sTag)):tagEndPos]
        subStrValue = str(subStrValue)
    except:
        tagStartPos = 0
        tagEndPos = 0
        subStrValue = ""

    return str(subStrValue)

def get_search_keyword():
    return img_name

def get_url_from_responsetext(responsetext):
    urls_list = []
    ipos = 1
    con = len(responsetext.split('<img data-src='))

    for i in range(con):
        ipos = responsetext.find('<img data-src=',ipos)
        tempUrl = ''
        tempUrl = subString(responsetext,ipos,'="','"')
        tempUrl = tempUrl.replace("'","")
        if 'http' in tempUrl:
            urls_list.append(tempUrl)
        ipos = ipos+10
    return urls_list

def fetch_urls():
    base_url = 'https://www.google.com/search?safe=active&tbm=isch&source=hp&biw=628&bih=657&ei=Px4LXdqLH9fLrQGk-5nwDQ&q='
    
    headers = {
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
               'Accept-language': 'en-US,en;q=0.9',
               'Content-type':'text/html; charset=UTF-8',
               'Referer': 'https://images.google.com/',
               'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
              }
    try:
        response = requests.get(url=f'{base_url}{get_search_keyword()}', headers=headers, timeout=50)
    except Exception as e:
        print(e)
    print('Response status:',response.status_code)
    if response.status_code==200:
        try:
            responseText = response.text
            all_list_urls = get_url_from_responsetext(responseText)
            
            writFile = open('urls.txt','a')
            for urls in all_list_urls:
                writFile.write(urls+'\n')
        except Exception as e:
            print('Error while parsing:',e)
    return all_list_urls
            

fetched_urls = fetch_urls()


def download_images_using(url, img_name, img_no):
    try:
        urllib.request.urlretrieve(url,f"images/{MYDIR}/{img_name}_{img_no}.jpg")
    except Exception as e:
        print(f'Error while downloading image {img_no}', e)

images_link = open('urls.txt','r')
#print(images_link.read())

img_no = 1
MYDIR = img_name
CHECK_FOLDER = os.path.isdir(MYDIR)
if not CHECK_FOLDER:
    cur_path = os.getcwd()
    os.chdir("images")
    os.makedirs(MYDIR)
    print("created folder : ", MYDIR)
    os.chdir(cur_path)
else:
    print(MYDIR, "folder already exists.")
    
with open('urls.txt','r') as f:
    for url in f:
        download_images_using(url, img_name, img_no)
        img_no=img_no+random.randint(0,100000)
    f.close()

print("Dowloading completed...!!!")
try:
    os.remove("urls.txt")
    print("File Removed!")
except:
    f = open('urls.txt','w')
