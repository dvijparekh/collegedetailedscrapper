import requests
from bs4 import BeautifulSoup
import csv

def mainpage():
    allpage = 0
    while allpage>=100:
        print(allpage)
        title, details, cdetails, course, eligible, filename, getcoursedetails, facebookmainlink, twittermainlink, youtubemainlink, wikipideamainlink, address, email, contact, no_of_faculty, facilities=' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '
        mainpageurl = "https://media.careers360.com/colleges/list-of-media-journalism-colleges-in-India?page="+ str(allpage) +"&sort_filter=alpha"
        print(mainpageurl)
        mainpage_code = requests.get(mainpageurl)
        mainpage_text = mainpage_code.text
        mainpage_soup = BeautifulSoup(mainpage_text, 'html.parser')
        for outer_name in mainpage_soup.findAll('div',{'class':'content-box f-right'}):
            for inner_name in outer_name.findAll('div',{'class':'title'}):
                for name in inner_name.findAll('a'):
                        title = name.getText()
                        title_link = name.get('href')
                        filename = title + '.jpeg'
                        print(title)
                        print(title_link)
                        print(filename)
                        currentpage(title_link,title, details, cdetails, course, eligible, filename, getcoursedetails, facebookmainlink, twittermainlink, youtubemainlink, wikipideamainlink, address, email, contact, no_of_faculty, facilities)
        allpage= allpage+1
def currentpage(currentpageurl,title, details, cdetails, course, eligible, filename, getcoursedetails, facebookmainlink, twittermainlink, youtubemainlink, wikipideamainlink, address, email, contact, no_of_faculty, facilities):
        currentpage_code = requests.get(currentpageurl)
        currentpage_text = currentpage_code.text
        currentpage_soup = BeautifulSoup(currentpage_text,'html.parser')
        facilities = ""
        for outer_facilities in currentpage_soup.findAll('div',{'id':'facility'}):
            for middle_facilities in outer_facilities.findAll('div',{'class':'contentBlockSec'}):
                #for inner_facilities in middle_facilities.finAll('div',{'class':'facilitylist'}):
                    for deeper_facilities in middle_facilities.findAll('ul'):
                        for get_facilities in deeper_facilities.findAll('li'):
                            if facilities == "":
                                facilities = get_facilities.text.strip()
                                print(facilities)
                            else:
                                facilities= facilities + " , " + get_facilities.text.strip()
                                print(facilities)
        for outer_faculty in currentpage_soup.findAll('div',{'class':'contentBlockSec'}):
           for inner_faculty in outer_faculty.findAll('div',{'class':'facilityCounter'}):
                for get_faculty in inner_faculty.findAll('h4',{'class':'blockSubHeading'}):
                    no_of_faculty = get_faculty.string
                    print(no_of_faculty)
        count = 0
        for outer_otherlinks in currentpage_soup.findAll('div',{'class':'social-icon-left'}):
            for inner_otherlink in outer_otherlinks.findAll('ul',{'class':'blockInfoIco'}):
                for facebook_link in inner_otherlink.findAll('li'):
                    for myfacebooklink in facebook_link.findAll('a'):
                        if count == 0:
                            facebookmainlink = myfacebooklink.get('href')
                            print(facebookmainlink)
                        elif count == 1:
                            twittermainlink = myfacebooklink.get('href')
                            print(twittermainlink)
                        elif count == 2:
                            youtubemainlink = myfacebooklink.get('href')
                            print(youtubemainlink)
                        elif count == 3:
                            wikipideamainlink = myfacebooklink.get('href')
                            print(wikipideamainlink)
                        count= count+1
        address_count=0
        for outer_address in currentpage_soup.findAll('div',{'class':'mapInfocols'}):
            for inner_address in outer_address.findAll('div', {'class': 'mapInfoColInner'}):
                #for get_address in inner_address.findAll('h5',{'class':'titleMap'}):
                if address_count==0:
                    address =inner_address.text.strip()
                    print(address)
                elif address_count== 1:
                    email = inner_address.text.strip() + "."
                    print(email)
                elif address_count == 2:
                    contact = inner_address.text.strip()
                    print(contact)
                address_count=address_count+1
        details=""
        details_count=0
        for outer_details in currentpage_soup.findAll('div',{'class':'instituteInfo'}):
            for inner_details in outer_details.findAll('ul',{'class':'clg-info'}):
                if details_count == 0:
                    details= inner_details.text.strip()
                    print (details)
                    #course_link = currentpageurl + "/courses"
                elif details_count==1:
                    cdetails = inner_details.text.strip()
                    print("cdetails: " + cdetails)
                details_count=details_count+1

                for outer_course_link in currentpage_soup.findAll('ul',{'class':'list-tabs'}):
                    for inner_course_link in outer_course_link.findAll('li')[1]:
                        course_link = 'https://media.careers360.com' + inner_course_link.get('href')
        coursepage(course_link,title,details,cdetails,course, eligible,filename,facebookmainlink,twittermainlink,youtubemainlink,wikipideamainlink,address,email,contact,no_of_faculty,facilities)

