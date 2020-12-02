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
    raise Exception('Facebook email and/or password environment variables could not be imported.')

#################### TEST CONSTANTS ####################


LANDING_PAGE_URL = "https://www.twitter.com/"

LOGIN_EMAIL_XPATH = "//input[@name='session[username_or_email]']"
LOGIN_PASSWORD_XPATH = "//input[@name='session[password]']"


LOGIN_BUTTON = "//button[contains(text(),'Log In')]"
LOGIN_SUBMIT_BUTTON = "//body/div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]"

MESSAGES_XPATH = "//span[contains(text(),'Messages')]"

HEADER_DROPDOWN_BUTTON = "//header/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]"
LOGOUT_BUTTON_XPATH = "//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[2]/div[1]/div[1]"
LOGOUT_SUBMIT_BUTTON_XPATH = "//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]"


def login(driver, timeout_sec):
    """This logs into the Twitter and returns the driver in the new
        state.
        """

    logger.info("[TEST] finding the login button")
    login_button = driver.find_element_by_xpath(LOGIN_BUTTON)
    login_button.click()
    time.sleep(timeout_sec)

    logger.info("[TEST] finding the login email box and filling it in")
    #email_box = driver.find_element_by_name("session[username_or_email]")
    email_box = driver.find_element_by_xpath(LOGIN_EMAIL_XPATH)
    email_box.send_keys(TW_EMAIL)

    logger.info("[TEST] finding the login pass box and filling it in")
    pass_box = driver.find_element_by_xpath(LOGIN_PASSWORD_XPATH)  # "session[password]"
    pass_box.send_keys(TW_PASS)

    logger.info("[TEST] finding the login submit button")
    login_submit = driver.find_element_by_xpath(LOGIN_SUBMIT_BUTTON)
    login_submit.click()
    time.sleep(timeout_sec)

    return driver


def view_messages(driver, timeout_sec):
    """This shows messages"""

    time.sleep(timeout_sec)
    logger.info("[TEST] finding messages button")

    messages_button = driver.find_element_by_xpath(MESSAGES_XPATH)
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

    logger.info("[TEST] clicking on dropdown button")
    header_dropdown_button.click()

    # clicking on the logout button
    time.sleep(timeout_sec)

    logger.info("[TEST] finding logout button")
    logout_button = driver.find_element_by_xpath(LOGOUT_BUTTON_XPATH)

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
