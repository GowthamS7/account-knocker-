from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time

class AccountChecker:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def check_pinterest_account(self, email, result_file):
        url = 'https://in.pinterest.com/'

        try:
            self.driver.get(url)
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="mweb-unauth-container"]/div/div/div[1]/div/div[2]/div[2]/button/div/div'))
            )
            login_button.click()

            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'email'))
            )

            email_input.send_keys(email)
            email_input.send_keys(Keys.RETURN)

            time.sleep(2)

            error_message = None
            try:
                error_message = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="email-error"]/div/div/div[2]'))
                )
            except:
                pass

            if error_message:
                result_file.write(f"{email} is not founded in Pinterest.\n")

        except Exception as e:
            print(f"EXCEPTION: {str(e)}")
            result_file.write(f"{email} encountered an error.\n")

    def check_spotify_account(self, email, result_file):
        url = 'https://www.spotify.com/in-en/signup'

        try:
            self.driver.get(url)

            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
            )

            email_input.send_keys(email)
            email_input.submit()

            try:
                error_message = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@class="Wrapper-sc-62m9tu-0 POdTa encore-warning-set AlreadyInUseBanner__StyledBanner-sc-1j4rkgm-0 jMBpIH"]'))
                )
                result_file.write(f"{email} is linked to Spotify.\n")

            except TimeoutException:
                next_button = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="submit"]'))
                )
                next_button.click()

        except Exception as e:
            print(f"EXCEPTION: {str(e)}")
            result_file.write(f"{email} encountered an error.\n")

    def check_quora_account(self, email, result_file):
        url = 'https://www.quora.com/'

        try:
            self.driver.get(url)

            email_input = self.driver.find_element(By.ID, 'email')
            email_input.send_keys(email)
            email_input.send_keys(Keys.RETURN)

            time.sleep(2)

            html_content = self.driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')

            error_message_div = soup.find('div', {'class': 'qu-color--red_error'})
            if error_message_div:
                result_file.write(f"{email} is not founded in Quora.\n")

        except Exception as e:
            print(f"EXCEPTION: {str(e)}")
            result_file.write(f"{email} encountered an error.\n")

    def close_driver(self):
        self.driver.quit()

if __name__ == "__main__":
    # Specify the emails directly in the code
    email_list = ["your email address"]

    # Create an instance of AccountChecker
    account_checker = AccountChecker()

    try:
        # Write results to output.txt
        with open('output.txt', 'w') as output_file:
            # Check accounts for each email
            for email in email_list:
                print(f"\nChecking email: {email}")
                account_checker.check_quora_account(email, output_file)
                account_checker.check_pinterest_account(email, output_file)
                account_checker.check_spotify_account(email, output_file)

    finally:
        # Close the driver when done
        account_checker.close_driver()
