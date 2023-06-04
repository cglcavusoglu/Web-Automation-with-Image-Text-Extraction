from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import cv2
import pytesseract

path = "C:/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

url = "https://e-okul.meb.gov.tr/IlkOgretim/Veli/IOV00001.aspx?strTkn=8420b145-7d4f-41"

def get_image_string():
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    img = cv2.imread("c.png")
    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (h, w) = gry.shape[:2]
    gry = cv2.resize(gry, (w*2, h*2))
    cls = cv2.morphologyEx(gry, cv2.MORPH_CLOSE, None)
    thr = cv2.threshold(cls, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    txt = pytesseract.image_to_string(thr)
    print("Text ----> "+txt)
    return txt

driver.get(url)

tc = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td[1]/table/tbody/tr/td[3]/table/tbody/tr[2]/td/table[1]/tbody/tr[3]/td[3]/input')
no=driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td[1]/table/tbody/tr/td[3]/table/tbody/tr[2]/td/table[1]/tbody/tr[4]/td[3]/input')
image = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td[1]/table/tbody/tr/td[3]/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td[3]/img')
dogrulama = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td[1]/table/tbody/tr/td[3]/table/tbody/tr[2]/td/table[1]/tbody/tr[2]/td[3]/input')

with open('c.png', 'wb') as file:
    file.write(image.screenshot_as_png)
tc.send_keys("tc")
no.send_keys("321")

dogrulama_text = get_image_string()
dogrulama.send_keys(dogrulama_text)
