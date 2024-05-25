import time
import os
import datetime
import random
import urllib.request
import html
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# 옵션 생성
options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")
# Chrome WebDriver의 경로를 직접 지정
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(1)
# Naver API key 입력
client_id = 'a36FRAny3U813eNsBHqP' 
client_secret = 'J_cwztPj_x'
news_list = ['국민의힘','날씨','민주당','의대','전쟁','정부']

n_display = 1
base_url = 'https://openapi.naver.com/v1/search/news.json'
sort = 'sim'

for k in news_list:
    encQuery = urllib.parse.quote(k)
    start = 1
    url = f'{base_url}?query={encQuery}&display={n_display}&start={start}&sort={sort}'

    my_request = urllib.request.Request(url)
    my_request.add_header("X-Naver-Client-Id",client_id)
    my_request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(my_request)

    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
    else:
        print("Error Code:" + rescode)

    search_results = response_body.decode('utf-8')
    search_results = eval(search_results)

    all_results = dict()
    i = 0
    for item in search_results['items']:
        link = html.unescape(item['link']).replace('\\','')
        pubdate = item['pubDate']
        if 'n.news.naver.com' in link: # "진짜" 네이버 뉴스 link만 사용합니다.
            all_results[i] = dict()
            
            # scraping하려는 웹페이지 주소를 get()에 전달
            driver.get(link)
            
            # 제목 추출하기
            title = driver.find_elements(By.CLASS_NAME, 'media_end_head_headline')
            title = title[0].text
            
            # 본문 추출하기
            body = driver.find_elements(By.ID, 'newsct_article')
            # body = driver.find_elements(By.ID, 'articeBody') # 가끔 ID가 이렇게 생긴 녀석도 존재합니다...
            body = body[0].text.replace('\n','')
            
            all_results[i]['link'] = link
            all_results[i]['pubdate'] = pubdate
            all_results[i]['title'] = title
            all_results[i]['body'] = body
            time.sleep(1)
            i += 1

    df = pd.DataFrame(all_results).T
    folder_path = f"G:/내 드라이브/4-1/텍데분/크롤링/크롤링폴더/{k}"
    now = datetime.datetime.now() 
    file_path = os.path.join(folder_path, f'{k}_{now.strftime("%Y%m%d")}_{start}.csv')

    # 지정된 경로에 CSV 파일 저장
    df.to_csv(file_path, encoding='utf-8-sig', index=False)


##################################################################################################################

for k in news_list:
    encQuery = urllib.parse.quote(k)
    start = 101
    url = f'{base_url}?query={encQuery}&display={n_display}&start={start}&sort={sort}'

    my_request = urllib.request.Request(url)
    my_request.add_header("X-Naver-Client-Id",client_id)
    my_request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(my_request)

    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
    else:
        print("Error Code:" + rescode)

    search_results = response_body.decode('utf-8')
    search_results = eval(search_results)

    all_results = dict()
    i = 0
    for item in search_results['items']:
        link = html.unescape(item['link']).replace('\\','')
        pubdate = item['pubDate']
        if 'n.news.naver.com' in link: # "진짜" 네이버 뉴스 link만 사용합니다.
            all_results[i] = dict()
            
            # scraping하려는 웹페이지 주소를 get()에 전달
            driver.get(link)
            
            # 제목 추출하기
            title = driver.find_elements(By.CLASS_NAME, 'media_end_head_headline')
            title = title[0].text
            
            # 본문 추출하기
            body = driver.find_elements(By.ID, 'newsct_article')
            # body = driver.find_elements(By.ID, 'articeBody') # 가끔 ID가 이렇게 생긴 녀석도 존재합니다...
            body = body[0].text.replace('\n','')
            
            all_results[i]['link'] = link
            all_results[i]['pubdate'] = pubdate
            all_results[i]['title'] = title
            all_results[i]['body'] = body
            time.sleep(1)
            i += 1

    df = pd.DataFrame(all_results).T
    folder_path = f"G:/내 드라이브/4-1/텍데분/크롤링/크롤링폴더/{k}"
    now = datetime.datetime.now() 
    file_path = os.path.join(folder_path, f'{k}_{now.strftime("%Y%m%d")}_{start}.csv')

    # 지정된 경로에 CSV 파일 저장
    df.to_csv(file_path, encoding='utf-8-sig', index=False)


