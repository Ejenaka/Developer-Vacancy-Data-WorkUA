import tkinter as tk
import tkinter.font as tkFont
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.font_style = tkFont.Font(family="Lucida Grande", size=20)

        self.button = tk.Button(parent,
                                text='Получить статистику',
                                command=self.get_statistic,
                                font=self.font_style,
                                width=20)

        self.label = tk.Label(parent,
                              text='Выберите город',
                              font=self.font_style)

        self.listbox = tk.Listbox(width=20)

        self.citydict = {
            'Киев': 'kyiv',
            'Днепр': 'dnipro',
            'Харьков': 'kharkiv',
            'Львов': 'lviv',
            'Запорожье': 'zaporizhzhya',
            'Николаев': 'mykolaiv_nk',
            'Винница': 'vinnytsya',
            'Черкасы': 'cherkasy',
            'Полтава': 'poltava',
        }

        keys = list(self.citydict.keys())
        keys.reverse()
        for i in keys:
            self.listbox.insert(0, i)

        self.label.pack()
        self.listbox.pack()
        self.button.pack()

    def get_url(self):
        city_index = self.listbox.curselection()
        city_name = self.listbox.get(city_index)
        city_id = self.citydict[city_name]
        url = 'https://www.work.ua/jobs-{}-developer/?page='.format(city_id)
        return url

    def get_data(self):
        url = self.get_url()
        page = '1'
        final_url = url + page
        source = requests.get(final_url).text
        soup = BeautifulSoup(source, 'lxml')
        pages = []
        for page in soup.find_all('a'):
            try:
                pages.append(int(page.text))
            except:
                pass
        vacancies = []
        if pages:
            max_page = max(pages)
        else:
            max_page = 1

        for new_page in range(1, max_page + 1):
            final_url = url + str(new_page)
            source = requests.get(final_url).text
            soup = BeautifulSoup(source, 'lxml')
            for header in soup.find_all('h2'):
                vacancies.append(header.text.rstrip().lstrip())
            vacancies.pop(-1)

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
        return sorted_data

    def get_statistic(self):
        plt.close()
        data = self.get_data()
        plt.barh(list(data.keys()), list(data.values()))
        plt.title(
            f"Статистика по городу: {self.listbox.get(self.listbox.curselection())}")
        plt.subplots_adjust(left=0.26)
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Статистика вакансий программистов')
    root.resizable(False, False)
    MainApplication(root)
    root.mainloop()
