import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

url =  "https://www.amazon.in/Apple-iPhone-13-128GB-Blue/dp/B09G9BL5CP/ref=sr_1_1_sspa?crid=2PV8WIFQB2571&dib=eyJ2IjoiMSJ9.QEJlVZTznGj9FcganUjqR0ggF84CdwVy2IP_nOVV8Yd8pK5EVBwC5T3JHAQNKHSrgnxLrgfQxZakTAd1WTLg6s_IiqnqoY8M1DUDrBx7PWFSWDVYAi87027jZhBHtJW_gX49D3ZpXgFMSw7PM_LMN05ZuowH0qndrfUh5E3xXk0XTlktG9NVf-z1s86aVak270lihfNf8IzDkgPOWlbvlTGZh7KoiNSTyxzf74UP40s.jFZ4k1K36UxboCNVQEJ07-D-yRzdcwzM7H5UpWBA0SI&dib_tag=se&keywords=apple&qid=1712909587&sprefix=apple%2Caps%2C281&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

page = requests.get(url, headers = headers)
soup = BeautifulSoup(page.content, "html.parser")
price = soup.find("span", class_="price-whole")

print(price)

4
