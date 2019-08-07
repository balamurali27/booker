from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#  TODO: fetch url from command line arg <07-08-19, Balamurali M> # 
#  url = "https://www.flipkart.com/redmi-note-7-pro-neptune-blue-64-gb/p/itmfegkx8nbcze6t?pid=MOBFDXZ376XRTZXH&srno=s_1_3&otracker=search&otracker1=search&lid=LSTMOBFDXZ376XRTZXHWRK63O&fm=SEARCH&iid=ac9ac5dd-77e4-427f-811a-00f9f7253d59.MOBFDXZ376XRTZXH.SEARCH&ppt=SearchPage&ppn=Search&ssid=9s2p9zmio0i1w2yo1556397932560&qH=c5a4e9df6cc18326"
url = "https://www.flipkart.com/redmi-note-7-sapphire-blue-64-gb/p/itmfdzvf8tptnezu?pid=MOBFDXZ3HJJZH3GG&srno=s_1_1&otracker=search&otracker1=search&lid=LSTMOBFDXZ3HJJZH3GGXELUJI&fm=organic&iid=9c884008-da59-48e5-b724-7c61d6aaedc4.MOBFDXZ3HJJZH3GG.SEARCH&qH=7d4ae70002247cdb"
#  css paths
buyNowButtonCss = "html.fonts-loaded body div#container div div.t-0M7P._3GgMx1._2doH3V div._3e7xtJ div div._1HmYoV.hCUpcT div._1HmYoV._35HD7C.col-5-12._3KsTU0 div.bhgxx2.col-12-12 div._1k1QCg._3QNwd7 ul.row li.col.col-6-12 form button._2AkmmA._2Npkh4._2kuvG8._7UHT_c"
continueButton1Css = "html.fonts-loaded body div#container div div._1Ua1Gl div.row._2e3-6j div._3B4tat div._7XMNLT div._1GRhLX._38vNoF div._3K1hJZ div._2eTL2v div._20egpM div._3cCusG span#to-payment button._2AkmmA._2Q4i61._7UHT_c"
continueButton2Css = "html.fonts-loaded body div#container div div._1Ua1Gl div.row._2e3-6j div._3B4tat div._1GRhLX._38vNoF div._3K1hJZ div.foVA5Z div._1GRhLX._17_fE5 div label._8J-bZE._3C6tOa._1syowc._2i24Q8._1Icwrf div._2o59RR._27CukN div._16sk0J div._3i_pKg div._3MGkT3 button._2AkmmA._37mBT-._7UHT_c"
upiOptionCss = "html.fonts-loaded body div#container div div._1Ua1Gl div.row._2e3-6j div._3B4tat div._1GRhLX._38vNoF div._3K1hJZ div.foVA5Z div._1GRhLX._17_fE5 div label._8J-bZE._3C6tOa._2i24Q8"
#  TODO: generalise home directory or command line options for cookies..or just username and password <07-08-19, Balamurali M> # 
#import firefox developer edition cookies to log in automatically
ffprofile = webdriver.FirefoxProfile("/home/balu/.mozilla/firefox/defaultprofilehere")
browser = webdriver.Firefox(firefox_profile=ffprofile)
#  TODO: add time event here to trigger at certain time <28-04-19 balu> # 
#booking the item
#wait for 5 seconds until the element is found
wait = WebDriverWait(browser, 10)
browser.get(url)
try:
    buyNowButton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, buyNowButtonCss)))
except:
    print("couldn't get buy now button")
buyNowButton.click()
try:
    continueButton1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, continueButton1Css)))
except:
    print("couldn't get continue button")
continueButton1.click()
#  TODO: make radio upi option selection work <28-04-19 balu> # 
#  try:
    #  upiOption = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, upiOptionCss)))
#  except:
    #  print("couldn't get upi option")
#  upiOption.click()
try:
    continueButton2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, continueButton2Css)))
except:
    print("couldn't get 2nd continue button")
continueButton2.click()
