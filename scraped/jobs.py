import schedule
import threading
import time
from .models import Details,image,Video
import requests
import os
from bs4 import BeautifulSoup

from apscheduler.schedulers.background import BackgroundScheduler
from django_q.tasks import schedule

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def weworkSrcipe():
    title_list = []
    link_list = []
    image_list = []
    thumb_list = []
    t = 0
    check = True

    video_list = []
    url = "https://sorrymother.video/"

    while check:
        try:
            html = requests.get(url, headers=headers).text
            soup = BeautifulSoup(html, 'lxml')

            section = soup.find_all("li", {"class": "g1-collection-item g1-collection-item-1of3"})

            for item in section:
                one = item.find("h3", {"class": "g1-gamma g1-gamma-1st entry-title"})
                link = item.find("a", {"class": "g1-frame"})
                thumb_div = item.find("img")
                # thumb = thumb_div.get('image-file')
                # print(thumb_div['data-src'])
                try:
                    # print(thumb['href'])
                    htmll = requests.get(link['href'], headers=headers).text
                    soupp = BeautifulSoup(htmll, 'lxml')
                    # print(htmll)
                    sec = soupp.find("div", {
                        "class": "g1-content-narrow g1-typography-xl entry-content"})
                    i = sec.find_all("img")
                    # print(i)
                    # print(len(i))
                    #
                    # print("Start")

                    # print(img)
                    star_image = []
                    for n in range(len(i)):
                        # print(i[n]['data-src'])
                        # print("next")
                        star_image.append(i[n]['data-src'])
                    # print(star_image)
                    link_list.append(link['href'])
                    title_list.append(one.text.strip())
                    thumb_list.append(thumb_div['data-src'])
                    job = Details(title=one.text.strip(), thumbnail_img=thumb_div['data-src'])

                    job.save()
                    print(job)
                    image_list.append(star_image)
                    for i in star_image:
                        im=image(image=i,author=job)
                        im.save()

                    name = soupp.find("h1", {"class": "g1-mega g1-mega-1st entry-title"})
                    video = soupp.find("div", {"class": "g1-content-narrow g1-typography-xl entry-content"})
                    v = video.select("video>source")
                    try:
                        list = []
                        for l in v:
                            list.append(l['src'])
                            print(list)
                        for i in list:
                            vi = Video(video=i, author=job)
                            vi.save()
                        # print(v)

                        # print(video['src'])
                    except:
                        pass
                    # print(title_list)
                except:
                    continue

            pages = soup.find("div", {"class": "g1-collection-more-inner"}).find_all('a', {
                "class": "g1-button g1-button-m g1-button-solid g1-load-more"})
            print(len(pages))
            if len(pages) > 0:
                url = pages[0]["data-g1-next-page-url"]
                print(url)

            else:
                check = False

        except:
            break