def coursepage(coursepageurl,title,details,cdetails,course, eligible,filename,facebookmainlink,twittermainlink,youtubemainlink,wikipideamainlink,address,email,contact,no_of_faculty,facilities):
        coursepage_code = requests.get(coursepageurl)
        coursepage_text = coursepage_code.text
        coursepage_soup = BeautifulSoup(coursepage_text,'html.parser')
        pagination=''
        for outer_pagination in coursepage_soup.findAll('div',{'class':'item-list'}):
            pagination = len(outer_pagination.findAll('li'))-2

        forward =0
        if pagination =='':
            for outer_morecourse in coursepage_soup.findAll('span', {'class': 'readmore'}):
                for inner_morecourse in outer_morecourse.findAll('a', {'class': 'apply_btn'}):
                    morecourse = inner_morecourse.get('href')
                    main_link = 'https://media.careers360.com' + morecourse
                    print(main_link)
                    lastpage(main_link, title, details, cdetails,course, eligible, filename, facebookmainlink, twittermainlink,
                             youtubemainlink, wikipideamainlink, address, email, contact, no_of_faculty, facilities)
        else:
            #print(pagination)
            while forward < int(pagination):
                coursepageurl1 = coursepageurl + '?levelId=all&courseNid=all-all&page=' + str(forward)
                coursepage_code1 = requests.get(coursepageurl1)
                coursepage_text1 = coursepage_code1.text
                coursepage_soup1 = BeautifulSoup(coursepage_text1, 'html.parser')
                for outer_morecourse in coursepage_soup1.findAll('span', {'class': 'readmore'}):
                    for inner_morecourse in outer_morecourse.findAll('a', {'class': 'apply_btn'}):
                        morecourse = inner_morecourse.get('href')
                        main_link = 'https://media.careers360.com' + morecourse
                        print(main_link)
                        lastpage(main_link, title, details, cdetails, course, eligible, filename, facebookmainlink,
                                 twittermainlink, youtubemainlink, wikipideamainlink, address, email, contact,
                                 no_of_faculty, facilities)
                forward = forward + 1

def lastpage(lastpageurl,title,details,cdetails,course, eligible,filename,facebookmainlink,twittermainlink,youtubemainlink,wikipideamainlink,address,email,contact,no_of_faculty,facilities):
        lastpage_code = requests.get(lastpageurl)
        lastpage_text = lastpage_code.text
        lastpage_soup = BeautifulSoup(lastpage_text,'html.parser')
        for outer_coursename in lastpage_soup.findAll('h2',{'class':'block-title'}):
            course = outer_coursename.text.strip()
            print(course)
        if len(lastpage_soup.findAll('span',{'class':'more-eligibility'})) == 1:
            for moreeligible in lastpage_soup.findAll('span',{'class':'more-eligibility'}):
                eligible = moreeligible.text.strip()
                print(eligible)
        else:
            for moreeligible in lastpage_soup.findAll('div',{'class':'default-elig'}):
                eligible = moreeligible.text.strip()
                print(eligible)
        getcoursedetails=""
        for coursedetails in lastpage_soup.find('div',{'class':'coursesPageBottomLable'}):
            if getcoursedetails=="":
                getcoursedetails = coursedetails.text.strip()
                print(getcoursedetails)
            else:
                getcoursedetails = getcoursedetails + " , " + coursedetails.text.strip()
                print(getcoursedetails)
        write_to_csv(title,details,cdetails,course,eligible,filename,getcoursedetails,facebookmainlink,twittermainlink,youtubemainlink,wikipideamainlink,address,email,contact,no_of_faculty,facilities)

def write_to_csv(clg_name,clg_details,cdetails,clg_course,clg_eligible,clg_filename,clg_coursedetails,facebookmainlink,twittermainlink,youtubemainlink,wikipideamainlink,address,email,contact,no_of_faculty,facilities):
    with open('media&journalism.csv', 'a') as csvfile:
        fieldnames = ['name', 'details', 'cdetails' , 'course', 'eligible', 'logoname' , 'coursedetails','facebookmainlink','twittermainlink','youtubemainlink','wikipideamainlink','address','email','contact','no_of_faculty',',facilities']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'name': clg_name, 'details': clg_details,'cdetails':cdetails, 'course': clg_course, 'eligible': clg_eligible, 'logoname' : clg_filename,'coursedetails': clg_coursedetails,'facebookmainlink':facebookmainlink,'twittermainlink':twittermainlink,'youtubemainlink':youtubemainlink,'wikipideamainlink':wikipideamainlink,'address':address,'email':email,'contact':contact,'no_of_faculty':no_of_faculty,',facilities':facilities})

mainpage()
