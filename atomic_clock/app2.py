import sys
from requests import get
from bs4 import BeautifulSoup as soup
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic
from PyQt5.QtCore import QTimer




my_url = "https://www.timeanddate.com/time/international-atomic-time.html"
#get page in english
page_html = get(my_url,headers = {"Accept-Language": "en-US, en;q=0.5"}) #better way


page_soup = soup(page_html.content,"html.parser")

class DemoApp(QDialog):

    def __init__(self, *args):
        super(DemoApp, self).__init__(*args)

        uic.loadUi("atomic_time.ui", self)
##########################################################################
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)  ####         REFRESH
        self.timer.start(1000)
##########################################################################

    def update_time(self):
        page_html = get(my_url, headers={"Accept-Language": "en-US, en;q=0.5"})  # better way
        page_soup = soup(page_html.content, "html.parser")
        hours_mins = page_soup.findAll("span", id="hourmin0")
        seconds = page_soup.findAll("span", id="sec0")
        date = page_soup.findAll("p", id="date0")[0]
        ahead = f"{date.next_sibling}{date.next_sibling.next_sibling.text}{date.next_sibling.next_sibling.next_sibling}"
        self.label.setText(hours_mins[0].text + ":" + seconds[0].text)
        self.label_2.setText(ahead)




app = QApplication(sys.argv)
widget = DemoApp()
widget.show()
sys.exit(app.exec_())



