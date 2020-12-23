"""
This is the Java Salesforce test implemented in Python.
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

sfLoginUrl = "https://login.salesforce.com/"
homePgurl = "https://testgold-dev-ed.lightning.force.com/lightning/page/home"
contactPgLayOutViewurl = "https://testgold-dev-ed.lightning.force.com/lightning/setup/ObjectManager/Contact/PageLayouts/view"
contPgRecentlyViewedurl = "https://testgold-dev-ed.lightning.force.com/lightning/o/Contact/list?filterName=Recent"
userNmTxtBx = "//input[@class='input r4 wide mb16 mt8 username']"
passwdTxtBx = "//input[@class='input r4 wide mb16 mt8 password']"

Userid = "dharam@testgold.dev"
Password = "admin123"

loginBtn = "//input[@class='button r4 wide primary']"
contactsButPath = "//span[.='Contacts']"
newContacttitle1 = "Recently Viewed | Contacts | Salesforce"
newContacttitle2 = "New Contact | Salesforce"
newBtnPath = "//a/div[@title='New']"
phonePath = "//div[@class='test-id__record-layout-container riseTransitionEnabled']/div/div[1]/div/div/div[1]/div[2]/div/div/div/input"
mobilePath = "//div[@class='test-id__record-layout-container riseTransitionEnabled']/div/div[1]/div/div/div[2]/div[2]/div/div/div/input"
salutePath = "(//fieldset)[1]/div/div[1]/div"  # //div[@class='test-id__section slds-section  slds-is-open full forcePageBlockSection forcePageBlockSectionEdit'][1]/div/div/div[2]/div[1]/div/div/fieldset/div/div[1]/div"
doctorTitle = "//li[@role='presentation']/a[ @title='Dr.']"
firstName = "//div[@class='test-id__section slds-section  slds-is-open full forcePageBlockSection forcePageBlockSectionEdit'][1]/div/div/div[2]/div[1]/div/div/fieldset/div/div[2]/input"
lastName = "//div[@class='test-id__section slds-section  slds-is-open full forcePageBlockSection forcePageBlockSectionEdit'][1]/div/div/div[2]/div[1]/div/div/fieldset/div/div[3]/input"
account_name = "//input[@class=' default input uiInput uiInputTextForAutocomplete uiInput--default uiInput--input uiInput uiAutocomplete uiInput--default uiInput--lookup']"
title_path = "//div[@class='test-id__section slds-section  slds-is-open full forcePageBlockSection forcePageBlockSectionEdit'][1]/div/div/div[4]/div[1]/div/div/div/input"
email_path = "//div[@class='test-id__section slds-section  slds-is-open full forcePageBlockSection forcePageBlockSectionEdit'][1]/div/div/div[3]/div[2]/div/div/div/input"
home_phone_path = "//div[@class='test-id__section slds-section  slds-is-open full forcePageBlockSection forcePageBlockSectionEdit'][1]/div/div/div[4]/div[2]/div/div/div/input"
dep_path = "//div[@class='test-id__section slds-section  slds-is-open full forcePageBlockSection forcePageBlockSectionEdit'][1]/div/div/div[5]/div[1]/div/div/div/input"
Assistant = "//div[@class='test-id__section slds-section  slds-is-open full forcePageBlockSection forcePageBlockSectionEdit'][1]/div/div/div[6]/div[2]/div/div/div/input"
dtPicker = "//a[@class='datePicker-openIcon display']"
descriptionPath = "//div[@class='test-id__section slds-section  slds-is-open full forcePageBlockSection forcePageBlockSectionEdit'][1]/div/div/div[5]/div[2]/div/div/div/textarea"
dtPickerPickList = "//select[@class='slds-select picklist__label']"
dtPickerYearPath = "//select[@class='slds-select picklist__label']/option[63]"
dayPickerPath = "//span[@class='slds-day weekday DESKTOP uiDayInMonthCell--default' or @class='slds-day weekend DESKTOP uiDayInMonthCell--default' and contains(text(),18)]"


###################
## test function ##
###################

def login_to_salesforce(driver, timeout_sec):
    """This logs into the Salesforce website and returns the driver in the new
    state.
    """

    time.sleep(timeout_sec)
    logger.info("[TEST] Navigate to Contact page and login when prompted..")

    driver.get(contPgRecentlyViewedurl)
    time.sleep(2.0)
    #curr_url = driver.current_url

    # click on the login button
    logger.info("[TEST] log into demodev")
    usr_name_txt = driver.find_element_by_xpath(userNmTxtBx)
    if usr_name_txt.is_enabled():
        logger.info("[TEST] UserName Txt enabled")
        usr_name_txt.send_keys(Userid)
    else:
        assert (usr_name_txt.is_enabled())

    passwd_txt = driver.find_element_by_xpath(passwdTxtBx)
    if passwd_txt.is_enabled():
        logger.info("[TEST] password Txt enabled")
        passwd_txt.send_keys(Password)
    else:
        assert (passwd_txt.is_enabled())

    submit_btn = driver.find_element_by_xpath(loginBtn)
    if submit_btn.is_enabled():
        logger.info("[TEST] submit button enabled.. submitting")
        submit_btn.click()
    else:
        assert (submit_btn.is_enabled())

    time.sleep(2.0)
    driver.get(contPgRecentlyViewedurl)
    time.sleep(2.0)
    curr_url = driver.current_url
    logger.info(curr_url)
    assert (curr_url == contPgRecentlyViewedurl)
    logger.info("[TEST] We Successfully landed in the Contact list recent page : " + curr_url)
    logger.info("[TEST] Clicking new to create new contact")

    new_btn = driver.find_element_by_xpath(newBtnPath)

    if new_btn.is_enabled():
        logger.info("[TEST]  contact button enabled.. clicking")
        new_btn.click()
    else:
        assert (new_btn.is_enabled())
    time.sleep(2.0)

    new_contact_title = driver.title
    is_pass = False
    if new_contact_title.lower() == newContacttitle1.lower() or new_contact_title.lower() == newContacttitle2.lower():
        is_pass = True
    assert is_pass
    logger.info("[TEST] We are ready to fill new contact info.. verified page title to be : " + new_contact_title)
    time.sleep(2.0)

    ########## NEW CONTACT ##########

    salute = driver.find_element_by_xpath(salutePath)

    if salute.is_displayed():
        logger.info("[TEST] salute Displayed")
        if salute.is_enabled():
            logger.info("[TEST] salute Enabled")
            salute.click()
            logger.info("[TEST] salute clicked")
            dr_title = driver.find_element_by_xpath(doctorTitle)
            if dr_title.is_displayed():
                logger.info("[TEST] Doctor Displayed")
                if dr_title.is_enabled():
                    logger.info("[TEST] Doctor Enabled")
                    dr_title.click()
                    time.sleep(1.0)
                    logger.info("[TEST] Doctor selected")

    logger.info("[TEST] Inputting first name")
    f_name = driver.find_element_by_xpath(firstName)
    if f_name.is_enabled():
        f_name.send_keys("James")
    time.sleep(1.0)

    logger.info("[TEST] Inputting required last name")
    l_name = driver.find_element_by_xpath(lastName)
    if l_name.is_enabled():
        l_name.send_keys("Wilson")
    time.sleep(1.0)

    # logger.info("[TEST] Inputting account name")
    # a_name = driver.find_element_by_xpath(account_name)
    # if a_name.is_enabled():
    #     a_name.send_keys("first_account")
    # time.sleep(1.0)

    logger.info("[TEST] Inputting title")
    title = driver.find_element_by_xpath(title_path)
    if title.is_enabled():
        title.send_keys("salesperson")
    time.sleep(1.0)

    logger.info("[TEST] Inputting department")
    dep = driver.find_element_by_xpath(dep_path)
    if dep.is_enabled():
        dep.send_keys("Sales")
    time.sleep(1.0)

    logger.info("[TEST] filling dates from date_picker")
    date_picker = driver.find_element_by_xpath(dtPicker)
    if date_picker.is_enabled():
        date_picker.click()

    time.sleep(1.0)
    dt_pick_list = driver.find_element_by_xpath(dtPickerPickList)
    if dt_pick_list.is_enabled():
        dt_pick_list.click()

    time.sleep(1.0)
    logger.info("[TEST] picking year")
    year = driver.find_element_by_xpath(dtPickerYearPath)
    if year.is_enabled():
        year.click()

    time.sleep(1.0)
    logger.info("[TEST] picking day")
    day = driver.find_element_by_xpath(dayPickerPath)
    if day.is_enabled():
        day.click()

    logger.info("[TEST] Inputting phone number")
    phone = driver.find_element_by_xpath(phonePath)
    if phone.is_enabled():
        phone.send_keys("4089999999")

    logger.info("[TEST] Inputting mobile")
    mobile = driver.find_element_by_xpath(mobilePath)
    if mobile.is_enabled():
        mobile.send_keys("4089999999")
    time.sleep(1.0)

    logger.info(
        "[TEST] inputting email")
    email = driver.find_element_by_xpath(email_path)
    if email.is_enabled():
        email.send_keys("jwilson@gmail.com")

    logger.info(
        "[TEST] inputting home phone")
    home_phone = driver.find_element_by_xpath(home_phone_path)
    if home_phone.is_enabled():
        home_phone.send_keys("4089999999")

    logger.info(
        "[TEST] inputting description")
    desc = driver.find_element_by_xpath(descriptionPath)
    if desc.is_enabled():
        desc.send_keys("new contact")

    time.sleep(1.0)
    logger.info("[TEST] inputting assistance's name")
    assist = driver.find_element_by_xpath(Assistant)
    if assist.is_enabled():
        assist.send_keys("Alice")



    time.sleep(timeout_sec * 2)

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
        login_to_salesforce(driver, timeout_sec)

    except Exception:

        logger.exception("Ran into exception when running test.")
        driver.success = False
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

