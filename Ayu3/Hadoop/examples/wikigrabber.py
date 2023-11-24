import wikipediaapi
import random

def download_random_documents():
    wiki_wiki = wikipediaapi.Wikipedia(user_agent='Hadoop familiarization project (vichogk@gmail.com)', language='en')
    annos = list(range(1900, 2024))
    muestra = random.sample(annos, 30)

    for it, item in enumerate(muestra):

        random_title = get_random_title(item)
        page_py = wiki_wiki.page(random_title)
        print(f"Title: {page_py.title}")
        print(f"URL: https://en.wikipedia.org/wiki/{page_py.title}") 
        print(f"Content: {page_py.text}")
        with open(f'./input{it%2}/{it}.txt', 'w') as f:
            f.write(page_py.text)

def get_random_title(item):
    random_title = wikipediaapi.Wikipedia(user_agent='Hadoop familiarization project (vichogk@gmail.com)', language='en').page(title=str(item)).title
    print(random_title)
    return random_title


download_random_documents()