import http
from html.parser import HTMLParser
import urllib.request as ur
from bs4 import BeautifulSoup
from bs4 import Comment

page="https://newsapi.org/v2/everything?sources=focus&apiKey=API_KEY"
output_file="test1.html"
s = ur.urlopen( page )
print( s.read() )


if( s.status == http.HTTPStatus.OK ):
    print( "Let's go!" )
    sl = s.read()
    soup = BeautifulSoup(sl.decode("utf-8"), 'lxml')
    #list_div = soup.find_all("div", attrs={"class": "teaserInfo"})
    comments = soup.find_all(string=lambda text:isinstance(text,Comment))
    print( "#comments: " + str( len( comments ) ) )
    for c in comments:
        #print( c )
        soup_comment = BeautifulSoup( c, 'lxml' )
        list_articles=soup_comment.find_all("div", class_="teaserInfo")
        print( "#articles:" + str ( len( list_articles ) ) )
        for h in list_articles:
            #soup_comment.select( h )
            #print( h.next_element )
            index=soup_comment.find( h )
            print( index )
            

    with open(output_file, "w") as file:
        file.write(str(soup))

#urls = ur.urlretrieve(page, output_file)
#print(type(urls))
#print(urls[1])
