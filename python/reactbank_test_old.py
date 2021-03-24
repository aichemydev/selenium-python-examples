"""
This is the Java React Bank test implemented in Python.

"""

import logging
import time
import sys

from selenium import webdriver

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    style="{",
    format='[{levelname:1.1} {asctime} {module}:{lineno}] {message}',
    datefmt='%y%m%d %H:%M:%S',
)


####################
## test constants ##
####################

landingPageUrl = "https://demo1.testgold.dev"
landingLoginButtonXPath = (
    "//a[@class='btn btn-primary btn-lg' and "
    "contains(text(),'Click here to log in')]"
)

loginEmailAddr = "email@example.com"
loginPassword = "admin123"

loginEmailXPath = "//input[@name='email']"
loginPasswordXPath = "//input[@name='password']"
loginSubmitXPath = (
    "//button[@class='btn btn-primary' and "
    "contains(text(),'Log in now')]"
)

logoutLinkXPath = (
    "//a[@href='/logout' and "
    "contains(text(),'Logout')]"
)

balanceLinkXPath = "//a//span[contains(text(),'Profile')]"
balanceItemXPath = "//span[.='Balance']"

helpLinkXPath = "//a//span[contains(text(),'Help')]"
helpNameXPath = "//input[@id='name']"
helpEmailXPath = "//input[@id='email']"
helpHomePhoneXPath = "//*[@id='home_phone1234']"
helpOfficePhoneXPath = "//*[@name='office_phone1234']"
helpMobilePhoneXPath = "//*[@class='mobilePhoneClass1234']"
helpSubjectXPath = "//select[@id='subject']"
helpMessageXPath = "//textarea[@id='message']"
helpSendButtonXPath = "//button[@type='submit']"

helpFormItems = {
    "name": "Node User",
    "email": "node@test.org",
    "homePhone": "1-555-650-5555",
    "officePhone": "1-555-440-5555",
    "mobilePhone": "1-555-240-5555",
    "message": "I'm a node user!"
}


###################
## test function ##
###################

def login_to_reactbank(driver, timeout_sec):
    """This logs into the ReactBank website and returns the driver in the new
    state.

    """

    time.sleep(timeout_sec)
    logger.info("[TEST] finding login link")

    # click on the login button
    login_button = driver.find_element_by_xpath(landingLoginButtonXPath)
    logger.info("[TEST] clicking login link")
    login_button.click()

    time.sleep(timeout_sec)

    # fill in the email address and password
    logger.info("[TEST] finding the login email box and filling it in")
    email_box = driver.find_element_by_xpath(loginEmailXPath)
    email_box.send_keys(loginEmailAddr)

    logger.info("[TEST] finding the login password box and filling it in")
    pass_box = driver.find_element_by_xpath(loginPasswordXPath)
    pass_box.send_keys(loginPassword)

    time.sleep(timeout_sec)

    # click on the submit button
    logger.info("[TEST] finding login submit button")
    login_submit = driver.find_element_by_xpath(loginSubmitXPath)
    login_submit.click()

    time.sleep(timeout_sec)

    return driver


def logout_from_reactbank(driver, timeout_sec):
    """This logs out from the React Bank website and returns the driver in the new
    state.

    """

    time.sleep(timeout_sec)

    # find the logout button
    logger.info("[TEST] finding logout link")
    logout_link = driver.find_element_by_xpath(logoutLinkXPath)
    logger.info("[TEST] clicking logout link")
    logout_link.click()

    time.sleep(timeout_sec)
    return driver


def find_balance_on_userpage(driver, timeout_sec):
    """Tries to find and click on the balance item on the user page and get the
    text of the balance item.

    """

    time.sleep(timeout_sec)

    # find the balance item
    logger.info("[TEST] finding Balance link")
    balance_link = driver.find_element_by_xpath(balanceLinkXPath)
    logger.info("[TEST] clicking on Balance link")
    balance_link.click()

    time.sleep(timeout_sec)

    # get the balance item
    logger.info("[TEST] finding Balance item")
    balance_item = driver.find_element_by_xpath(balanceItemXPath)
    balance_text = balance_item.text
    logger.info(f"[TEST] Balance item text is: {balance_text}")

    time.sleep(timeout_sec)
    return driver


