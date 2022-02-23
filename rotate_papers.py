from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time

content = requests.get("http://stackoverflow.com/").content

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://127.0.0.1:5000/?q=generative+information+extraction&rank=time&tags=&pid=&time_filter=&svm_c=0.01&skip_have=no&results_per_page=1&page_number=10")

for pg in range(1,200):
    print(pg)
    driver.get(f"http://127.0.0.1:5000/?q=generative+information+extraction&rank=time&tags=&pid=&time_filter=&svm_c=0.01&skip_have=no&results_per_page=1&page_number={pg}")
    controls = driver.find_element_by_id("controls")
    driver.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, controls)
    time.sleep(2)

controls = driver.find_element_by_id("controls")

driver.execute_script("""
var element = arguments[0];
element.parentNode.removeChild(element);
""", controls)