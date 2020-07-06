# Silesian Real Estate Market - Analysis
> Currently, I live in Wodzisław Śląski, but I am curious which city is more beneficial to live from financial perspective, if I will start working in Katowice. 

## Objectives:
There is one main objective I had, described above split on 3 parts:
* build a tool for scraping in Beautiful Soup library
* clean and transform gained data
* analyse real estate market and find the best city to life from my subjective perspective
* create a prediction model which helps you to see what might be a price in a chosen city once you write down arguments in the model

## Description:
1. I have built a [tool](https://raw.githubusercontent.com/mborycki/Silesian_Real_Estate_Market/master/Real_Estate_Market_Scraper.py) which is able to scrap required outputs for 15 chosen cities you can see in the below map and save all of them in a dataframe.
The map with all cities I was interested in:
![](/images/map.png)

2. Next, I have translated and cleaned the dataframe looks like this:

![](/images/first_df.png)

...into this one:

![](/images/clean_df.png)

3. In the dataframe we had both For Sale and For Rent offers. So, I have created 2 separate tables as we needed to analyse them individually. 

4. I was interested in just with flats, as I did not look for houses or apartments. I have checked what is the ratio in both tables of different type of properties:

* For Rent:

![](/images/building_type_rent.png)

* For Sale:

![](/images/building_type_sale.png)

5. After all of the cleaning and transforming parts, we were able to see an average price per square meters for both tables.

* For Rent:

![](/images/avg_sqm_prc_rent.png)

* For Sale:

![](/images/avg_sqm_prc_sale.png)

6. The last thing I wanted to do is finally to see where is the best place for me to buy or/and rent a flat.

* For Rent:

![](/images/profitability_rent.png)
>For rent properties we could see really interesting thing. If we want to rent a flat, then the best we can do is to find it somewhere close to our workplace. There is no significant in price difference between the cities. The most expensive option is to stay in Wodzisław Śląski as traveling costs will be enormous. Theoretically Mysłowice and Chorzów are the cheapest cities to rent a flat, but I would choose Katowice because there is no need to travel.

* For Sale:

![](/images/profitability_sale.png)
>You can see here that flats in Katowice are the most expensive. Although, we do not need to travel to work (by car), I do not see any financial reasons to buy a flat there. However, there is realy good options close to Katowice such as Bytom, Chorzów, Ruda Śląska, Świętochłowice or Tarnowskie Góry. I would choose Chorzów because the smallest distance to Katowice.

---
7. PowerBI report - ***UNDER DEVELOPMENT***

8. Prediction Model - ***UNDER DEVELOPMENT***

## Libraries:
* Beautiful Soup ([documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/))
* Pandas ([documentation](https://pandas.pydata.org/pandas-docs/version/0.25/))
* NumPy ([documentation](https://numpy.org/doc/1.19/))
* Folium ([documentation](https://python-visualization.github.io/folium/))
* Matplotlib ([documentation](https://matplotlib.org/3.2.2/contents.html))

## More details:
1. Platform where the data come from:
* The [OLX marketplace](https://www.olx.pl/)
> It is a platform for buying and selling services and goods such as electronics, fashion items, furniture, household goods, real estates, cars and bikes

2. Scraped Date: 
* 2020-05-07

3. Cities taken into consideration:
* Wodzisław Śląski, Żory, Rybnik, Chorzów, Tychy, Mysłowice, Mikołów, Tarnowskie Góry, Gliwice, Zabrze, Ruda Śląska, Knurów, Świętochłowice, Bytom, Katowice

4. Please find the analysis and more details / explanation in the source file: [jupyter notebook](https://github.com/mborycki/Silesian_Real_Estate_Market/blob/master/Real_Estate_Market_Analyzing.ipynb)
