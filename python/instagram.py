import logging
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

#################### TEST CONSTANTS ####################


LANDING_PAGE_URL = "https://www.instagram.com/"
LOGIN_SUBMIT = "//div[contains(text(),'Log In')]"
# LOGIN_SUBMIT = ("//button[@id='u_0_f' and "
#                 "contains(text(),'Log In')]"
#                 )

#LOGIN_EMAIL_XPATH = "//input[contains(text(),'Phone number, username, or email')]"
#LOGIN_PASSWORD_XPATH = "//input[contains(text(),'Password')]"

LOGIN_EMAIL_XPATH = "//input[@name='username']"
LOGIN_PASSWORD_XPATH = "//input[@name='password']"

MESSAGES_XPATH = "//body/div[@id='react-root']/section[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/a[1]/*[1]"

HEADER_DROPDOWN_BUTTON = "//body/div[@id='react-root']/section[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[5]/span[1]/img[1]"
LOGOUT_BUTTON_XPATH = "//div[contains(text(),'Log Out')]"


def login(driver, timeout_sec):
    """This logs into the Instagram and returns the driver in the new
        state.
        """
    INST_EMAIL = "testgoldqa@gmail.com"  # input('Enter Email:')
    INST_PASS = "testgold1234"  # input('Enter Password:')

    time.sleep(timeout_sec)

    logger.info("[TEST] finding the login email box and filling it in")
    email_box = driver.find_element_by_xpath(LOGIN_EMAIL_XPATH)
    email_box.send_keys(INST_EMAIL)

    logger.info("[TEST] finding the login pass box and filling it in")
    pass_box = driver.find_element_by_xpath(LOGIN_PASSWORD_XPATH)
    pass_box.send_keys(INST_PASS)

    # click on the submit button
    time.sleep(timeout_sec)

    logger.info("[TEST] finding login submit button")
    login_submit = driver.find_element_by_xpath(LOGIN_SUBMIT)
    login_submit.click()
    time.sleep(timeout_sec)
    return driver


def view_messages(driver, timeout_sec):
    """This shows  groups page info"""

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
    logger.info("[TEST] finding header dropdown button")
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
        logger.info("[RUNNER] viewing messages info")
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
