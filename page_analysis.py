#coding=utf-8
from bs4 import BeautifulSoup
import requests,pymongo,time,random
client=pymongo.MongoClient('localhost',27017)
ganji=client['ganji']
url_list=ganji['url_list']
url_contents=ganji['url_contents_new']
headers  = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Connection':'keep-alive',
	'Host':'bj.ganji.com'
}

# http://cn-proxy.com/
proxy_list = [
    'http://117.177.250.151:8081',
    'http://111.85.219.250:3129',
    'http://122.70.183.138:8118',
    ]
proxy_ip = random.choice(proxy_list) # 随机获取代理ip
proxies = {'http': proxy_ip}

def get_urls_from_onepage(url,num,seller_type=1):
	url_new='{}o{}/{}/'.format(url,str(num),str(seller_type))
	time.sleep(1)
	print (url_new)
	db=requests.get(url_new)
	soup=BeautifulSoup(db.text,'lxml')
	# wrapper > div.leftBox > div.layoutlist > div > dl > dt > img
	Empty=soup.select('div > div.noinfotishi,div > dl > dt > img')
	if not Empty :
		#nongchanping #GcnADId1 > ul > li:nth-child(3) > span.Gcn-info > a
		#jiaju  #infolist > div.infocon > table > tbody > tr:nth-child(1) > td.t > a
		# jingzhun > tbody > tr:nth-child(3) > td.t > a
		# #wrapper > div.leftBox > div.layoutlist > dl:nth-child(1) > dt > div > a
		# wrapper > div.leftBox > div.layoutlist > dl:nth-child(1) > dt > div > a
		links=soup.select(' tbody > tr > td.t > a , dt > div > a')
		for link in links:
			url=link.get('href')
			print(url)
			if url:
				url_list.insert_one({'url':url})
		return True#reduec the null search
	else:
		return False#reduec the null search
		pass
# get_urls_from_onepage('http://bj.ganji.com/ershoufree/',11)
def get_contens_from_oneurl(url,trytime=3):
	db=requests.get(url)
	time.sleep(1)
	print(url)
	try:
		if db.status_code==404 :
			pass
		else:
			soup = BeautifulSoup(db.text, 'lxml')
			if url.find('ganji') and  url.find('zhuanzhuan')==-1:
				# wrapper > div.content.clearfix > div.leftBox > div:nth-child(2) > div > ul > li:nth-child(5) > label

				info={
					'title': soup.select('div.box_left_top > h1,div.col-cont.title-box > h1')[0].text.strip(),
					'price': soup.select('.f22.fc-orange.f-type')[0].text.strip(),
					##can't get the seller_name cause the the name is not in label,with analysis
					'seller_name': soup.select('div > ul > li:nth-of-type(5) ')[2].text[4:12].strip(),
					'cates': list(soup.select('ul.det-infor > li:nth-of-type(1) > span')[0].stripped_strings)[0],
					'area': list(map(lambda x: x.text, soup.select('ul.det-infor > li:nth-of-type(3) > a'))),
					'pub_date': soup.select('.pr-5')[0].text.strip().split(' ')[0],
					'product_description': soup.select('div.leftBox > div > div.det-summary > div > div')[0].text.strip(),
					'url': url
				}
				print(info)
				# print(soup.select('div > ul > li:nth-of-type(5) ')[2].text[0:12])
				# print(soup.select('div > ul > li:nth-of-type(5) ').find)
				url_contents.insert_one(info)
			elif url.find('zhuanzhuan') and url.find('ganji'):
				info={
					#title body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.box_left_top > h1
					#name body > div.content > div > div.box_right > div:nth-child(1) > div.personal_jieshao > p.personal_name
					# area body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.palce_li > span > i
					# pub_date
					# product description body > div.content > div > div.box_left > div:nth-child(2) > div > div > p

					'title': soup.select('div.box_left_top > h1,div.col-cont.title-box > h1')[0].text.strip(),
					'price': soup.select('.price_now > i')[0].text.strip(),
					'seller_name': soup.select('p.personal_name')[0].text.strip(),
					'cates': 'None',
					'area': soup.select('div.palce_li > span > i')[0].text.strip(),
					'pub_date': 'None',
					'product_description': soup.select('div.box_left > div:nth-of-type(2) > div > div > p')[0].text.strip(),
					'url': url
				}
				print(info)
				url_contents.insert_one(info)
	except IndexError:
		print('once again')
		trytime = trytime - 1
		if trytime >0 :get_contens_from_oneurl(url,trytime)
		else:pass
		#d当商品下架后


get_contens_from_oneurl('http://bj.ganji.com/qitawupin/2460000546x.htm')
# get_contens_from_oneurl('http://zhuanzhuan.ganji.com/detail/818785355977768966z.shtml?from=pc&source=ganji&cate=&cateurl=')
# get_contens_from_oneurl('http://zhuanzhuan.ganji.com/detail/819715470826455048z.shtml')
#wrapper > div.content.clearfix > div.leftBox > div:nth-child(2) > div > ul > li:nth-child(2) > i




