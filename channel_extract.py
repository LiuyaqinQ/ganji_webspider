from bs4 import BeautifulSoup
import requests
url='http://bj.ganji.com/wu'
headers={
	'Cookie':'citydomain=bj; ganji_uuid=5789851934091298126071; ganji_xuuid=2d6cabf2-07a6-475c-8921-7ef5a37868f1.1484121249327; ganji_login_act=1484184168766; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A32269278352%7D; __utma=32156897.1153995792.1484121249.1484121249.1484182669.2; __utmb=32156897.2.10.1484182669; __utmc=32156897; __utmz=32156897.1484121249.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); GANJISESSID=8d8bc30fa0e4c492f2a26096c2b54a53; 58uuid=7477edc8-7d0a-437a-83f8-4d6885e2e6c7; new_session=0; init_refer=; new_uv=1; lg=1',
	'Host':'bj.ganji.com',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	'User_Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}
def get_links(url):
	response=requests.get(url)
	soup=BeautifulSoup(response.text,'lxml')
	# print(soup.prettify())
	links=soup.select('div > div > div > dl > dt > a')
	for link in links:
		print('http://bj.ganji.com'+link.get('href'))
# get_links(url)
link_list='''
http://bj.ganji.com/jiaju/
http://bj.ganji.com/rirongbaihuo/
http://bj.ganji.com/shouji/
http://bj.ganji.com/shoujihaoma/
http://bj.ganji.com/bangong/
http://bj.ganji.com/nongyongpin/
http://bj.ganji.com/jiadian/
http://bj.ganji.com/ershoubijibendiannao/
http://bj.ganji.com/ruanjiantushu/
http://bj.ganji.com/yingyouyunfu/
http://bj.ganji.com/diannao/
http://bj.ganji.com/xianzhilipin/
http://bj.ganji.com/fushixiaobaxuemao/
http://bj.ganji.com/meironghuazhuang/
http://bj.ganji.com/shuma/
http://bj.ganji.com/laonianyongpin/
http://bj.ganji.com/xuniwupin/
http://bj.ganji.com/qitawupin/
http://bj.ganji.com/ershoufree/
http://bj.ganji.com/wupinjiaohuan/
'''