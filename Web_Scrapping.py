import requests
from bs4 import BeautifulSoup
import pandas as pd

review_List = []

def get_soup(url):
    r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 2})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_reviews(soup):
    reviews = soup.find_all('div', {'data-hook': 'review'})
    try:
        for item in reviews:
            rating = item.find('i', {'data-hook': 'review-star-rating'})
            body = item.find('span', {'data-hook': 'review-body'})
            
            review = {}
            
            if rating is not None:
                review['review_rating'] = float(rating.text.replace('out of 5 stars', '').strip())
            
            if body is not None:
                review['review_body'] = body.text.strip()
            
            review_List.append(review)
    except:
        pass

for x in range(1, 20):
    soup = get_soup(f'https://www.amazon.in/Intel%C2%AE-CoreTM-i5-10400-Processor-Cache/dp/B086MN38Q2/ref=sr_1_12?crid=3ANCB5MJRPI19&dib=eyJ2IjoiMSJ9.I6wpvJtrwcthmEqKOurPEgLyCxA0elnvg0b3RWx8ZWDrOxZLdWKTaImyaKWyNsjDIAGFNz_be5K6QQG4T3ubOlN9Kcm_GZRuHfialSlboMsFUhJsbt1USnTsVyfIZqoiDdCkn7Lw6Z8Ut043nhaeLfCCxtjLW1yCt44IUqq7QRI1Ta1KKeis4wIZdEAJ0GJy8mMrzb-kdT7VtcppoMH9m20IUPA5Ljghle5q1iPwWLg.dOBJDJL5FQsgBwfccGDV60iYuP4QUXLCcvxVaQR56SY&dib_tag=se&keywords=intel+i5+processor&qid=1720694197&sprefix=intel+i5+processor%2Caps%2C337&sr=8-12')
    print(f'Getting page: {x}')
    get_reviews(soup)
    print(len(review_List))
    if not soup.find('li', {'class': 'a-disabled a-last'}):
        pass
    else:
        break

df = pd.DataFrame(review_List)
df.to_excel('a6408-reviews.xlsx', index=False)
print('Finish')
