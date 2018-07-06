import http
from html.parser import HTMLParser
import urllib.request as ur
from bs4 import BeautifulSoup
from bs4 import Comment

page="https://www.focus.de/schlagzeilen/"
output_file="test1.html"
output_file1="test2.html"
#s = ur.urlopen("http://www.focus.de")
#sl = s.read()
#print(sl)

s = ur.urlopen( page )
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
            #print( type( h ) )
            #print ( h )
            #print( "#elements: " + str( len( h.next_elements ) ) )
            print ( "next elements")
            for x in h.next_elements:
                print ( "_____________" )
                print( x )
            print( "End" )
            #exit()
            #t = soup_comment.find( h )
            #print(t)
            #print( t )
            #index=soup_comment.find( h )
            #print( index )
            

    with open(output_file, "w") as file:
        file.write(str(soup))

    with open(output_file1, "w") as file:
        file.write(str(comments))

#urls = ur.urlretrieve(page, output_file)
#print(type(urls))
#print(urls[1])
