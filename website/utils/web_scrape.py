import time
import itertools
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
# webdriver_service = Service(f"/home/prabal/python/web-scraping/chromedriver/stable/chromedriver")

# Set path to chromedriver as per your configuration
webdriver_service = Service(f"/home/prabal/python/web-scraping/chromedriver/stable/chromedriver")

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
URL = "https://proshore.eu/resources/"



def scroll_down(driver):
    """A method for scrolling the page."""
    
    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to the bottom. 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load the page.
        time.sleep(5)
        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            elements = driver.find_elements(By.CLASS_NAME, "playground-item")
            return driver
        last_height = new_height  

def find_elements_by_class_name(driver, class_name: str):     
    elements = driver.find_elements(By.CLASS_NAME, class_name)
    return elements

def combine_all_elements(list_of_lists: List[List]) -> List:
    flat_list = list(itertools.chain.from_iterable(list_of_lists))
    return flat_list

def get_blog_details_link_from_elements(elements: List):
    all_blog_details: List = []
    for element in elements:
        blog_detail_link = element.find_element(By.TAG_NAME, "a").get_attribute("href")

        try:
            reading_time = element.find_element(By.CLASS_NAME, "playground-read-time-text").text
        except NoSuchElementException:
            reading_time = 0

        blog_details = {"reading_time": reading_time, "blog_detail_link": blog_detail_link }
        all_blog_details.append(blog_details)
    
    return all_blog_details


def get_blog_description_from_element(element):
    try:
        description_text = element.find_element(By.CLASS_NAME, "playground-content-wrapper").text
    except NoSuchElementException:
        print("Description element not found")
        description_text = ""
    
    return description_text


def get_title_from_element(element):
    try:
        title_text = element.find_element(By.CLASS_NAME, "playground-single-title").text
    except NoSuchElementException:
        print("Title not Found")
        title_text = ""
    
    return title_text

def get_author_details_from_element(element):
    try:
        author_element = element.find_element(By.CLASS_NAME, "playground-single-author")
        author_name = author_element.find_element(By.CLASS_NAME, "playground-author-name").text
        author_designation = author_element.find_element(By.CLASS_NAME, "playground-author-description").text
        try:
            author_image_url = author_element.find_element(By.CLASS_NAME, "playground-author-image").find_element(By.TAG_NAME, "img").get_attribute("src")
        except NoSuchElementException:
            author_image_url = ""
            print("No image URL")
        
        return author_name, author_designation, author_image_url
    except NoSuchElementException:
            print("No author element")

def get_blog_image_url_from_element(element):
    try:
        blog_image_url = element.find_element(By.CLASS_NAME, "playground-feature-img-wrap").find_element(By.TAG_NAME, "img").get_attribute("src")
    except NoSuchElementException:
        print("Image URL not found")
        blog_image_url = ""
    
    return blog_image_url
    
def get_element_by_class_name_from_driver(driver, class_name):
    try:
        element = driver.find_element(By.CLASS_NAME, class_name)
    except NoSuchElementException:
        print("No such element")
        element = None
    
    return element

def get_all_blog_details(all_blog_links: List):
    # breakpoint()
    all_blog_details = []
    for item in all_blog_links:
        blog_details = {}
        reading_time = item["reading_time"]
        blog_details["reading_time"] = reading_time
        url = item["blog_detail_link"]
        driver.get(url)
        playground_container_element = get_element_by_class_name_from_driver(driver, "playground-container")
        if playground_container_element == None:
            print("No element found")
            continue
        blog_details["title"] = get_title_from_element(playground_container_element)
        description_text = get_blog_description_from_element(playground_container_element)
        blog_details["description"] = description_text
        blog_image_url = get_blog_image_url_from_element(playground_container_element)
        blog_details["blog_image_url"] = blog_image_url
        author_name, author_designation, author_image_url = get_author_details_from_element(playground_container_element)
        blog_details["author_name"], blog_details["author_designation"], blog_details["author_image_url"] = author_name, author_designation, author_image_url
        
        all_blog_details.append(blog_details)
    
    return all_blog_details

def write_json(input):
    pass

def main():
    
    #Set URL
    URL = "https://proshore.eu/resources/"
    # Get page
    driver.get(URL)
    scrolled_down_driver = scroll_down(driver)
    all_elements = find_elements_by_class_name(scrolled_down_driver, "playground-item")
    # breakpoint()
    blog_links_list = get_blog_details_link_from_elements(all_elements)
    
    all_blog_details = get_all_blog_details(blog_links_list)
    # breakpoint()
    print(len(all_blog_details))
    return all_blog_details
   

if __name__ == "__main__":
    main()