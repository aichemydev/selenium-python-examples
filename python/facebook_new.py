

import logging
import os
import sys
import time

from selenium import webdriver

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    style="{",
    format='[{levelname:1.1} {asctime} {module}:{lineno}] {message}',
    datefmt='%y%m%d %H:%M:%S',
)


############# Import env variables ############

FB_EMAIL, FB_PASS = os.getenv('FB_EMAIL'), os.getenv('FB_PASS')
if not FB_EMAIL or not FB_PASS:
    logger.error('Facebook email and/or password environment variables could not be imported.')
    raise Exception


#################### TEST CONSTANTS ####################


LANDING_PAGE_URL = "https://www.facebook.com/"
LOGIN_EMAIL_XPATH = "//input[@id='email']"
LOGIN_PASSWORD_XPATH = "//input[@id='pass']"
LOGIN_SUBMIT_XPATH = "//button[contains(text(),'Log In')]"  # "//button[id='u_0_f']"
#GROUPS_XPATH="//body/div[@id='mount_0_0']/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[4]/span[1]/div[1]/a[1]"
GROUPS_XPATH = "//span[contains(text(),'Groups')]" # newer design "//div[contains(text(),'Groups')]" # older design

HEADER_DROPDOWN_BUTTON = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/span[1]/div[1]/div[1]/img[1]"
#HEADER_DROPDOWN_BUTTON="//body/div[@id='mount_0_0']/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/span[1]/div[1]/div[1]"
#HEADER_DROPDOWN_BUTTON = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[5]/span[1]" # newer design "//div[contains(text(),'Account Settings')]" # older design


LOGOUT_BUTTON_XPATH = "//span[contains(text(),'Log Out')]"


def login(driver, timeout_sec):
    """This logs into the Facebook and returns the driver in the new
        state.
    """

    time.sleep(timeout_sec)

    logger.info("[TEST] finding the login email box and trying to break its xpath")

    email_box = driver.find_element_by_xpath(LOGIN_EMAIL_XPATH)

    # ########### breaking by changing id attribute ###########
    #
    # old_id = email_box.get_attribute("id")
    # logger.info(f"[TEST] Current ID of the cart item web element: {old_id}")
    # time.sleep(timeout_sec)
    # new_id = "email_address"
    # logger.info(f"[TEST] Changing ID of the cart item web element to: {new_id}")
    # #driver.execute_script("arguments[0].setAttribute('id', arguments[1])", email_box, new_id)
    # driver.execute_script("arguments[0].id = arguments[1]", email_box, new_id)
    # time.sleep(timeout_sec)
    # logger.info(f"[TEST] ID of the cart item web element has been succesfully changed to: {email_box.get_attribute('id')}")
    #
    # time.sleep(timeout_sec*2)
    # logger.info("[TEST] finding the login email box after the modification and trying to fill it in")
    # email_box=driver.find_element_by_xpath(LOGIN_EMAIL_XPATH)
    #
    # ##########

    email_box.send_keys(FB_EMAIL)

    logger.info("[TEST] finding the login pass box and trying to break its xpath")

    pass_box = driver.find_element_by_xpath(LOGIN_PASSWORD_XPATH)

    # ########### breaking by changing id attribute ###########
    #
    # old_id = pass_box.get_attribute("id")
    # logger.info(f"[TEST] Current ID of the cart item web element: {old_id}")
    # time.sleep(timeout_sec)
    # new_id = "password"
    # logger.info(f"[TEST] Changing ID of the cart item web element to: {new_id}")
    # #driver.execute_script("arguments[0].setAttribute('id', arguments[1])", pass_box, new_id)
    # driver.execute_script("arguments[0].id = arguments[1]", pass_box, new_id)
    # time.sleep(timeout_sec)
    # logger.info(f"[TEST] ID of the cart item web element has been succesfully changed to: {pass_box.get_attribute('id')}")
    #
    # time.sleep(timeout_sec*2)
    # logger.info("[TEST] finding the login pass box after the modification and trying to fill it in")
    # pass_box = driver.find_element_by_xpath(LOGIN_PASSWORD_XPATH)
    #
    # ##########

    pass_box.send_keys(FB_PASS)

    # click on the submit button
    logger.info("[TEST] finding the login submit button")
    #login_submit = driver.find_element_by_xpath(LOGIN_SUBMIT_XPATH)
    login_submit = driver.find_element_by_id('u_0_f')

    ########### breaking by changing id attribute ###########

    old_id = login_submit.get_attribute("id")
    logger.info(f"[TEST] Current ID of the cart item web element: {old_id}")
    time.sleep(timeout_sec)
    new_id = "U_0_F"
    logger.info(f"[TEST] Changing ID of the cart item web element to: {new_id}")
    #driver.execute_script("arguments[0].setAttribute('id', arguments[1])", pass_box, new_id)
    driver.execute_script("arguments[0].id = arguments[1]", login_submit, new_id)
    time.sleep(timeout_sec)
    logger.info(f"[TEST] ID of the login has been succesfully changed to ---> {login_submit.get_attribute('id')}")

    time.sleep(timeout_sec*2)
    logger.info("[TEST] finding the login button the modification and trying to fill it in")
    login_submit = driver.find_element_by_id(f"{old_id}")

    ##########

    time.sleep(timeout_sec)
    login_submit.click()
    time.sleep(timeout_sec)

    return driver


