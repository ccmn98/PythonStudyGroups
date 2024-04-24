
# A script that scans an EAD3 XML file for a title element that has a string that contains date informtaion tha is not encoded in <date> or <unitdate> elements.
# The script than extracts this infomation and puts it in a <date> and <unitdate> elements. 
# The goal that I wanted to achieve was to output an XML file of the XML with these changes. 

from gettext import find
from bs4 import BeautifulSoup as bs, Tag
from lxml import etree
import re
content = []
#Read the xml file
with open(r'E:\GitHub\Python_practice_scripts\XML_Projects\ZBRIG_ms011108_1.xml', 'r', encoding="latin-1") as file:
    contents = file.read()
    soup = bs(contents, features="xml")
    
unittitle_tags = ['unittitle']

did_tags = ['did']

# This scans for date ranges within the unittitle and replaces date range text with a date element containing the attributes
def date_range():
    for tags in soup.find_all(unittitle_tags):
        kids = list(tags.children)
        date_array = re.findall(r'[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]', tags.text.strip())
        if not(tags.find('date')):
            # converts date list(array) into string
            date_string = ' '.join(date_array)
            element_as_string = str(date_array)
            date_range_test = bool(re.search(r'[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]', date_string))
            number_date_ranges = len(date_array)
            if date_range_test is True:
                if number_date_ranges == 1:
                    single_range_string = date_array[0]
                    date_soup = bs('<date></date>', features="xml")
                    date_range_tag = date_soup.date
                    date_range_tag['encodinganalog'] = '245$f'
                    date_range_tag['localtype'] = 'inclusive'
                    date_range_tag['normal'] = single_range_string.replace('-', '/')
                    date_range_tag.append(date_string)
                print(f"Original tag: {tags} \n Amended String: {date_range_tag} \n \n" )
                
                    # for dates in soup.find_all(string = re.compile(r'[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]')):
                        # dates.replace_with(date_range_tag)
                        # print(f"output of dates: {dates} \n")
                    # print(f"Tag: {tags} \n single date range test: {date_range_tag}\n \n")
                    # date_range_element_string = str(date_range_tag)
                if number_date_ranges == 2:
                    #encoding the first date range when a unittitle contains two date ranges in its string
                    first_date_range_string_0 = date_array[0]
                    date_2_1_soup = bs('<date></date>', features="xml")
                    date_2_range_tag_01 = date_2_1_soup.date
                    date_2_range_tag_01['encodinganalog'] = '245$f'
                    date_2_range_tag_01['localtype'] = 'inclusive'
                    date_2_range_tag_01['normal'] = first_date_range_string_0.replace('-', '/')
                    date_2_range_tag_01.append(first_date_range_string_0)
                    # print(date_range_tag)
                    date_range_element_string = str(date_range_tag)
                    
                    #encoding the second date range when a unittitle contains two date ranges in its string
                    second_date_range_string_1 = date_array[1]
                    date_2_2_soup = bs('<date></date>', features="xml")
                    date_2_range_tag_02 = date_2_2_soup.date
                    date_2_range_tag_02['encodinganalog'] = '245$f'
                    date_2_range_tag_02['localtype'] = 'inclusive'
                    date_2_range_tag_02['normal'] = second_date_range_string_1.replace('-', '/')
                    date_2_range_tag_02.append(second_date_range_string_1)
                if number_date_ranges == 3:
                    #encoding the first date range when a unittitle contains three date ranges in its string
                    first_date_range_string_00 = date_array[0]
                    date_3_1_soup = bs('<date></date>', features="xml")
                    date_3_range_tag_01 = date_3_1_soup.date
                    date_3_range_tag_01['encodinganalog'] = '245$f'
                    date_3_range_tag_01['localtype'] = 'inclusive'
                    date_3_range_tag_01['normal'] = first_date_range_string_00.replace('-', '/')
                    date_3_range_tag_01.append(first_date_range_string_00)
                    # print(date_range_tag)
                    date_range_element_string = str(date_range_tag)
                    
                    #encoding the second date range when a unittitle contains three date ranges in its string
                    second_date_range_string_01 = date_array[1]
                    date_3_2_soup = bs('<date></date>', features="xml")
                    date_3_range_tag_02 = date_3_2_soup.date
                    date_3_range_tag_02['encodinganalog'] = '245$f'
                    date_3_range_tag_02['localtype'] = 'inclusive'
                    date_3_range_tag_02['normal'] = second_date_range_string_01.replace('-', '/')
                    date_3_range_tag_02.append(second_date_range_string_01)
                    
                    #encoding the second date range when a unittitle contains three date ranges in its string
                    second_date_range_string_02 = date_array[2]
                    date_3_3_soup = bs('<date></date>', features="xml")
                    date_3_range_tag_03 = date_3_3_soup.date
                    date_3_range_tag_03['encodinganalog'] = '245$f'
                    date_3_range_tag_03['localtype'] = 'inclusive'
                    date_3_range_tag_03['normal'] = second_date_range_string_02.replace('-', '/')
                    date_3_range_tag_03.append(second_date_range_string_02)
                    
                if number_date_ranges == 4:
                    #encoding the first date range when a unittitle contains four date ranges in its string
                    first_date_range_string_000 = date_array[0]
                    date_4_1_soup = bs('<date></date>', features="xml")
                    date_4_range_tag_01 = date_4_1_soup.date
                    date_4_range_tag_01['encodinganalog'] = '245$f'
                    date_4_range_tag_01['localtype'] = 'inclusive'
                    date_4_range_tag_01['normal'] = first_date_range_string_000.replace('-', '/')
                    date_4_range_tag_01.append(first_date_range_string_00)
                    # print(date_range_tag)
                    date_range_element_string = str(date_range_tag)
                    
                    #encoding the second date range when a unittitle contains four date ranges in its string
                    second_date_range_string_001 = date_array[1]
                    date_4_2_soup = bs('<date></date>', features="xml")
                    date_4_range_tag_02 = date_4_2_soup.date
                    date_4_range_tag_02['encodinganalog'] = '245$f'
                    date_4_range_tag_02['localtype'] = 'inclusive'
                    date_4_range_tag_02['normal'] = second_date_range_string_001.replace('-', '/')
                    date_4_range_tag_02.append(second_date_range_string_001)
                    
                    #encoding the third date range when a unittitle contains four date ranges in its string
                    second_date_range_string_002 = date_array[2]
                    date_4_3_soup = bs('<date></date>', features="xml")
                    date_4_range_tag_03 = date_4_3_soup.date
                    date_4_range_tag_03['encodinganalog'] = '245$f'
                    date_4_range_tag_03['localtype'] = 'inclusive'
                    date_4_range_tag_03['normal'] = second_date_range_string_002.replace('-', '/')
                    date_4_range_tag_03.append(second_date_range_string_002)
                    
                    #encoding the third date range when a unittitle contains four date ranges in its string
                    second_date_range_string_003 = date_array[3]
                    date_4_3_soup = bs('<date></date>', features="xml")
                    date_4_range_tag_03 = date_4_3_soup.date
                    date_4_range_tag_03['encodinganalog'] = '245$f'
                    date_4_range_tag_03['localtype'] = 'inclusive'
                    date_4_range_tag_03['normal'] = second_date_range_string_003.replace('-', '/')
                    date_4_range_tag_03.append(second_date_range_string_003)
                    date_4_range_element_03_string = str(date_4_range_tag_03)
                    # print(f"reconfigered Element: {re.sub(r'[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]', unitdate_range_element_string, element_as_string)}\n\n")
    for tags in soup.find_all(did_tags):
        unitdate_array = re.findall(r'[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]', tags.text.strip()) 
        if not(tags.find('unitdate')):
            unitdate_string = ' '.join(unitdate_array)
            unitdate_range_test = bool(re.search(r'[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]', unitdate_string))
            number_unitdate_ranges = len(unitdate_array)
            if unitdate_range_test is True:
                if number_unitdate_ranges == 1:
                    single_unitdate_range_string = unitdate_array[0]
                    unitdate_soup = bs('<unitdate></unitdate>', features="xml")
                    unitdate_range_tag = unitdate_soup.unitdate
                    unitdate_range_tag['encodinganalog'] = '245$f'
                    unitdate_range_tag['unitdatetype'] = 'inclusive'
                    unitdate_range_tag['normal'] = single_unitdate_range_string.replace('-', '/')
                    unitdate_range_tag.append(unitdate_string)
                    # print(unitdate_range_tag)
                    unitdate_range_element_string = str(unitdate_range_tag)
            
                if number_unitdate_ranges == 2:
                    #encoding the first date range when a unittitle contains two date ranges in its string
                    first_unitdate_range_string_0 = unitdate_array[0]
                    unitdate_2_1_soup = bs('<unitdate></unitdate>', features="xml")
                    unitdate_2_range_tag_01 = unitdate_2_1_soup.unitdate
                    unitdate_2_range_tag_01['encodinganalog'] = '245$f'
                    unitdate_2_range_tag_01['unitdatetype'] = 'inclusive'
                    unitdate_2_range_tag_01['normal'] = first_unitdate_range_string_0.replace('-', '/')
                    unitdate_2_range_tag_01.append(first_unitdate_range_string_0)
                    # print(unitdate_2_range_tag_01)
                    date_range_element_string = str(unitdate_2_range_tag_01)
                    
                    #encoding the second date range when a unittitle contains two date ranges in its string
                    second_unitdate_range_string_1 = unitdate_array[1]
                    unitdate_2_2_soup = bs('<unitdate></unitdate>', features="xml")
                    unitdate_2_range_tag_02 = unitdate_2_2_soup.unitdate
                    unitdate_2_range_tag_02['encodinganalog'] = '245$f'
                    unitdate_2_range_tag_02['unitdatetype'] = 'inclusive'
                    unitdate_2_range_tag_02['normal'] = second_unitdate_range_string_1.replace('-', '/')
                    unitdate_2_range_tag_02.append(second_unitdate_range_string_1)
                    
                    
                if number_unitdate_ranges == 3:
                    #encoding the first date range when a unittitle contains three date ranges in its string
                    first_unitdate_range_string_00 = unitdate_array[0]
                    unitdate_3_1_soup = bs('<unitdate></unitdate>', features="xml")
                    unitdate_3_range_tag_01 = unitdate_3_1_soup.unitdate
                    unitdate_3_range_tag_01['encodinganalog'] = '245$f'
                    unitdate_3_range_tag_01['unitdatetype'] = 'inclusive'
                    unitdate_3_range_tag_01['normal'] = first_unitdate_range_string_00.replace('-', '/')
                    unitdate_3_range_tag_01.append(first_unitdate_range_string_00)
                    # print(unitdate_3_range_tag_01)
                    unitdate_range_element_string = str(first_unitdate_range_string_00)
                    
                    #encoding the second date range when a unittitle contains three date ranges in its string
                    second_unitdate_range_string_01 = date_array[1]
                    unitdate_3_2_soup = bs('<unitdate></unitdate>', features="xml")
                    unitdate_3_range_tag_02 = date_3_2_soup.date
                    unitdate_3_range_tag_02['encodinganalog'] = '245$f'
                    unitdate_3_range_tag_02['unitdatetype'] = 'inclusive'
                    unitdate_3_range_tag_02['normal'] = second_unitdate_range_string_01.replace('-', '/')
                    unitdate_3_range_tag_02.append(second_unitdate_range_string_01)
                    
                    #encoding the second date range when a unittitle contains three date ranges in its string
                    second_unitdate_range_string_02 = date_array[2]
                    unitdate_3_3_soup = bs('<unitdate></unitdate>', features="xml")
                    unitdate_3_range_tag_03 = date_3_3_soup.date
                    unitdate_3_range_tag_03['encodinganalog'] = '245$f'
                    unitdate_3_range_tag_03['unitdatetype'] = 'inclusive'
                    unitdate_3_range_tag_03['normal'] = second_unitdate_range_string_02.replace('-', '/')
                    unitdate_3_range_tag_03.append(second_unitdate_range_string_02)
                    
   
                if number_unitdate_ranges == 4:
                    #encoding the first date range when a unittitle contains three date ranges in its string
                    first_date_range_string_00 = date_array[0]
                    date_3_1_soup = bs('<date></date>', features="xml")
                    date_3_range_tag_01 = date_3_1_soup.date
                    date_3_range_tag_01['encodinganalog'] = '245$f'
                    date_3_range_tag_01['localtype'] = 'inclusive'
                    date_3_range_tag_01['normal'] = first_date_range_string_00.replace('-', '/')
                    date_3_range_tag_01.append(first_date_range_string_00)
                    # print(date_range_tag)
                    date_range_element_string = str(date_range_tag)
                    
                    #encoding the second date range when a unittitle contains three date ranges in its string
                    second_date_range_string_01 = date_array[1]
                    date_3_2_soup = bs('<date></date>', features="xml")
                    date_3_range_tag_02 = date_3_2_soup.date
                    date_3_range_tag_02['encodinganalog'] = '245$f'
                    date_3_range_tag_02['localtype'] = 'inclusive'
                    date_3_range_tag_02['normal'] = second_date_range_string_01.replace('-', '/')
                    date_3_range_tag_02.append(second_date_range_string_01)
                    
                    #encoding the second date range when a unittitle contains three date ranges in its string
                    second_date_range_string_02 = date_array[2]
                    date_3_3_soup = bs('<date></date>', features="xml")
                    date_3_range_tag_03 = date_3_3_soup.date
                    date_3_range_tag_03['encodinganalog'] = '245$f'
                    date_3_range_tag_03['localtype'] = 'inclusive'
                    date_3_range_tag_03['normal'] = second_date_range_string_02.replace('-', '/')
                    date_3_range_tag_03.append(second_date_range_string_02)
            
date_range()      
            
                    
# for tags in soup.find_all(unittitle_tags):
#     array = re.findall(r'[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]', tags.text.strip())
#     if not(tags.find('date')):
#         date_string = ' '.join(array)
#         date_range_test = bool(re.search(r'[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]', date_string))
#         if date_range_test is True:
#             date_range()
        
# for tags in soup.find_all(unittitle_tags):
#     array = re.findall(r'[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]', tags.text.strip())
#     if not(tags.find('date')):
#         date_string = ' '.join(array)
#         date_range_test = bool(re.search(r'[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]', date_string))
#         if date_range_test is True:
#             date_range()
            
            
# for tags in soup.find_all(unittitle_tags):
#     array = re.findall(r'[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]', tags.text.strip())
#     if not(tags.find('date')):
#         date_string = ' '.join(array)
#         date_range_test = bool(re.search(r'[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]', date_string))
#         if date_range_test is True:
#             date_range()
