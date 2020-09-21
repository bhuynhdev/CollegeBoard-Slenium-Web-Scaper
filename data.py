# File to store information data and xpath datas
# After scraping successfully, the scraped data goes back into the ALL_ELEMENTS list
# in this file

from constants import DEADLINE, COST, ADMISSION

class InfoElement:
    """
    A helper class to store and organize information
    """
    def __init__(self, category, description):
        self.category = category
        self.xpath = ""
        self.content = ""
        self.desp = description

# Deadlines info
class Deadline:
    """
    Helper class to store deadline information better
    """
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

deadline_object_list = [rd, ea, ed1, ed2]
DEADLINE_TUPLE_ELEMENTS = [(x.date, x.month) for x in deadline_object_list]
DEADLINE_ELEMENTS = [x for date_month_tuple in DEADLINE_TUPLE_ELEMENTS for x in date_month_tuple ]


# Admission info: admission rate, SAT, etc.
admit_rate = InfoElement(ADMISSION, "Admission rate")
admit_rate.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[1]/div[1]/div[3]/p/div[3]'

# Must click additionally on the "SAT & ACT Scores" tab first (after clicking the "Applying" tab)
# to access SAT/ACT info
sat_range = InfoElement(ADMISSION, "SAT range")
sat_range.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[1]/table/tbody/tr/td[2]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div'

act_range = InfoElement(ADMISSION, "ACT range")
act_range.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[3]/div/div/div[3]/div[2]/div/div/div[1]/table/tbody/tr/td[2]/div/div[1]/div[2]/div[2]/div[1]/div'

ADMISSION_ELEMENTS = [admit_rate, sat_range, act_range]
# Cost info
# Must click on "Out-Of-State Costs" tab first
out_tuition = InfoElement(COST, "Out-of-state tuition")
out_tuition.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[3]/div/div/div[4]/div[1]/div/div/div/table/tbody/tr[1]/td[1]/span'

room = InfoElement(COST, "Room and board")
room.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[3]/div/div/div[4]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/span'

out_total = InfoElement(COST, "Out-of-state total cost")
out_total.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[3]/div/div/div[4]/div[1]/div/div/div/table/tbody/tr[7]/td[1]/span'


COST_ELEMENTS = [out_tuition, room, out_total]

ALL_ELEMENTS = ADMISSION_ELEMENTS + DEADLINE_ELEMENTS + COST_ELEMENTS

def generate_dict(school_name, all_elements=ALL_ELEMENTS):
    result = dict()
    result["School"] = school_name
    for element in all_elements:
        result[element.desp] = element.content
    return result