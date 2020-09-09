from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt


# finding max pages
url = 'https://www.work.ua/jobs-kyiv-developer/?advs=1&page='
page = '1'

finall_url = url + page
sourse = requests.get(finall_url).text
soup = BeautifulSoup(sourse, 'lxml')

links_text = []

for link in soup.find_all('a'):
    try:
        links_text.append(int(link.text))
    except:
        pass

max_pages = max(links_text)
vacancies = []

# finding text of <a> through all pages
for new_page in range(1, max_pages + 1):
    finall_url = url + str(new_page)
    sourse = requests.get(finall_url).text
    soup = BeautifulSoup(sourse, 'lxml')
    for header in soup.find_all('h2'):
        vacancies.append(header.text.rstrip().lstrip())
    vacancies.pop(-1)

# lower case the list
vacancies = tuple(map(lambda string: string.casefold(), vacancies))

# lists of current jobs
php = [job for job in vacancies if job.find(
    'php') != -1 or job.find('рнр') != -1]
sql = [job for job in vacancies if job.find(
    'sql') != -1 or job.find('база') != -1 or job.find('base') != -1]
front_end = [job for job in vacancies if job.find(
    'front') != -1]
python = [job for job in vacancies if job.find(
    'python') != -1 or job.find('django') != -1]
nodejs = [job for job in vacancies if job.find(
    'node') != -1]
web_dev = [job for job in vacancies if job.find(
    'web') != -1]
one_c = [job for job in vacancies if job.find(
    '1c') != -1 or job.find('1с') != -1]
full_stack = [job for job in vacancies if job.find(
    'full') != -1]
ruby = [job for job in vacancies if job.find(
    'ruby') != -1]
backend = [job for job in vacancies if job.find(
    'back') != -1]
js = [job for job in vacancies if job.find(
    'javascript') != -1 or job.find('js') != -1]
c_sharp_and_net = [job for job in vacancies if job.find(
    'c#') != -1 or job.find('.net') != -1]
drupal = [job for job in vacancies if job.find(
    'drupal') != -1]
word_press = [job for job in vacancies if job.find(
    'wordpress') != -1]
android = [job for job in vacancies if job.find(
    'android') != -1]
unity = [job for job in vacancies if job.find(
    'unity') != -1]
cpp = [job for job in vacancies if job.find(
    'c++') != -1]
ios = [job for job in vacancies if job.find(
    'ios') != -1]
java = [job for job in vacancies if job.find(
    'java ') != -1]
golang = [job for job in vacancies if job.find(
    'golang') != -1]
bigdata = [job for job in vacancies if job.find(
    'bigdata') != -1]
mobile = [job for job in vacancies if job.find(
    'mobile') != -1 or job.find('мобил') != -1]

# creating dictionary that represents lenght of arrays --> count of vacancies of each job
data = {
    'PHP': len(php),
    'SQL': len(sql),
    'Front-End': len(front_end),
    'Python': len(python),
    'Node.js': len(nodejs),
    'Web Development': len(web_dev),
    '1C': len(one_c),
    'Full-Stack': len(full_stack),
    'Ruby': len(ruby),
    'Back-End': len(backend),
    'JavaScript': len(js),
    'C# and .NET': len(c_sharp_and_net),
    'Drupal': len(drupal),
    'WordPress': len(word_press),
    'Android': len(android),
    'Unity': len(unity),
    'C++': len(cpp),
    'IOS': len(ios),
    'Java': len(java),
    'Go': len(golang),
    'BigData': len(bigdata),
    'Mobile Development': len(mobile),
}

sorted_data = {k: v for k, v in sorted(
    data.items(), key=lambda item: item[1])}

plt.barh(list(sorted_data.keys()), list(sorted_data.values()), )

plt.show()
