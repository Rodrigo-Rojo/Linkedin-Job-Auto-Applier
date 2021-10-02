from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

LOGIN = "EMAIL"
PASS = "PASS"
LINK = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
chrome_driver_path = "YOUR PATH"
driver = webdriver.Chrome(chrome_driver_path)

driver.get(LINK)
sleep(1)
sign_in_btn1 = driver.find_element_by_class_name('nav__button-secondary')
sign_in_btn1.click()
sleep(1)

username = driver.find_element_by_id('username')
username.send_keys(LOGIN)
password = driver.find_element_by_id('password')
password.send_keys(PASS)
sign_in_btn2 = driver.find_element_by_class_name('btn__primary--large')
sign_in_btn2.click()
sleep(3)

jobs = driver.find_elements_by_class_name('job-card-container--clickable')

for job in jobs:
    job.click()
    sleep(1)
    try:
        # driver.find_element_by_class_name('jobs-apply-button').click()
        driver.find_element_by_css_selector('.jobs-unified-top-card__content--two-pane button.jobs-apply-button').click()
        sleep(1)
        driver.find_element_by_css_selector('form .artdeco-button--primary').click()
        sleep(1)
        driver.find_element_by_css_selector('form .artdeco-button--primary').click()
        sleep(1)
        driver.find_element_by_css_selector('.jobs-easy-apply-content .artdeco-button--primary').click()
        sleep(1)

        try:
            driver.find_element_by_class_name('artdeco-modal__dismiss').click()
            sleep(1)
            driver.find_element_by_css_selector('.artdeco-modal__actionbar .artdeco-button--primary').click()
        except NoSuchElementException:
            print('Applied!')
            try:
                driver.find_element_by_class_name('artdeco-modal__dismiss').click()
            except NoSuchElementException:
                print('There was no questions')
        else:
            print('Filling out a form is requied!')

    except NoSuchElementException:
        print('Already applied')
    except ElementNotInteractableException:
            print('LinkedIn application loading error')

driver.close()