#
# def newWork():
#     title_list = []
#     link_list = []
#     image_list = []
#     thumb_list = []
#     check = True
#     t = 0
#     list = []
#     video = []
#     url = "https://www3.onlyfansleaks.net/"
#
#     while check:
#         if t < 100:
#             html = requests.get(url, headers=headers).text
#             soup = BeautifulSoup(html, 'lxml')
#             section = soup.find_all("li", {"class": "g1-collection-item g1-collection-item-1of3"})
#             # print(section)
#             for item in section:
#                 one = item.find("h3", {"class": "g1-gamma g1-gamma-1st entry-title"})
#                 link = item.find("a", {"class": "g1-frame"})
#                 thumb_div = item.find("img")
#                 # print(thumb_div)
#                 try:
#                     # print(thumb['href'])
#                     htmll = requests.get(link['href'], headers=headers).text
#                     soupp = BeautifulSoup(htmll, 'lxml')
#                     # print(htmll)
#
#                     sec = soupp.find_all("div", {"class": "g1-frame-inner"})
#
#                     a = None
#                     # print("next:")
#                     star_image = []
#                     for i in sec:
#                         img = i.find_all("img")
#                         # print(img[0]['data-src'])
#                         star_image.append(img[0]['data-src'])
#                     # print(star_image)
#                     link_list.append(link['href'])
#                     title_list.append(one.text.strip())
#                     thumb_list.append(thumb_div['data-src'])
#                     image_list.append(star_image)
#                 except:
#                     continue
#
#             # print(len(title_list))
#             # print(title_list)
#             #
#             # print(link_list)
#             # print(len(link_list))
#             #
#             # print(image_list)
#
#             dict = {'title': title_list, 'link': link_list, 'thumb': thumb_list, 'image': image_list}
#             df5 = pd.DataFrame(dict)
#             df5.to_csv(os.path.join(BASE_DIR, f'output\\test2.csv'), encoding='utf-8')
#             #
#             try:
#                 pages = soup.find("div", {"class": "g1-collection-more-inner"}).find('a', {
#                     "class": "g1-button g1-button-m g1-button-solid g1-load-more"})
#                 print(len(pages))
#                 if len(pages) > 0:
#                     url = pages["data-g1-next-page-url"]
#                     print(url)
#                     t = t + 1
#                 else:
#                     check = False
#             except:
#                 t = t + 1
#                 print(t)
#                 continue
#
#
# def newWork2():
#     title_list = []
#     link_list = []
#     image_list = []
#     thumb_list = []
#     check = True
#     t = 0
#
#     video_list = []
#     url = "http://www.onlyfansx.club"
#     while check:
#         if t < 100:
#             html = requests.get(url, headers=headers).text
#             soup = BeautifulSoup(html, 'lxml')
#             section = soup.find_all("li", {"class": "g1-collection-item g1-collection-item-1of3"})
#             # print(section)
#             for item in section:
#                 one = item.find("h3", {"class": "g1-gamma g1-gamma-1st entry-title"})
#                 # print(one)
#                 link = item.find("a", {"class": "g1-frame"})
#                 # print(link)
#                 thumb_div = item.find("img")
#                 # print(thumb_div)
#                 try:
#                     # print(thumb['href'])
#                     htmll = requests.get(link['href'], headers=headers).text
#                     soupp = BeautifulSoup(htmll, 'lxml')
#                     # print(htmll)
#
#                     sec = soupp.find_all("div", {"class": "g1-frame-inner"})
#                     # print(sec)
#
#                     a = None
#                     # print("next:")
#                     star_image = []
#                     for i in sec:
#                         img = i.find_all("img")
#                         # print(img[0]['data-src'])
#                         star_image.append(img[0]['data-src'])
#                     # print(star_image)
#                     link_list.append(link['href'])
#                     title_list.append(one.text.strip())
#                     thumb_list.append(thumb_div['data-src'])
#                     image_list.append(star_image)
#
#                     # name = soupp.find("h1", {"class": "g1-link g1-link-m g1-link-right next"})
#
#                 except:
#                     continue
#                     # print(len(title_list))
#
#                     # print(link_list)
#
#                     # print(thumb_list)
#                     # print(image_list)
#                     # print(len(image_list))
#
#                 dict = {'title': title_list, 'link': link_list, 'thumb': thumb_list, 'image': image_list
#                         }
#                 df6 = pd.DataFrame(dict)
#                 df6.to_csv(os.path.join(BASE_DIR, f'output\\test3.csv'), encoding='utf-8')
#
#                 pages = soup.find("nav", {"class": "g1-pagination"}).select('a', {
#                     "class": "g1-button g1-button-m g1-button-solid g1-load-more"})
#                 # print(len(pages))
#                 if len(pages) > 0:
#                     url = pages[-1]["href"]
#                     print(url)
#
#                 else:
#                     check = False
#                 t = t + 1
#         else:
#             break



def Command():
    print('Called')
    Details.objects.all().delete()
    weworkSrcipe()
    # newWork()
    # newWork2()





def run_continuously(self, interval=10):
    """Continuously run, while executing pending jobs at each elapsed
    time interval.
    @return cease_continuous_run: threading.Event which can be set to
    cease continuous run.
    Please note that it is *intended behavior that run_continuously()
    does not run missed jobs*. For example, if you've registered a job
    that should run every minute and you set a continuous run interval
    of one hour then your job won't be run 60 times at each interval but
    only once.
    """

    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):

        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                self.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.setDaemon(True)
    continuous_thread.start()
    return cease_continuous_run


BackgroundScheduler.run_continuously = run_continuously


def start_scheduler():
    print("hi")
    scheduler = BackgroundScheduler()
    scheduler.add_job(Command, 'interval', minutes=1)
    scheduler.start()
    # schedule.every(1).minutes.do(Command)
    #
    # while True:
    #     schedule.run_pending()
    #     time.sleep(10)

# Command()
