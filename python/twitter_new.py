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

TW_EMAIL, TW_PASS = os.getenv('TW_EMAIL'), os.getenv('TW_PASS')
if not TW_EMAIL or not TW_PASS:
    logger.error('Twitter email and/or password environment variables could not be imported.')
    raise Exception


#################### TEST CONSTANTS ####################


LANDING_PAGE_URL = "https://www.twitter.com/"

LOGIN_EMAIL_XPATH = "//input[@name='session[username_or_email]']"
LOGIN_PASSWORD_XPATH = "//input[@name='session[password]']"

LOGIN_BUTTON = "//a[contains(string(.), 'Log in')]"
LOGIN_SUBMIT_BUTTON ="//div[@role='button']"

MESSAGES_XPATH = "//a[contains(text(),'Messages')]"

HEADER_DROPDOWN_BUTTON = "//header/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]"
LOGOUT_BUTTON_XPATH = "//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[2]/div[1]/div[1]"
LOGOUT_SUBMIT_BUTTON_XPATH = "//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]"


def login(driver, timeout_sec):
    """This logs into the Twitter and returns the driver in the new
        state.
        """

    time.sleep(timeout_sec)
    logger.info("[TEST] finding the login button")
    login_button = driver.find_element_by_xpath(LOGIN_BUTTON)

    login_button.click()
    time.sleep(timeout_sec)
    logger.info("[TEST] finding the login email box and filling it in")
    # email_box = driver.find_element_by_name("session[username_or_email]")
    email_box = driver.find_element_by_xpath(LOGIN_EMAIL_XPATH)

    # ########### breaking by changing a name attribute(fails to heal) ###########
    #
    # old_name = email_box.get_attribute('name')
    # logger.info(f"[TEST] Current name of the email_box: {old_name}")
    # logger.info(
    #     f"[TEST] Current outer HTML of the email_box: {email_box.get_attribute('outerHTML')}")
    # time.sleep(timeout_sec)
    # new_name = "session[username_or_email_or_phone]"
    # logger.info(f"[TEST] Changing name of the email_box to: {new_name}")
    # driver.execute_script("arguments[0].name = arguments[1]", email_box, new_name)
    # time.sleep(timeout_sec * 2)
    # logger.info(
    #     f"[TEST] Name of the email_box has been succesfully changed to ---> {email_box.get_attribute('name')}")
    #
    # logger.info("[TEST] finding the email_box after the modification")
    # email_box = driver.find_element_by_name(old_name)
    #
    # ###########

    email_box.send_keys(TW_EMAIL)

    logger.info("[TEST] finding the login pass box and filling it in")
    # pass_box = driver.find_element_by_name("session[password]")  # "session[password]"
    pass_box = driver.find_element_by_xpath(LOGIN_PASSWORD_XPATH)  # "session[password]"
    pass_box.send_keys(TW_PASS)

    time.sleep(timeout_sec)
    logger.info("[TEST] finding the login button")
    login_submit = driver.find_element_by_xpath(LOGIN_SUBMIT_BUTTON)

    login_submit.click()
    time.sleep(timeout_sec)

    return driver


def view_messages(driver, timeout_sec):
    """This shows messages"""

    time.sleep(timeout_sec)
    logger.info("[TEST] finding messages button")

    messages_button = driver.find_element_by_xpath(MESSAGES_XPATH)

    ########### breaking by changing aan ttribute ###########

    old_id = messages_button.get_attribute("data-testid")
    logger.info(
        f"[TEST] Current outer HTML of the messages_button web element: {messages_button.get_attribute('outerHTML')}")
    logger.info(f"[TEST] Current data-testid of the messages_button: {old_id}") #AppTabBar_DirectMessage_Link

    new_id = "AppTabBar_Message_Link"
    logger.info(f"[TEST] Changing data-testid of the messages_button to: {new_id}")
    driver.execute_script("arguments[0].setAttribute('data-testid', arguments[1])", messages_button, new_id)
    time.sleep(timeout_sec)
    logger.info(
        f"[TEST] Id of the messages_button has been succesfully changed to ---> {messages_button.get_attribute('data-testid')}")

    time.sleep(timeout_sec)
    logger.info("[TEST] finding the messages_button after the modification")
    messages_button = driver.find_element_by_xpath(f"//a[@data-testid='{old_id}']")

    ##########

    time.sleep(timeout_sec)
    logger.info("[TEST] clicking messages button")
    messages_button.click()

    time.sleep(timeout_sec)
    return driver


def logout(driver, timeout_sec):
    """This logs out from the UI and returns the driver in the new
           state. """

    time.sleep(timeout_sec)
    logger.info("[TEST] finding header dropdown button at the left bottom")
    header_dropdown_button = driver.find_element_by_xpath(HEADER_DROPDOWN_BUTTON)

    logger.info("[TEST] clicking on a dropdown button")
    header_dropdown_button.click()

    # clicking on the logout button
    time.sleep(timeout_sec)

    logger.info("[TEST] finding logout button")
    logout_button = driver.find_element_by_xpath(LOGOUT_BUTTON_XPATH)

    ########### breaking by changing the xpath ###########

    old_text = logout_button.get_attribute('outerText')
    logger.info(f"[TEST] Current text of the logout button web element: {old_text}")
    logger.info(
        f"[TEST] Current outer HTML of the logout button web element: {logout_button.get_attribute('outerHTML')}")
    time.sleep(timeout_sec)
    new_text = "<<<log_out>>>"
    logger.info(f"[TEST] Changing text of the logout button web element to: {new_text}")
    # driver.execute_script("arguments[0].setAttribute('outerText', arguments[1])", logout_button, new_text)
    driver.execute_script("arguments[0].innerText = arguments[1]", logout_button, new_text)
    time.sleep(timeout_sec)
    logger.info(
        f"[TEST] Text of the logout button web element has been succesfully changed to: {logout_button.get_attribute('outerText')}")

    time.sleep(timeout_sec)
    logger.info("[TEST] finding the logout button after the modification")
    logout_button = driver.find_element_by_xpath(LOGOUT_BUTTON_XPATH)

    ##########

    time.sleep(timeout_sec)
    logger.info("[TEST] Clicking on the Logout button")
    logout_button.click()

    time.sleep(timeout_sec)
    logger.info("[TEST] finding logout submit button")
    logout_button = driver.find_element_by_xpath(LOGOUT_SUBMIT_BUTTON_XPATH)

    time.sleep(timeout_sec)
    logger.info("[TEST] Clicking on the Logout submit button")
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
        options.add_experimental_option("prefs", {
            # take care of the notification popup after logging in: https://stackoverflow.com/questions/38684175/how-to-click-allow-on-show-notifications-popup-using-selenium-webdriver
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
        logger.info("[RUNNER] viewing messages")
        view_messages(driver, timeout_sec)

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

