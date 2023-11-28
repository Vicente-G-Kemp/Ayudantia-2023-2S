import wikipediaapi
import random

def download_random_documents():
    wiki_wiki = wikipediaapi.Wikipedia(user_agent='Hadoop familiarization project (vichogk@gmail.com)', language='en')
    annos = list(range(1900, 2024))
    muestra = random.sample(annos, 30)
    for it, item in enumerate(muestra):
        page_py = wiki_wiki.page(title=str(item))
        print(f"Title: {page_py.title}")
        print(f"URL: https://en.wikipedia.org/wiki/%7Bpage_py.title%7D") 
        print(f"Content: {page_py.text}")
        with open(f'./input{it%2}/{it}.txt', 'w') as f:
            f.write(str(page_py.title)+"<splittername>")
            f.write((page_py.text).replace("\n", " "))

download_random_documents()
