import connect
import argparser
import requests
from bs4 import BeautifulSoup
import pandas

parser=argparser.ArgumentParser()
parser.add_argument("---page_num_max", help="Enter the number of pages to parse:", type=int)
args=parser.parse_args()
go_url="https://www.goibibo.com/hotels/find-hotels-in-Mumbai/4213513766539949483/4213513766539949483/%7B%22ci%22:%2220220504%22,%22co%22:%2220220505%22,%22r%22:%221-2-0%22%7D/?{%22filter%22:{}}&sec=dom&cc=IN"
page_num_MAX=args.page_num_max
scraped_info_list=[]

for page_num in range(1,page_num_MAX):
    req=requets.get(go_url+str[page_num])
    content=req.content
    
    soup=BeautifulSoup(content, "html.parser")
    
    all_hotels=soup.find_all("div", {"class":"HotelCardstyles"})
    
    for hotels in all_hotels:
        hotel_dict={}
        hotel_dict{"name"}=hotel.find("h4",{"class":"dwebCommonstyles"})
        hotel_dict{"address"}=hotel.find("span",{"class":"HotelCardstyles"})
        hotel_dict{"price"}=hotel.find("div",{"class":"HotelCardstyles"})
        try:
            hotel_dict{"rating"}=hotel.find("div",{"class":"ReviewAndRatingsstyles"})
        except AttributeError:
            pass
        parent_amenities_elements=hotel.find("span",{"class":"PersuasionHoverTextstyles"})
        amenities_list=[]
        for amenity in parent_amenities_elements.find_all("span",{"class":"PersuasionHoverTextstyles"}):
            amenities_list.append(amenity.find_all("span",{"class":"PersuasionHoverTextstyles").text.strip())
            
        hotel_dict["amenities"]=', '.join(amenities_list[-1])
        
        scraped_info_list.append(hotel_dict)
        connect.insert_into_table(args.dbname, tuple(hotel_dict.values()))
dataFrame=pandas.DataFrame(scraped_info_list)
dataFrame.to_csv("Go.csv")


#=====connect.py=======
import sqlite3

def create_table(db_name):
    conn=sqlite3.connect("captain.db")

    conn.execute("CREATE TABLE IF NOT EXISTS GO_HOTELS(NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, RATING TEXT)")

    print("TABLE CREATED SUCESSFULLY")
    
    conn.close()
    
def insert_table(db_name):
    conn=sqlite3.connect("captain.db")

    conn.execute("INSERT INTO GO_HOTELS(NAME , ADDRESS, PRICE, AMENITIES, RATING ) VALUES (GO_HOTEL, HHOTEL STREET, 500, FREE WIFI,4.5)")
    conn.commit()
    conn.close()

def get_info(db_name):
    conn=sqlite3.connect("captain.db")
    cur=conn.cursor()

    cur.execute("SELECT * FROM GO_HOTELS")

    table_data=cur.fetchall()

    for record in table_data:
       print(record)
       
    conn.close()