##################################################################################################################

for k in news_list:
    encQuery = urllib.parse.quote(k)
    start = 201

    url = f'{base_url}?query={encQuery}&display={n_display}&start={start}&sort={sort}'

    my_request = urllib.request.Request(url)
    my_request.add_header("X-Naver-Client-Id",client_id)
    my_request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(my_request)

    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
    else:
        print("Error Code:" + rescode)

    search_results = response_body.decode('utf-8')
    search_results = eval(search_results)

    all_results = dict()
    i = 0
    for item in search_results['items']:
        link = html.unescape(item['link']).replace('\\','')
        pubdate = item['pubDate']
        if 'n.news.naver.com' in link: # "진짜" 네이버 뉴스 link만 사용합니다.
            all_results[i] = dict()
            
            # scraping하려는 웹페이지 주소를 get()에 전달
            driver.get(link)
            
            # 제목 추출하기
            title = driver.find_elements(By.CLASS_NAME, 'media_end_head_headline')
            title = title[0].text
            
            # 본문 추출하기
            body = driver.find_elements(By.ID, 'newsct_article')
            # body = driver.find_elements(By.ID, 'articeBody') # 가끔 ID가 이렇게 생긴 녀석도 존재합니다...
            body = body[0].text.replace('\n','')
            
            all_results[i]['link'] = link
            all_results[i]['pubdate'] = pubdate
            all_results[i]['title'] = title
            all_results[i]['body'] = body
            time.sleep(1)
            i += 1

    df = pd.DataFrame(all_results).T
    folder_path = f"G:/내 드라이브/4-1/텍데분/크롤링/크롤링폴더/{k}"
    now = datetime.datetime.now() 
    file_path = os.path.join(folder_path, f'{k}_{now.strftime("%Y%m%d")}_{start}.csv')

    # 지정된 경로에 CSV 파일 저장
    df.to_csv(file_path, encoding='utf-8-sig', index=False)


##################################################################################################################

for k in news_list:
    encQuery = urllib.parse.quote(k)
    start = 301

    url = f'{base_url}?query={encQuery}&display={n_display}&start={start}&sort={sort}'

    my_request = urllib.request.Request(url)
    my_request.add_header("X-Naver-Client-Id",client_id)
    my_request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(my_request)

    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
    else:
        print("Error Code:" + rescode)

    search_results = response_body.decode('utf-8')
    search_results = eval(search_results)

    all_results = dict()
    i = 0
    for item in search_results['items']:
        link = html.unescape(item['link']).replace('\\','')
        pubdate = item['pubDate']
        if 'n.news.naver.com' in link: # "진짜" 네이버 뉴스 link만 사용합니다.
            all_results[i] = dict()
            
            # scraping하려는 웹페이지 주소를 get()에 전달
            driver.get(link)
            
            # 제목 추출하기
            title = driver.find_elements(By.CLASS_NAME, 'media_end_head_headline')
            title = title[0].text
            
            # 본문 추출하기
            body = driver.find_elements(By.ID, 'newsct_article')
            # body = driver.find_elements(By.ID, 'articeBody') # 가끔 ID가 이렇게 생긴 녀석도 존재합니다...
            body = body[0].text.replace('\n','')
            
            all_results[i]['link'] = link
            all_results[i]['pubdate'] = pubdate
            all_results[i]['title'] = title
            all_results[i]['body'] = body
            time.sleep(1)
            i += 1
        

    df = pd.DataFrame(all_results).T
    folder_path = f"G:/내 드라이브/4-1/텍데분/크롤링/크롤링폴더/{k}"
    now = datetime.datetime.now() 
    file_path = os.path.join(folder_path, f'{k}_{now.strftime("%Y%m%d")}_{start}.csv')

    # 지정된 경로에 CSV 파일 저장
    df.to_csv(file_path, encoding='utf-8-sig', index=False)

driver.quit()