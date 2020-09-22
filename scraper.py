from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import values
from constants import DEADLINE, ADMISSION, COST, BIGFUTURE_DOMAIN, BIGFUTURE_ERROR


def generate_URL(school_name):
    school_url_path = school_name.replace(" ", "-").lower()
    return BIGFUTURE_DOMAIN + school_url_path

def construct_school_dict(school_name):
    """
    A dictionary template to generate a dictionary
    to store scraped information about each school
    """
    school = dict()
    school["Name"] = school_name
    for field in values.FIELD_NAMES:
        school[field] = ""
    return school

def check_school_existed(school_name, database):
    """
    Check from the mongoDB to see if school has already been scraped
    """
    find_result = database.find_by_criterion("Name", school_name)
    return (len(find_result) > 0)

class CollegeBoardScaper:
    """
    Initiating a scraper session
    """
    def __init__(self, web_driver, school_name):
        self.driver = web_driver
        self.school_info = construct_school_dict(school_name)
    
    def click(self, element_to_click):
        """
        Special click using Javascript because normal Selenium click does not work
        """
        self.driver.execute_script("arguments[0].click();", element_to_click)

    def check_valid_page(self):
        if (self.driver.current_url == BIGFUTURE_ERROR):
            raise NotFoundError()

    def find_and_set_content(self, info_element):
        content = self.driver.find_element_by_xpath(info_element.xpath).text
        self.school_info[info_element.desp] = content
    #     # print(f"{info_element.desp}: {info_element.content}")

    def scrape_deadlines(self):
        deadlines_tab = self.driver.find_element_by_link_text(DEADLINE)
        self.click(deadlines_tab)
        # For loops to scrape all elements at once
        for (date_element, month_element) in values.DEADLINE_TUPLE_ELEMENTS:
            self.find_and_set_content(date_element)
            self.find_and_set_content(month_element)
    
    def scrape_admission(self):
        # First click on admission tab for website to dynamically generate admission data
        admission_tab = self.driver.find_element_by_link_text(ADMISSION)
        self.click(admission_tab)
        # Get addmission rate
        self.find_and_set_content(values.ADMIT_RATE)
        # Additional click to open "SAT and ACT" tab
        sat_act_tab = self.driver.find_element_by_link_text("SAT & ACT Scores")
        self.click(sat_act_tab)
        # Additional clicks to access specific "SAT" or "ACT" tab
        sat_inner_tab = self.driver.find_element_by_xpath('/html/body/div[9]/div/div/div[3]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div/div[1]/button')
        self.click(sat_inner_tab)
        self.find_and_set_content(values.SAT_RANGE)

        act_inner_tab = self.driver.find_element_by_xpath('/html/body/div[9]/div/div/div[3]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div/div[2]/button')
        self.click(act_inner_tab)
        self.find_and_set_content(values.ACT_RANGE)

    def scrape_cost(self):
        cost_tab = self.driver.find_element_by_link_text(COST)
        self.click(cost_tab)
        # Wait for the Cost page to load fully; it loads quite slowly
        out_of_state_xpath = '//*[@id="cpProfile_tabs_paying_outstatecosts_anchor"]/a'
        out_of_state_tab = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, out_of_state_xpath))
        )
        
        self.click(out_of_state_tab)

        for element in values.COST_ELEMENTS:
            self.find_and_set_content(element)

    def scrape_all(self):
        self.scrape_admission()
        self.scrape_deadlines()
        self.scrape_cost()
 
class NotFoundError(Exception):
    """Exception raised for school names that cannot be found on CollegeBoard"""
    def __init__(self, message="Cannot find school"):
        self.message = message
        super().__init__(self.message)


def run_from_command_line():
    school = input("Enter school name to search: ")
    URL = generate_URL(school)
    driver = webdriver.Safari()
    driver.implicitly_wait(15)
    scraper_session = CollegeBoardScaper(driver, school)
    try:
        driver.get(URL)
        scraper_session.check_valid_page()
        scraper_session.scrape_all()
    except NotFoundError:
        print(f"'{school}' cannot be found. Make sure to type in the school's full name correctly")
    except TimeoutException:
        print("Timeout. Check network connection")
    finally:
        driver.quit()


def run_from_file(input_file, existed_school_list) -> dict:
    all_results = [] # List of dictionaries to store all results
    driver = webdriver.Safari()
    driver.implicitly_wait(10)
    with open(input_file) as school_list:
        for school_name in school_list:
            school_name = school_name.rstrip()
            print(school_name)
            if school_name in existed_school_list:
                print(f"{school_name} already in database")
                continue
            URL = generate_URL(school_name)
            scraper_session = CollegeBoardScaper(driver, school_name)
            try:
                driver.get(URL)
                scraper_session.check_valid_page()
                scraper_session.scrape_all()
                all_results.append(scraper_session.school_info)
            except NotFoundError:
                print(f"'{school_name}' cannot be found. Make sure to type in the school's full name correctly")
            except TimeoutException:
                print(f"Timeout for {school_name}. Check network connection")
            finally:
                print("Done")
    driver.quit()
    return all_results
