import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from IPython.display import clear_output

def GetWebInsight(soup, class_name):
    x = soup.find('div', class_=class_name) # here we check what is a name of the offer and copy the link of the soup and append these data into two columns (data_a, data_b)
    if x is not None:
        y = x.get_text(strip=True)
    else:
        y = 'no data'
    return y
def download_page_insight(web_page, counter):
    url_site = requests.get(web_page)
    soup = BeautifulSoup(url_site.text, 'html.parser')
    localisation_name = GetWebInsight(soup, 'offer-user__address')
    price_value = GetWebInsight(soup, 'pricelabel')
    additional_a = ['Cena', 'Miejsce', 'Link']
    additional_b = [price_value, localisation_name, web_sites[counter]]  
    data_a = []
    data_b = []
                
    table = soup.find('div', {'class': 'clr descriptioncontent marginbott20'})
    for th in table.find_all('span', {'class' : 'offer-details__name'}):
        data_a.append(th.get_text(strip=True))
    for a in additional_a:
        data_a.append(a)
    
    table = soup.find('div', {'class': 'clr descriptioncontent marginbott20'})
    for strong in table.find_all('strong', {'class' : 'offer-details__value'}):
        data_b.append(strong.get_text(strip=True))
    for b in additional_b:
        data_b.append(b)
    return data_a, data_b
    
olx_table_cols = {'Cena': [], 'Cena za m²': [], 'Czynsz (dodatkowo)': [], 'Finanse': [], 'Liczba pokoi': [], 'Link': [], 'Miejsce': [],
                  'Oferta od': [], 'Powierzchnia': [], 'Poziom': [], 'Rodzaj zabudowy': [], 'Rynek': [], 'Umeblowane': [], 'Miasto': []}
final_olx_table = pd.DataFrame(data=olx_table_cols)

list_of_cities = ['wodzislaw-slaski','zory','rybnik','chorzow','tychy','myslowice','mikolow','tarnowskie-gory','gliwice','zabrze','ruda-slaska','knurow','swietochlowice','bytom','katowice']
for chosen_city in list_of_cities:    
    print('\n Scraping data from: ' + chosen_city + '\n')
    url = requests.get('https://www.olx.pl/nieruchomosci/mieszkania/' + chosen_city + '/') # get the data
    soup = BeautifulSoup(url.text, 'html.parser') # load data into bs4
    div = soup.find('div', {'class': 'pager rel clr'}) # Checking amount of web pages with the offers for a chosen city 
    pages_list = []
    for a in div.find_all('a'):
        xx = a.get_text(strip=True)
        pages_list.append(xx)
    page_highest_number = max([s for s in pages_list if s.isdigit()])
        
    web_sites = [] # Write down each of the link from all of the web pages. To not overload the site I put 2 seconds pause for each site
    for web_page in range(1, int(page_highest_number)+1): # open each of the page with offers
        url = requests.get('https://www.olx.pl/nieruchomosci/mieszkania/' + chosen_city + '/?page=' + str(web_page))
        soup = BeautifulSoup(url.text, 'html.parser')
        div = soup.find('div', { 'class': 'rel listHandler' })
        time.sleep(10)
        for a in div.find_all('a', href=True): # copy every link from the chosen page
            web_sites.append(a['href'])
                
    web_sites = list(dict.fromkeys(web_sites)) # removing duplicates
    web_sites = [x for x in web_sites if 'https://www.olx.pl/oferta/' in x] # leave just offerts from olx
    to_remove = [';promoted'] # we do not want any link contains this string (duplication)
    web_sites = [el for el in web_sites if not any(ignore in el for ignore in to_remove)]
    
    a = {'data': [], 'info': [], 'lp': []} # Here we run all the url's and check the offers. To not overload the site I put 3 seconds pause for each link
    olx_table = pd.DataFrame(data=a) # Create a DataFrame for collected data
    offer_no = len(web_sites)
    for offer in range(0, offer_no):
        clear_output(wait=True)
        print("Processing: {:.0%}".format(((offer + 1) / offer_no)))
        url_address = web_sites[offer] 
        # web_soup_count = w
        time.sleep(10)
        value1, value2 = download_page_insight(url_address, offer) # run the function from the top of this script
        
        aa = {'data': value1, 'info': value2, 'lp': offer + 1}
        df = pd.DataFrame(data=aa)
        olx_table = olx_table.append(df)
    olx_table = olx_table.pivot(index='lp', columns='data')['info']
    olx_table['Miasto'] = chosen_city
    final_olx_table = final_olx_table.append(olx_table)
final_olx_table.to_csv('OLX_Table.csv', index=False)