def fill_out_help_form(driver, timeout_sec):
    """This tries to find the help page, then fill in the help form, then submit
    it.

    """

    time.sleep(timeout_sec)

    logger.info("[TEST] finding help page link")
    helpform_link = driver.find_element_by_xpath(helpLinkXPath)
    logger.info("[TEST] clicking on help page link")
    helpform_link.click()

    time.sleep(timeout_sec)

    #
    # get the help form items and fill them in
    #
    logger.info("[TEST] filling in help form name item")
    help_name = driver.find_element_by_xpath(helpNameXPath)
    help_name.send_keys(helpFormItems["name"])
    time.sleep(1.0)

    logger.info("[TEST] filling in help form email item")
    help_name = driver.find_element_by_xpath(helpEmailXPath)
    help_name.send_keys(helpFormItems["email"])
    time.sleep(1.0)

    logger.info("[TEST] filling in help form home-phone item")
    help_name = driver.find_element_by_xpath(helpHomePhoneXPath)
    help_name.send_keys(helpFormItems["homePhone"])
    time.sleep(1.0)

    logger.info("[TEST] filling in help form office-phone item")
    help_name = driver.find_element_by_xpath(helpOfficePhoneXPath)
    help_name.send_keys(helpFormItems["officePhone"])
    time.sleep(1.0)

    logger.info("[TEST] filling in help form mobile-phone item")
    help_name = driver.find_element_by_xpath(helpMobilePhoneXPath)
    help_name.send_keys(helpFormItems["mobilePhone"])
    time.sleep(1.0)

    logger.info("[TEST] finding in help form subject item")
    help_name = driver.find_element_by_xpath(helpSubjectXPath)
    help_name_tag = help_name.tag_name
    logger.info(f"[TEST] help form subject tag is ${help_name_tag}")
    time.sleep(1.0)

    logger.info("[TEST] filling in help form message item")
    help_name = driver.find_element_by_xpath(helpMessageXPath)
    help_name.send_keys(helpFormItems["message"])
    time.sleep(1.0)

    logger.info("[TEST] clicking the help form submit button")
    help_send_button = driver.find_element_by_xpath(helpSendButtonXPath)
    help_send_button.click()

    time.sleep(timeout_sec)
    return driver


def run_test(timeout_sec):
    """
    This runs the test.

    """

    driver = None
    exit_code = 0

    try:

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-extensions")

        driver = webdriver.Chrome(options=options)

        # get to the landing page
        driver.get(landingPageUrl)

        #
        # login
        #
        logger.info("[RUNNER] doing login")
        login_to_reactbank(driver, timeout_sec)
        logger.info("[RUNNER] login done")

        #
        # other tests go here
        #

        # balance check
        logger.info("[RUNNER] doing balance check")
        find_balance_on_userpage(driver, timeout_sec)
        logger.info("[RUNNER] balance check done")

        # help form fill-in
        logger.info("[RUNNER] doing help form")
        fill_out_help_form(driver, timeout_sec)
        logger.info("[RUNNER] help form done")

        #
        # logout
        #
        logger.info("[RUNNER] doing logout")
        logout_from_reactbank(driver, timeout_sec)
        logger.info("[RUNNER] logout done")

    except Exception:

        logger.exception("Ran into exception when running test.")
        exit_code = 1

    finally:

        if driver is not None:

            logger.info("[RUNNER] waiting to close the window")
            time.sleep(2.5)
            driver.close()
            logger.info("[RUNNER] window close done, waiting for driver quit")
            driver.quit()
            logger.info("[RUNNER] driver quit done")

    logger.info(f"[RUNNER] test run complete. exit code: {exit_code}")
    sys.exit(exit_code)


if __name__ == "__main__":
    run_test(2.0)