def view_groups(driver, timeout_sec):
    """This shows  groups page info"""

    time.sleep(timeout_sec)
    logger.info("[TEST] finding groups button")

    groups_button = driver.find_element_by_xpath(GROUPS_XPATH)
    logger.info("[TEST] clicking groups button")
    groups_button.click()

    time.sleep(timeout_sec)
    return driver


def logout(driver, timeout_sec):
    """This logs out from the UI and returns the driver in the new
           state. """

    time.sleep(timeout_sec)
    logger.info("[TEST] finding header dropdown button")
    header_dropdown_button = driver.find_element_by_xpath(HEADER_DROPDOWN_BUTTON)

    logger.info("[TEST] clicking on dropdown button")
    header_dropdown_button.click()

    # clicking on the logout button
    time.sleep(timeout_sec)

    logger.info("[TEST] finding logout button")
    logout_button = driver.find_element_by_xpath(LOGOUT_BUTTON_XPATH)

    ########### breaking by changing the xpath ###########

    old_text = logout_button.get_attribute('outerText')
    logger.info(f"[TEST] Current text of the logout button web element: {old_text}")
    logger.info(f"[TEST] Current outer HTML of the logout button web element: {logout_button.get_attribute('outerHTML')}")
    time.sleep(timeout_sec)
    new_text = "<<<log_out>>>"
    logger.info(f"[TEST] Changing text of the logout button web element to: {new_text}")
    #driver.execute_script("arguments[0].setAttribute('outerText', arguments[1])", logout_button, new_text)
    driver.execute_script("arguments[0].innerText = arguments[1]", logout_button, new_text)
    time.sleep(timeout_sec*3)
    logger.info(f"[TEST] Text of the logout button web element has been succesfully changed to: {logout_button.get_attribute('outerText')}")

    time.sleep(timeout_sec)
    logger.info("[TEST] finding the logout button after the modification")
    logout_button = driver.find_element_by_xpath(LOGOUT_BUTTON_XPATH)

    ##########

    time.sleep(timeout_sec)
    logger.info("[TEST] Clicking on the Logout button")
    logout_button.click()

    time.sleep(timeout_sec)
    return driver


def run_test(timeout_sec):
    """ This runs the test. """

    driver = None
    exit_code = 0

    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        options.add_experimental_option("prefs", { # take care of the notification popup after logging in: https://stackoverflow.com/questions/38684175/how-to-click-allow-on-show-notifications-popup-using-selenium-webdriver
            "profile.default_content_setting_values.notifications": 1 
        })

        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1920, 1080)

        # get to the landing page
        driver.get(LANDING_PAGE_URL)

        # login
        logger.info("[RUNNER] doing login")
        login(driver, timeout_sec)
        logger.info("[RUNNER] login done")


        # last launch info
        logger.info("[RUNNER] viewing groups info")
        view_groups(driver, timeout_sec)

        # logout
        logger.info("[RUNNER] doing logout")
        logout(driver, timeout_sec)
        logger.info("[RUNNER] logout done")


    except Exception:

        logger.exception("Ran into exception when running test.")
        exit_code = 1
        raise

    finally:

        if driver is not None:
            logger.info("[RUNNER] waiting to close the window")
            time.sleep(1.0)
            driver.close()
            logger.info("[RUNNER] window close done, waiting for driver quit")
            driver.quit()
            logger.info("[RUNNER] driver quit done")

        logger.info(f"[RUNNER] test run complete. exit code: {exit_code}")
        sys.exit(exit_code)


if __name__ == "__main__":
    run_test(2.0)
