from multiprocessing import Pool
from channel_extract import link_list
from page_analysis import get_urls_from_onepage,url_list,get_contens_from_oneurl,url_contents
import time

total_url=[item['url']  for item in url_list.find()]
saved_url=[item['url']  for item in url_contents.find()]

total_url_set=set(total_url)
saved_url_set=set(saved_url)
left_url_set=total_url_set-saved_url_set

# while left_url_set:
print(left_url_set,len(left_url_set),len(total_url_set))
if __name__=='__main__':
	pool=Pool(processes=6)
	pool.map(get_contens_from_oneurl,list(left_url_set))



