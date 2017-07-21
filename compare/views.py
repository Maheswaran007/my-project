from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from lxml import html  
import requests
def load(request):
	return render(request,'mainpage.html',)	
def compare(request, value=None):
	li=list()
	first=''
	second=''
	third=''
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	if(value== "1"):
		li.insert(0,'http://www.bak2life.fr/3073/apple-iphone-6-plus-grey-16gb.jpg')
		Aurl='http://www.amazon.in/Apple-iPhone-Space-Grey-32GB/dp/B01NCN4ICO/ref=sr_1_2?ie=UTF8&qid=1499747027&sr=8-2&keywords=iphone+6%5C'

		Furl='https://www.flipkart.com/apple-iphone-6-space-grey-32-gb/p/itmetmh3hfhnxtcj?pid=MOBETMH3ZYNDPVVC&srno=b_1_1&otracker=clp_metro_expandable_1_apple-categ-94e9d_iPhone_apple-products-store_90ff40fd-a46b-4a40-9440-fbe783136afb_DesktopSite_wp1&lid=LSTMOBETMH3ZYNDPVVC7BAC1S'

		Curl='https://www.croma.com/apple-iphone-6-space-grey-32gb-/p/202452'

	if(value== "2"):
		li.insert(0,'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone7/jetblack/iphone7-jetblack-select-2016?wid=300&hei=300&fmt=png-alpha&qlt=95&.v=1472430076339')
	 	Aurl='http://www.amazon.in/Apple-iPhone-7-Black-32GB/dp/B01LZKSVRB/ref=sr_1_1?s=electronics&ie=UTF8&qid=1499774442&sr=1-1&keywords=iphone+7'

		Furl='https://www.flipkart.com/apple-iphone-7-black-32-gb/p/itmen6daftcqwzeg?pid=MOBEMK62PN2HU7EE&srno=s_1_1&otracker=search&lid=LSTMOBEMK62PN2HU7EEINTGNU&qH=5d05ddab4536111a'
	
		Curl='https://www.croma.com/apple-iphone-7-black-32gb-mobile-phone/p/199216'
	
	if(value=="3"):
		li.insert(0,'https://gadgetstouse.com/wp-content/uploads/2017/06/Samsung-Galaxy-J7-Pro-1.jpg')
		Aurl='http://www.amazon.in/Samsung-Galaxy-J7-Max-Black/dp/B073PWDMHD/ref=sr_1_2?ie=UTF8&qid=1499832612&sr=8-2&keywords=samsung+j7+max'

		Furl='https://www.flipkart.com/samsung-j7-max-black-32-gb/p/itmev5vtbw8pmatj?pid=MOBEV5VTG57KHRYV&srno=s_1_2&otracker=search&lid=LSTMOBEV5VTG57KHRYVBKKB8S&qH=8c1bfab508ff35b6'
		
		Curl='https://www.croma.com/samsung-galaxy-j7-max-black-32gb-mobile-phone/p/203870'
	if(value=="4"):
		li.insert(0,'https://s1.bukalapak.com/img/1467606711/m-1000-1000/OPPO_F3_PLUS_GRANSI_RESMI_INDONESIA_SETAHUN.png')
		Aurl='http://www.amazon.in/OPPO-F3-Black-64-GB/dp/B072Q7DDVR/ref=sr_1_4?s=electronics&ie=UTF8&qid=1499832960&sr=1-4&keywords=oppo'

		Furl='https://www.flipkart.com/oppo-f3-black-64-gb/p/itmeumw5sejzmmym?pid=MOBEUMW44EWAX9VE&srno=s_1_1&otracker=search&lid=LSTMOBEUMW44EWAX9VEGFGJQK&qH=c892ba238c98835d'
		Curl='https://www.croma.com/oppo-f3-black-64gb-mobile-phone/p/203753'
	#Amazon
	Apage = requests.get(Aurl,headers=headers)
	doc = html.fromstring(Apage.content)
	XPATH_NAME = '//h1[@id="title"]//text()'
	XPATH_SALE_PRICE = '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()'
	OTHER_XPATH_SALE_PRICE = '//span[contains(@class,"a-color-price") or contains(@id,"saleprice")]/text()'
 	RAW_NAME = doc.xpath(XPATH_NAME)
	RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
	OTHER_RAW_SALE_PRICE = doc.xpath(OTHER_XPATH_SALE_PRICE)
	OTHER_PRICE = ' '.join(''.join(OTHER_RAW_SALE_PRICE).split()).strip() if OTHER_RAW_SALE_PRICE else None 
	ANAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
	ASALE_PRICE = ''.join(RAW_SALE_PRICE).strip() if RAW_SALE_PRICE else None
	AOTHER_PRICE=OTHER_PRICE.partition(' ')[0]
	
	#Flipkart
	Fpage = requests.get(Furl,headers=headers)
	doc = html.fromstring(Fpage.content)
	XPATH_NAME = '//h1[@class="_3eAQiD"]//text()'
	XPATH_SALE_PRICE = '//div[contains(@class,"_1vC4OE _37U4_g")]/text()'
	RAW_NAME = doc.xpath(XPATH_NAME)
	RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
	FNAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
	FPRICE = ''.join(RAW_SALE_PRICE).strip() if RAW_SALE_PRICE else None
	FPRICE=FPRICE[1:]
	
	#Croma
	Cpage = requests.get(Curl,headers=headers)
	doc = html.fromstring(Cpage.content)
	XPATH_NAME = '//h1[@style="text-transform: uppercase;"]//text()'
	XPATH_SALE_PRICE = '//h2[@style="font-size: 20px;"]/text()'
	XPATH_MRP_PRICE = '//span[@style="text-decoration: line-through;"]/text()'
	RAW_NAME = doc.xpath(XPATH_NAME)
	RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
	RAW_MRP_PRICE = doc.xpath(XPATH_MRP_PRICE)
	CNAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
	CSALE_PRICE = ''.join(RAW_SALE_PRICE).strip() if RAW_SALE_PRICE else None
	CMRP_PRICE = ''.join(RAW_MRP_PRICE).strip() if RAW_MRP_PRICE else None
	
	flag=0
	if ASALE_PRICE<=AOTHER_PRICE:
		APRICE=ASALE_PRICE
	else:
		APRICE=AOTHER_PRICE
		flag=1
	if APRICE<=FPRICE and APRICE<=CSALE_PRICE:
		first='Amazon '+APRICE
		if FPRICE<=CSALE_PRICE:
			second='Flipkart '+FPRICE
			third='Corma '+CSALE_PRICE
		else:
			second='Corma '+CSALE_PRICE
			third='Flipkart '+FPRICE
	if FPRICE<=APRICE and FPRICE<=CSALE_PRICE:
		first='Flipkart '+FPRICE
		if APRICE<=CSALE_PRICE:
			second='Amazon '+APRICE
			third='Corma '+CSALE_PRICE
		else:
			second='Corma '+CSALE_PRICE
			third='Amazon  '+APRICE
	if CSALE_PRICE<=APRICE and CSALE_PRICE<=FPRICE:
		first='Corma '+CSALE_PRICE
		if APRICE<=FPRICE:
			second='Amazon '+APRICE
			third='Flipkart '+FPRICE
		else:
			second='Flipkart '+FPRICE
			third='Amazon  '+APRICE
	li.insert(1,ANAME)
	li.insert(2,first)
	li.insert(3,second)
	li.insert(4,third) 
	return  render_to_response('Result.html',{'posts' : li})	
	
