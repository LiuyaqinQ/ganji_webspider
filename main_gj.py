from multiprocessing import Pool
from channel_extract import link_list
from page_analysis import get_urls_from_onepage,url_list,get_contens_from_oneurl
import time


# print ([url['url'] for url in url_list.find()
# def get_all_links_from(channel):
# 	for num in range(1,101):
# 		if not get_urls_from_onepage(channel,num):break#reduec the null search
#
# if __name__=='__main__' :
# 	pool=Pool(processes=6)
# 	pool.map(get_all_links_from,link_list.split())
# TypeError: filter must be an instance of dict, bson.son.SON, or other type that inherits from collections.Mapping
if __name__=='__main__':
	pool=Pool(processes=6)
	pool.map(get_contens_from_oneurl,[url['url'] for url in url_list.find()])
	# index=1
	# for link in url_list.find():
	# 	url=(link['url'])
	# 	get_contens_from_oneurl(url)
	# 	print(index)
	# 	index += 1


