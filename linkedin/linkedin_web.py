from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import setup_logger
import time

logger = setup_logger()

class LinkedInWebAutomation:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.setup_driver()
        self.login()

    def setup_driver(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless=new')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument('--remote-debugging-port=9222')
            chrome_options.add_argument('--disable-features=VizDisplayCompositor')
            chrome_options.add_argument('--disable-software-rasterizer')
            chrome_options.add_argument('--disable-dev-tools')
            
            chrome_prefs = {
                'profile.default_content_setting_values.notifications': 2,
                'profile.default_content_settings.popups': 0,
                'download.prompt_for_download': False,
                'download.directory_upgrade': True,
                'safebrowsing.enabled': True
            }
            chrome_options.add_experimental_option('prefs', chrome_prefs)
            
            logger.info("Setting up Chrome driver with options...")
            service = Service('/usr/bin/chromedriver')
            
            self.driver = webdriver.Chrome(
                service=service,
                options=chrome_options
            )
            
            # Set timeouts
            self.driver.set_page_load_timeout(60)
            self.driver.implicitly_wait(30)
            
            # Test the driver
            logger.info("Testing Chrome driver...")
            self.driver.get('https://www.google.com')
            logger.info("Chrome driver test successful")
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to setup driver: {str(e)}")
            raise

    def login(self):
        max_retries = 3
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                logger.info(f"Login attempt {retry_count + 1}")
                self.driver.delete_all_cookies()
                
                # Navigate to login page
                logger.info("Navigating to LinkedIn login page...")
                self.driver.get('https://www.linkedin.com/login')
                
                # Print page source for debugging
                logger.info(f"Page title: {self.driver.title}")
                logger.info("Page source length: " + str(len(self.driver.page_source)))
                
                # Wait for email field
                logger.info("Waiting for email field...")
                email_field = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.ID, "username"))
                )
                email_field.clear()
                time.sleep(1)
                email_field.send_keys(self.email)
                logger.info("Email entered")
                
                time.sleep(2)  # Small delay between fields
                
                # Enter password
                logger.info("Entering password...")
                password_field = self.driver.find_element(By.ID, "password")
                password_field.clear()
                time.sleep(1)
                password_field.send_keys(self.password)
                logger.info("Password entered")
                
                time.sleep(2)  # Small delay before clicking
                
                # Click login
                logger.info("Clicking login button...")
                login_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
                )
                login_button.click()
                
                # Wait for successful login
                logger.info("Waiting for successful login...")
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".feed-shared-update-v2, .share-box-feed-entry__trigger"))
                )
                logger.info("Successfully logged in to LinkedIn")
                return True
                
            except Exception as e:
                retry_count += 1
                logger.error(f"Login attempt {retry_count} failed: {str(e)}")
                
                try:
                    screenshot_path = f"logs/login_error_{int(time.time())}.png"
                    self.driver.save_screenshot(screenshot_path)
                    logger.error(f"Login error screenshot saved to {screenshot_path}")
                    
                    # Save page source
                    with open(f"logs/page_source_{int(time.time())}.html", 'w') as f:
                        f.write(self.driver.page_source)
                    
                except Exception as screenshot_error:
                    logger.error(f"Failed to save debug info: {str(screenshot_error)}")
                
                if retry_count == max_retries:
                    raise
                
                time.sleep(10)
                self.setup_driver()

    def create_post(self, content):
        try:
            # Go to LinkedIn feed
            self.driver.get('https://www.linkedin.com/feed/')
            logger.info("Navigated to LinkedIn feed")
            
            # Click "Start a post" button - updated selector
            start_post_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.share-box-feed-entry__trigger"))
            )
            start_post_button.click()
            logger.info("Clicked start post button")
            
            # Wait for post modal and enter content - updated selector
            post_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox']"))
            )
            post_field.send_keys(content)
            logger.info("Entered post content")
            
            # Click Post button - updated selector
            post_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.share-actions__primary-action"))
            )
            post_button.click()
            logger.info("Clicked post button")
            
            # Wait for success notification
            success_notification = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".artdeco-toast-item--type-success"))
            )
            logger.info("Successfully created post")
            
        except Exception as e:
            logger.error(f"Failed to create post: {str(e)}")
            # Take screenshot for debugging
            try:
                screenshot_path = f"logs/error_screenshot_{int(time.time())}.png"
                self.driver.save_screenshot(screenshot_path)
                logger.error(f"Screenshot saved to {screenshot_path}")
            except:
                pass
            raise

    def __del__(self):
        try:
            if hasattr(self, 'driver'):
                self.driver.quit()
        except:
            pass 