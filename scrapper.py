from bs4 import BeautifulSoup
import json
import requests


if __name__== "__main__":
    url = "http://www.artsandscience.utoronto.ca/ofr/timetable/winter/"
    timetable = requests.get("http://www.artsandscience.utoronto.ca/ofr/timetable/winter/")
    timetable_soup = BeautifulSoup(timetable.content)
    department_tag = timetable_soup.findAll("a")[0:75]
    department_url = list()

    for a in department_tag:
        department_url.append(url + a['href'])

    dept_req_list = list()
    for res in department_url:
        course_table = requests.get(res)
        dept_req_list.append(BeautifulSoup(course_table.content))

#get row-> check first td tag-> check for a tag -> if none a sub section