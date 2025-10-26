

#This app scrap data from booking.com

''''
give the url,file name
greetings
start scrapping 
hotel_name
price 
location
ratings
reviews
link
save the file


'''


import requests
from bs4 import BeautifulSoup
import lxml
import csv
import time
import random



   #url_text=https://www.booking.com/searchresults.html?ss=New+Delhi%2C+Delhi+NCR%2C+India&efdco=1&label=gen173rf-10CAEoggI46AdIM1gDaGyIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGiAgpnaXRodWIuY29tqAIBuAKWtuTHBsACAdICJGU3YmFhOTNlLTVlODItNDYyNC05ZTAzLTM2MzJkYmQ4NzEzYtgCAeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-2106102&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=03ce7e4b6402054b&ac_meta=GhAwM2NlN2U0YjY0MDIwNTRiIAAoATICZW46BWRlbGhpQABKAFAA&checkin=2025-11-01&checkout=2025-11-02&group_adults=2&no_rooms=1&group_children=0



def web_scrapper2(web_url,f_name):
  #greetings 
 print("Thank you sharing the url and file name!\nstarting the webscraping")
 num=random.randint(3,7)
 time.sleep(num)


 header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'}


 response=requests.get(web_url,headers=header)

 print(response.status_code)


 if response.status_code==200:
    print("Connected to the website")
    html_content=response.text

    #creating soup

    soup= BeautifulSoup(html_content,'lxml')
    #print(soup.prettify())
    

    #main containers
    hotel_divs=soup.find_all('div',class_="c3bdfd4ac2 a0ab5da06c d46ff48a92 f728e61e72 d0acd69e66 c256f1a28a bc2204a477")
    #print(hotel_divs)

    with open(f'{f_name}.csv','w',encoding='utf-8') as file_csv:
     writer=csv.writer(file_csv)
        #adding header
     writer.writerow(['hotel_name','locality','price','rating','score','review','link'])

     for hotel in hotel_divs:

        hotel_name=hotel.find('div',class_="b87c397a13 a3e0b4ffd1").text.strip()
        hotel_name if hotel_name else 'NA'
        location=hotel.find('span',class_="d823fbbeed f9b3563dd4").text.strip()
        location if location else 'NA'
        price=hotel.find('span',class_="b87c397a13 f2f358d1de ab607752a2").text.replace('₹ ','')
        price if price else 'NA'
        ratings=hotel.find('div',class_="f63b14ab7a f546354b44 becbee2f63").text.strip()
        ratings if ratings else 'NA'
        score=hotel.find('div',class_="f63b14ab7a dff2e52086").text.strip()
        score if score else 'NA'
        reviews=hotel.find('div',class_="fff1944c52 fb14de7f14 eaa8455879").text.strip().split(' ')[0]
        reviews if reviews else 'NA'
        #getting link

        link=hotel.find('a',href=True).get('href')
        link if link else 'NA'
      
        #saving the file to csv

        writer.writerow([hotel_name,location,price,ratings,score,reviews,link])





     #  print(hotel_name)
      # print(location)
     #  print(price)
      # print(ratings)
     #  print(score)
      # print(reviews)
     #  print(link)
      # print('')

#if using this script directly than below task will be executed

if __name__=='__main__':
  
   web_url=input('Please enter url!:')
   f_name=input('please give file name!:')

   #calling the function

   web_scrapper2(web_url,f_name)

                 



else:
    print(f'Connection failed{response.status_code}')


