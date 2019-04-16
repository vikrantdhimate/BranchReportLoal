from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
response = urlopen('http://ci-datastore.vse.rdlabs.hpecorp.net/nextgen/test_failure_summary?program=3&branch_name=rel%2F5.00&created_after=-24h&annotation=dailystability')
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')

f = open("Report.txt", "w")

#Branch Status
for x in soup.find_all("h4"): #for passed tests just change fail to pass
    print(x.text + "\n");
    f.write(x.text + "\n");
    break;

#Passed Count
passed = 0;
for x in soup.find_all("div", attrs={'class':'panel-heading pass'}, id = re.compile("test-*")): #for passed tests just change fail to pass
    passed = passed + 1;
print("Total Success are : " + str(passed));
f.write("Total Success are : " + str(passed) + "\n");


#Failed Count
failed = 0;
for x in soup.find_all("div", attrs={'class':'panel-heading fail'}, id = re.compile("test-*")): #for passed tests just change fail to pass
    failed = failed + 1;
print("Total Failures are : " + str(failed));
f.write("Total Failures are : " + str(failed) + "\n")


#For passed Tests list
print("Failed Tests : ");
f.write("Failed Tests : " + "\n")
for x in soup.find_all("div", attrs={'class':'panel-heading fail'}, id = re.compile("test-*")): #for passed tests just change fail to pass
    for a in x.find_all('a'):
        print(a.text);
        f.write(a.text);

f.write("\n");

#For Failed Tests list
print("Passed Tests : ");
f.write("Passed Tests : " + "\n")
for x in soup.find_all("div", attrs={'class':'panel-heading pass'}, id = re.compile("test-*")): #for passed tests just change fail to pass
    for a in x.find_all('a'):
        print(a.text);
        f.write(a.text);
f.write("\n");	

f.close();
