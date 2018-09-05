from requests import get
from bs4 import BeautifulSoup as soup
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer, QTime
import time


app = QtWidgets.QApplication([])
dlg = uic.loadUi("atomic_time.ui")

my_url = "https://www.timeanddate.com/time/international-atomic-time.html"
#get page in english
page_html = get(my_url,headers = {"Accept-Language": "en-US, en;q=0.5"}) #better way


page_soup = soup(page_html.content,"html.parser")


def refresh():
    hours_mins = page_soup.findAll("span", id="hourmin0")
    seconds = page_soup.findAll("span", id="sec0")
    date = page_soup.findAll("p", id="date0")[0]
    ahead = f"{date.next_sibling}{date.next_sibling.next_sibling.text}{date.next_sibling.next_sibling.next_sibling}"
    dlg.label.setText(hours_mins[0].text + ":" + seconds[0].text)
    dlg.label_2.setText(ahead)





dlg.show()
refresh()
app.exec()






