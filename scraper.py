from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

URL = "https://bigfuture.collegeboard.org/college-university-search/drexel-university"


# Category's link text for Selenium to find
DEADLINE = "Deadlines"
ADMISSION = "Applying"
MAJOR = "Majors & Learning Environment"
INTERNATIONAL = "International Students"
COST = "Paying"

class InfoElement:
    def __init__(self, category, description):
        self.category = category
        self.xpath = ""
        self.content = ""
        self.desp = description

    def find_and_set_content(self):
        global driver
        self.content = driver.find_element_by_xpath(self.xpath).text
        print(f"{self.desp}: {self.content}")

# Deadlines info
class Deadline:
    def __init__(self, description):    
        self.date = InfoElement(DEADLINE, description + " Date")
        self.month = InfoElement(DEADLINE, description + " Month")

rd = Deadline("Regular decision")
rd.month.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]'
rd.date.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]'


ea = Deadline("Early action")
ea.month.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]'
ea.date.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]'

ed1 = Deadline("Early decision 1")
ed1.month.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[5]/div[1]'
ed1.date.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]'

ed2 = Deadline("Early decision 2")
ed2.month.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]'
ed2.date.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]'

# Generating deadline elements list
deadline_object_list = [rd, ea, ed1, ed2]
DEADLINE_ELEMENTS = []
for deadline_object in deadline_object_list:
    DEADLINE_ELEMENTS.append(deadline_object.date)
    DEADLINE_ELEMENTS.append(deadline_object.month)

# Admission info: admission rate, SAT, etc.

admit_rate = InfoElement(ADMISSION, "Admission rate")
admit_rate.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[1]/div[1]/div[3]/p/div[3]'

# Must click additionally on the "SAT & ACT Scores" tab first (after clicking the "Applying" tab)
# to access SAT/ACT info
sat = InfoElement(ADMISSION, "SAT range")
sat.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[1]/table/tbody/tr/td[2]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div'

act = InfoElement(ADMISSION, "ACT range")
act.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[3]/div/div/div[3]/div[2]/div/div/div[1]/table/tbody/tr/td[2]/div/div[1]/div[2]/div[2]/div[1]/div'

ADMISSION_ELEMENTS = [sat, act, admit_rate]

# Cost info
# Must click on "Out-Of-State Costs" tab first
out_tuition = InfoElement(COST, "Out-of-state tuition")
out_tuition.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[3]/div/div/div[4]/div[1]/div/div/div/table/tbody/tr[1]/td[1]/span'

room = InfoElement(COST, "Room and board")
room.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[3]/div/div/div[4]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/span'

out_total = InfoElement(COST, "Out-of-state total cost")
out_total.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[3]/div/div/div[4]/div[1]/div/div/div/table/tbody/tr[7]/td[1]/span'

COST_ELEMENTS = [out_tuition, room, out_total]

def click(element_to_click):
    global driver
    driver.execute_script("arguments[0].click();", element_to_click)


# Test 1
driver = webdriver.Safari()
driver.get(URL)
driver.implicitly_wait(15)

# Getting deadlines info
deadlines_tab = driver.find_element_by_link_text(DEADLINE)
click(deadlines_tab)
for element in DEADLINE_ELEMENTS:
    element.find_and_set_content()

# Getting admission info
admission_tab = driver.find_element_by_link_text(ADMISSION)
click(admission_tab)
admit_rate.find_and_set_content()
# Additional click to open "SAT and ACT" tab
sat_act_tab = driver.find_element_by_link_text("SAT & ACT Scores")
click(sat_act_tab)

sat_inner_tab = driver.find_element_by_xpath('/html/body/div[9]/div/div/div[3]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div/div[1]/button')
click(sat_inner_tab)
sat.find_and_set_content()

act_inner_tab = driver.find_element_by_xpath('/html/body/div[9]/div/div/div[3]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div/div[2]/button')
click(act_inner_tab)
act.find_and_set_content()

# Getting cost info
cost_tab = driver.find_element_by_link_text(COST)
click(cost_tab)
click(driver.find_element_by_link_text("Out-Of-State Costs"))

for element in COST_ELEMENTS:
    element.find_and_set_content()

driver.quit()