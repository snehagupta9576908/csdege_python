import pandas as pd
import requests
from bs4 import BeautifulSoup


Product_name=[]
Prices=[]
Description=[]
Reviews=[]

for i in range(2,12):
    url="https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&as-pos=1&as-type=HISTORY&page="+str(i)

    r= requests.get(url)
   # print(r)

    soup=BeautifulSoup(r.text,'html.parser')
    boxes=soup.find_all("div",class_="DOjaWF gdgoEp")

    

    for box in boxes:
        name=box.find("div",class_="KzDlHZ")
        prices= box.find("div",class_="Nx9bqj _4b5DiR")
        desc = box.find("ul",class_="G4BRas")
        reviews =box.find("div",class_="_5OesEi")

        Product_name.append(name.text if name else "No name")
        Prices.append(prices.text if prices else "No price")
        Description.append(desc.text if desc else "No description")
        Reviews.append(reviews.text if reviews else "No reviews")


df=pd.DataFrame({"Product Name ":Product_name,"Prices":Prices,"Description":Description,"Reviews":Reviews})
print(df)
df.to_csv("flipkart_mobiles_under_50000.csv",index=False)
