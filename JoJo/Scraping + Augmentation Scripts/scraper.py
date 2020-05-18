import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import BytesIO
from time import sleep

# Note: In the time since the JoJo wiki appears to have replaces the images on it's character template pages
# with substantially lower resolution ones. Thus this scraper now returns images way more upscaled then was
# actually used in model tranining.


def save_element(chrome, element, filename):
    location = element.location_once_scrolled_into_view
    size = element.size
    png = chrome.get_screenshot_as_png()  # saves screenshot of entire page

    im = Image.open(BytesIO(png))  # uses PIL library to open image in memory

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    im = im.crop((left, top, right, bottom))  # defines crop points
    im = im.resize((512, 512))
    im.save(f'images\\{filename}.png')


def capture_images():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    count = 0

    for part in range(1, 10):
        print(part)
        url = f"https://jojo.fandom.com/wiki/Template:Part_{str(part)}_Character_Table"
        if part == 9:
            url = "https://jojo.fandom.com/wiki/Template:One_Shot_Character_Table"
        try:
            driver.get(url)
        except Exception as e:
            print(e)
        element = driver.find_element_by_class_name('wds-global-navigation-wrapper')
        driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)
        diamond = driver.find_element_by_class_name("diamonds")
        pics = diamond.find_elements_by_tag_name("div")
        for i in range(len(pics)):
            if i % 2 != 1:
                continue
            save_element(driver, pics[i], str(count))
            count += 1

    driver.close()


if __name__ == "__main__":
    assert len(sys.argv) == 1
    capture_images()

