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


LANDING_PAGE_URL = "https://www.facebook.com/"
LOGIN_EMAIL_XPATH = "//input[@id='email']"
LOGIN_PASSWORD_XPATH = "//input[@id='pass']"
LOGIN_SUBMIT_XPATH = "//button[@type='submit']"  #"//button[contains(text(),'Log In')]"

# GROUPS_XPATH="//body/div[@id='mount_0_0']/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[4]/span[1]/div[1]/a[1]"
# GROUPS_XPATH = "//span[contains(text(),'Groups')]"  # newer design "//div[contains(text(),'Groups')]" # older design

#HEADER_DROPDOWN_BUTTON = "//body/div[@id='mount_0_0']/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/span[1]/div[1]/div[1]"
HEADER_DROPDOWN_BUTTON = "//body/div[@id='mount_0_0']/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/span[1]" #"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/span[1]/div[1]/div[1]/img[1]" # newer design "//div[contains(text(),'Account Settings')]" # older design
# HEADER_DROPDOWN_BUTTON = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[5]/span[1]"

LOGOUT_BUTTON_XPATH = "//span[contains(text(),'Log Out')]"


def login(driver, timeout_sec):
    """This logs into the Facebook and returns the driver in the new
        state.
    """

    time.sleep(timeout_sec)

    logger.info("[TEST] finding the login email box and filling it in")
    email_box = driver.find_element_by_xpath(LOGIN_EMAIL_XPATH)
    email_box.send_keys(FB_EMAIL)

    logger.info("[TEST] finding the login pass box and filling it in")
    pass_box = driver.find_element_by_xpath(LOGIN_PASSWORD_XPATH)
    pass_box.send_keys(FB_PASS)

    # click on the submit button
    logger.info("[TEST] finding the login submit button")
    login_submit = driver.find_element_by_xpath(LOGIN_SUBMIT_XPATH)
    login_submit.click()
    time.sleep(timeout_sec)
    return driver

def view_profile(driver, timeout_sec):
    """This shows profile page info"""

    time.sleep(timeout_sec * 1.5)
    logger.info("[TEST] finding profile button")
    profile_btn = driver.find_element_by_xpath("//*[@id='mount_0_0']//div[@class='buofh1pr']/ul/li/div/a")
    #"//*[@id='mount_0_0']/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[4]/a")  # "//*[@id='mount_0_0']/div/div[1]/div[1]/div[2]//a[starts-with(@href, '/profile')]")
    logger.info("[TEST] clicking profile_btn button")
    profile_btn.click()
    time.sleep(timeout_sec * 1.5)

    logger.info("[TEST] finding 'about' button")
    about_btn = driver.find_element_by_xpath("//a/div/span[contains(text(),'About')]")   #"//span[contains(text(),'About')]")  #
    logger.info("[TEST] clicking about_btn button")
    about_btn.click()
    time.sleep(timeout_sec * 1.5)

    logger.info("[TEST] finding work_btn button")
    work_btn = driver.find_element_by_xpath("//a/span[contains(text(),'Work and Education')]")
    logger.info("[TEST] clicking work_btn button")
    work_btn.click()
    time.sleep(timeout_sec * 1.5)

    logger.info("[TEST] finding places_btn button")
    places_btn = driver.find_element_by_xpath("//a/span[contains(text(),'Places Lived')]")
    logger.info("[TEST] clicking places_btn button")
    places_btn.click()
    time.sleep(timeout_sec*1.5)

    logger.info("[TEST] finding contact_btn button")
    contact_btn = driver.find_element_by_xpath("//a/span[contains(text(),'Contact and Basic Info')]")
    logger.info("[TEST] clicking contact_btn button")
    contact_btn.click()
    time.sleep(timeout_sec*1.5)

    logger.info("[TEST] finding family_btn button")
    family_btn = driver.find_element_by_xpath("//a/span[contains(text(),'Family and Relationships')]")
    logger.info("[TEST] clicking family_btn button")
    family_btn.click()
    time.sleep(timeout_sec*1.5)

    logger.info("[TEST] finding datails_btn button")
    datails_btn = driver.find_element_by_xpath("//a/span[contains(text(),'Details About You')]")
    logger.info("[TEST] clicking family_btn button")
    datails_btn.click()
    time.sleep(timeout_sec*1.5)

    logger.info("[TEST] finding life_btn button")
    life_btn = driver.find_element_by_xpath("//a/span[contains(text(),'Life Events')]")
    logger.info("[TEST] clicking life_btn button")
    life_btn.click()
    time.sleep(timeout_sec*2)


    logger.info("[TEST] finding friends_btn button")
    friends_btn = driver.find_element_by_xpath("//h2/span/a[contains(text(), 'Friends')]")
    logger.info("[TEST] clicking friends_btn button")
    friends_btn.click()
    time.sleep(timeout_sec*1.5)

    logger.info("[TEST] finding sports_btn button")
    sports_btn = driver.find_element_by_xpath("//a[contains(text(), 'Sports')]")
    logger.info("[TEST] clicking sports_btn button")
    sports_btn.click()
    time.sleep(timeout_sec*1.5)

    logger.info("[TEST] finding music_btn button")
    music_btn = driver.find_element_by_xpath("//a[contains(text(), 'Music')]")
    logger.info("[TEST] clicking music_btn button")
    music_btn.click()
    time.sleep(timeout_sec*1.5)

    logger.info("[TEST] finding movies_btn button")
    movies_btn = driver.find_element_by_xpath("//a[contains(text(), 'Movies')]")
    logger.info("[TEST] clicking movies_btn button")
    movies_btn.click()
    time.sleep(timeout_sec*1.5)

    logger.info("[TEST] finding tv_shows_btn button")
    tv_shows_btn = driver.find_element_by_xpath("//a[contains(text(), 'TV Shows')]")
    logger.info("[TEST] clicking tv_shows_btn button")
    tv_shows_btn.click()
    time.sleep(timeout_sec*1.5)

    logger.info("[TEST] finding books_btn button")
    books_btn = driver.find_element_by_xpath("//a[contains(text(), 'Books')]")
    logger.info("[TEST] clicking books_btn button")
    books_btn.click()
    time.sleep(timeout_sec*1.5)

    logger.info("[TEST] finding likes_btn button")
    likes_btn = driver.find_element_by_xpath("//a[contains(text(), 'Likes')]")
    logger.info("[TEST] clicking likes_btn button")
    likes_btn.click()
    time.sleep(timeout_sec*1.5)

    logger.info("[TEST] finding questions_btn button")
    questions_btn = driver.find_element_by_xpath("//a[contains(text(), 'Questions')]")
    logger.info("[TEST] clicking questions_btn button")
    questions_btn.click()
    time.sleep(timeout_sec*1.5)

    logger.info("[TEST] finding groups_btn button")
    groups_btn = driver.find_element_by_xpath("//a[contains(text(), 'Groups')]")
    logger.info("[TEST] clicking groups_btn button")
    groups_btn.click()
    time.sleep(timeout_sec*1.5)

    return driver


# def view_groups(driver, timeout_sec):
#     """This shows  groups page info"""
#
#     time.sleep(timeout_sec)
#     logger.info("[TEST] finding groups button")
#
#     groups_button = driver.find_element_by_xpath(GROUPS_XPATH)
#     logger.info("[TEST] clicking groups button")
#     groups_button.click()
#
#     time.sleep(timeout_sec)
#     return driver


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

        # profile info
        logger.info("[RUNNER] viewing profile info")
        view_profile(driver, timeout_sec)

        # groups info
        # logger.info("[RUNNER] viewing groups info")
        # view_groups(driver, timeout_sec)

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
