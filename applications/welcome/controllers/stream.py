import sys; 
sys.path.append('/usr/local/lib/python2.7/dist-packages')
sys.path.append('/usr/lib/python2.7/dist-packages')
from pattern.web import Twitter


def index():

    response.flash = T("Feedsdf s!")
    response.flash2 = T('Twitter Feed Area')

    text = request.vars.search_text
    
    get_data = search(text)

    list_text = []
   
    words = text.split()

    for word in words:
            list_text.append(word)

    length = len(get_data)

    response.view = 'default/detail-one.html'
    return dict(message=get_data, lengthofdata=length, words=list_text)


def search(text):
	list = []
 

	twitter = Twitter(language='en') 
	for tweet in twitter.search(text, count=30, cached=False):
            list.append(tweet.text)

                
	return list

def count():
    counter = counter + 1


# def parse(text):
  
#     s = parsetree(text) 
#     for sentence in s: 
#             for chunk in sentence.chunks:
#                 for word in chunk.words:
#                     s.append(word)
  

#     return s

