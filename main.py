
import requests
from requests_html import HTML
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
url = 'https://www.marketwatch.com/story/based-on-19-bear-markets-in-the-last-140-years-heres-where-the-current-downturn-may-end-says-bank-of-america-11651847842'


def save_html_to_file(url, filename):
    re = requests.get(url)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(re.text, )
    return filename

# save_html(url, 'article.html')

# All text content are in the "#js-article__body" class
def retrieve_text(from_file, to_file):
    
    with open(from_file, 'r', encoding='utf-8') as f:
        html_file = f.read()
        
        # use requests_html -> HTML to parse and retrieve the content
        html_parsed = HTML(html=html_file)
        article_body = html_parsed.find('#js-article__body', first=True)

        # All text are inside "p" tags
        paragraphs = article_body.find('p') 
        text = ''
        for p in paragraphs:
            text = text +"\n" + p.text

        # save the text to a file for further analysis
        with open(to_file, 'w', encoding='utf-8') as f:
            f.write(text)
    return text

# text = retrieve_text(save_html_to_file(url, 'article.html'), 'text.txt')

with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()
# list top 10 frequent words in the article
def get_most_frequent_words(text, num_of_words):

    # get all words in a list in lower case
    words = text.split() 
    lower_words = [w.lower() for w in words if w.isalpha()] 

    # get stop words set from NLTK so that those can be removed from the 'lower_words' list
    stops = set(stopwords.words('english'))
    word_dict = {}
    for w in lower_words:
        if w not in stops:
            word_dict[w] = word_dict.get(w, 0) +1  # see NOTE1 below

    words_list = list()
    for k,v in word_dict.items():
        # create a tuple with k,v position reversed, save to the words_list
        words_list.append((v, k))

    # sort the list. 
    sorted_words = sorted(words_list, reverse=True)[:num_of_words] # see NOTE2 below
    
    print(sorted_words) 
    return sorted_words

get_most_frequent_words(text, 10)
# [(8, 'market'), (8, 'bear'), (4, 'nasdaq'), (3, 'strategists'), (3, 'recent'), (3, 'investors'), (3, 'hartnett'), (3, 'billion'), (3, 'average'), (2, 'year')]



