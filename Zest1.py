from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.find_element_by_id("twotabsearchtextbox").send_keys("iPhone XR (64GB)")
driver.find_element_by_xpath("//div[@id='nav-search']/form[@role='search']//input[@value='Go']").click()
driver.find_element_by_xpath("/html//div[@id='search']/div[1]/div[2]/div[@class='sg-col-inner']/span[4]/div[@class='s-result-list s-search-results sg-row']/div[1]/div/span//h2/a[@href='/Apple-iPhone-XR-64GB-White/dp/B07JGXM9WN/ref=sr_1_1?keywords=iPhone+XR+%2864GB%29&qid=1581656010&smid=A14CZOWI0VEHLG&sr=8-1']/span[.='Apple iPhone XR (64GB) - White']").click()
price = driver.find_element_by_xpath("/html//div[@id='search']/div[1]/div[2]/div[@class='sg-col-inner']/span[4]/div[@class='s-result-list s-search-results sg-row']/div[1]/div[@class='sg-col-inner']/span//div[@class='a-section a-spacing-none a-spacing-top-small']/div[2]/div[@class='a-row']/a[@href='/Apple-iPhone-XR-64GB-White/dp/B07JGXM9WN/ref=sr_1_1?keywords=iPhone+XR+%2864GB%29&qid=1581656010&smid=A14CZOWI0VEHLG&sr=8-1']/span[@class='a-price']//span[@class='a-price-whole']").click()

if price is not None:
    #print(price)

driver.get("https://www.flipkart.com/")
time.sleep(6)
driver.find_element_by_xpath("//div[@class='_2ISNhP _3AOFWO']//button[.='✕']").click()
driver.find_element_by_name("q").send_keys("iPhone XR (64GB)")
driver.find_element_by_xpath("//path[class='_2BhAHa']//path[style='outline: orange dashed 2px !important; outline-offset: -1px !important;']").click()
driver.find_element_by_xpath("//svg[@viewBox='0 0 17 18']").click()
driver.find_element_by_xpath("//div[@class='_3wU53n']//div[xpath='1']").click()
price1 = driver.find_element_by__xpath("/html//div[@id='container']/div/div[3]//div[@class='_1HmYoV hCUpcT']/div[2]/div[2]/div[@class='_3O0U0u']/div/div[@class='_1UoZlX']/a[@href='/apple-iphone-xr-white-64-gb/p/itmf9z7zhgzkmgm3?pid=MOBF9Z7ZUYC2EYQD&lid=LSTMOBF9Z7ZUYC2EYQDVYJTIC&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=c7d35709-7a4d-49c9-8daf-0c8cce76e9ac.MOBF9Z7ZUYC2EYQD.SEARCH&ppt=sp&ppn=sp&ssid=qk301xxdeo0000001581658197334&qH=c6dc15c7d218b4f3']//div[@class='_1vC4OE _2rQ-NK']")
if price > price1:
    print('Amazon has less price')
else:
    print('Flipkart has less price')


