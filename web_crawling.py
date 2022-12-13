from bs4 import BeautifulSoup
import requests, openpyxl
from datetime import time
from datetime import date
from datetime import datetime

news_date = (date.today())
ns_date = news_date.strftime("%d/%b/%Y")
n_date = news_date.strftime("%A")
update_time = datetime.now()
up_time = (update_time.strftime("%H:%M:%S:%p"))

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Latest News"
sheet.append(["Location", "Headlines", "Author", 'Date', 'Day', 'Time'])

try:
    responce = requests.get("https://www.thehindu.com/latest-news/")
    soup = BeautifulSoup(responce.text, "html.parser")
    #print(soup)
    page = soup.find('ul', class_="timeline-with-img").find_all("li")

    for record in page:
        #print(rec)
        title = record.find("h3", class_="title").a.text
        author_name = record.find("div", class_="author-name").a.text
        label = record.find("div", class_="label").a.text
        time_of_published = record.find("div", class_='news-time time')
        #time1 = rec.find('div', class_= 'news-time time' data-published ="2022-12-13T09:02:00+05:30")
        #print(time_of_published)

        #print(time1)

        if sheet.append([label, title, author_name, ns_date, n_date, up_time]) in sheet:
            sheet.remove([label, title, author_name, ns_date, n_date, up_time])
            sheet.append([label, title, author_name, ns_date, n_date, up_time])


except Exception as e:
    print(e)

print(sheet)
excel.save("Update_News.xlsx")

print("***Update the content successfully!!!")
