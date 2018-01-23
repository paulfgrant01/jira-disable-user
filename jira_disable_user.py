""" Disable JIRA User via selenium and chrome headless browser """

from os import environ
from time import time
import argparse
from selenium_client import Selenium

JIRA_SERVER = environ['JIRA_SERVER']


def main():
    """ Main """
    args = parse_args()
    selenium = Selenium()
    set_jira_user_inactive(selenium.driver, selenium, args.user)


def parse_args():
    """ Parse command line args """
    parser = argparse.ArgumentParser(description='Disable user in JIRA')
    parser.add_argument('--user', required=True, help='User to disable')
    return parser.parse_args()


def set_jira_user_inactive(driver, selenium, user):
    """ Set jira user inactive"""
    try:
        selenium.get_page(JIRA_SERVER)
        selenium.wait_for_element_to_click('login')
        driver.find_element_by_id('login-form-username').send_keys(selenium.user)
        driver.find_element_by_id("login-form-password").send_keys(selenium.password)
        driver.find_element_by_id("login").click()
        selenium.wait_for_element_to_click('admin_menu')
        driver.find_element_by_id('admin_menu').click()
        selenium.wait_for_element_to_click('admin_users_menu')
        driver.find_element_by_id('admin_users_menu').click()
        selenium.wait_for_element_to_click('login-form-authenticatePassword')
        driver.find_element_by_id('login-form-authenticatePassword').send_keys(selenium.password)
        driver.find_element_by_id('login-form-submit').click()
        selenium.wait_for_element_to_click('user-filter-userSearchFilter')
        driver.find_element_by_id('user-filter-userSearchFilter').send_keys(user)
        driver.find_element_by_id('user-filter-submit').click()
        selenium.wait_for_element_to_click('edituser_link_{}'.format(user))
        driver.find_element_by_class_name('edit-profile-link').click()
        selenium.wait_for_element_to_click('user-edit-active')

        # Find out if user is active or not
        user_active = driver.find_element_by_id('user-edit-active').get_attribute('checked')
        if user_active:
            print('User {} is active in JIRA, setting inactive'.format(user))
            driver.find_element_by_id('user-edit-active').click()
            driver.find_element_by_id('user-edit-submit').click()
        else:
            print('User {} is already inactive in JIRA'.format(user))

    except Exception as error: # pylint: disable=broad-except
        print(error)
        selenium.save_screenshot('{}-{}'.format(user, int(time())))
    finally:
        # quit the driver
        driver.quit()
        print('quitting')


main()
