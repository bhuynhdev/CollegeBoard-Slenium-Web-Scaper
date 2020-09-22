"""
File to store information and xpath data
"""

from constants import DEADLINE, COST, ADMISSION


class InfoElement:
    """
    A helper class to store and organize information
    """
    def __init__(self, category, description):
        self.category = category
        self.xpath = ""
        self.desp = description


RD_MONTH = InfoElement(DEADLINE, "RD Month")
RD_MONTH.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]'

RD_DATE = InfoElement(DEADLINE, "RD DATE")
RD_DATE.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]'

EA_MONTH = InfoElement(DEADLINE, "EA Month")
EA_MONTH.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]'

EA_DATE = InfoElement(DEADLINE, "EA Date")
EA_DATE.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]'

ED1_MONTH = InfoElement(DEADLINE, "ED1 Month")
ED1_MONTH.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[5]/div[1]'

ED1_DATE = InfoElement(DEADLINE, "ED1 Date")
ED1_DATE.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]'

ED2_MONTH = InfoElement(DEADLINE, "ED2 Month")
ED2_MONTH.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]'

ED2_DATE = InfoElement(DEADLINE, "ED2 Date")
ED2_DATE.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]'

DEADLINE_TUPLE_ELEMENTS = [(RD_DATE, RD_MONTH), (EA_DATE, EA_MONTH),
                           (ED1_DATE, ED1_MONTH), (ED2_DATE, ED2_MONTH)]
DEADLINE_ELEMENTS = [x for datemonth_tuple in DEADLINE_TUPLE_ELEMENTS for x in datemonth_tuple]


# Admission info: admission rate, SAT, etc.
ADMIT_RATE = InfoElement(ADMISSION, "Admission rate")
ADMIT_RATE.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[1]/div[1]/div[3]/p/div[3]'

# Must click additionally on the "SAT & ACT Scores" tab first (after clicking the "Applying" tab)
# to access SAT/ACT info
SAT_RANGE = InfoElement(ADMISSION, "SAT range")
SAT_RANGE.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[1]/table/tbody/tr/td[2]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div'

ACT_RANGE = InfoElement(ADMISSION, "ACT range")
ACT_RANGE.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[3]/div/div/div[3]/div[2]/div/div/div[1]/table/tbody/tr/td[2]/div/div[1]/div[2]/div[2]/div[1]/div'

ADMISSION_ELEMENTS = [ADMIT_RATE, SAT_RANGE, ACT_RANGE]


# Cost info
# Must click on "Out-Of-State Costs" tab first
OUT_TUITION = InfoElement(COST, "Out-of-state tuition")
OUT_TUITION.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[3]/div/div/div[4]/div[1]/div/div/div/table/tbody/tr[1]/td[1]/span'

ROOM = InfoElement(COST, "ROOM and boaRD")
ROOM.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[3]/div/div/div[4]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/span'

OUT_TOTAL = InfoElement(COST, "Out-of-state total cost")
OUT_TOTAL.xpath = '//*[@id="topFrame"]/div[2]/div[2]/div/div/div[3]/div/div/div[4]/div[1]/div/div/div/table/tbody/tr[7]/td[1]/span'


COST_ELEMENTS = [OUT_TUITION, ROOM, OUT_TOTAL]

ALL_ELEMENTS = ADMISSION_ELEMENTS + DEADLINE_ELEMENTS + COST_ELEMENTS

FIELD_NAMES = [x.desp for x in ALL_ELEMENTS]
