from retrieve_titles import retrieve_from_siggraph
from selenium import webdriver
from os import path
from msedge.selenium_tools import Edge, EdgeOptions

if __name__ == "__main__":
    # define selenium web crawler
    cur_path = path.dirname(path.abspath(__file__))
    # print(cur_path)
    chromedriver_path = cur_path + "/chromedriver_mac_97"
    microsoftdriver_path = cur_path + "/msedgedriver"
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    # driver = webdriver.Chrome(options=option, executable_path=chromedriver_path)
    desired_cap = {}
    driver = webdriver.Edge(microsoftdriver_path, capabilities=desired_cap)
    web = "https://dl.acm.org/toc/tog/2020/39/4" # Siggraph example paper website
    driver.get(web)
    print(retrieve_from_siggraph(driver))