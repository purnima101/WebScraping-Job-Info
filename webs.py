from bs4 import BeautifulSoup
import requests
import time
print('The skill u need')
s=input('>')
print("Filtering...")

def find_jobs():
    t1=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup=BeautifulSoup(t1,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        dates=job.find('span',class_='sim-posted').text
        if 'few' in dates:
            company=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            link=job.header.h2.a['href']
            if s in skills:
                with open(f'D:\Python Practice\Webscraping\{index}.txt','w') as f:
                    f.write(f'Comapny: {company.strip()} \n')
                    f.write(f'Skills: {skills.strip()} \n')
                    f.write(f'Dates: {dates.strip()}\n')
                    f.write(f'Link: {link}\n \n')

                    print(f'Comapny: {company.strip()}')
                    print(f'Skills: {skills.strip()}')
                    print(f'Dates: {dates.strip()}')
                    print(f'Link: {link}')

                    print('\n')

if __name__=='__main__':
    while True:
        find_jobs()
        print('Waiting..')
        time.sleep(1000)
        #to run the program every 1000 sec

