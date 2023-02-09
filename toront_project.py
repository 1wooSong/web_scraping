import requests
from bs4 import BeautifulSoup
import html.parser
from lxml import etree
#토론토 날씨정보 
#headline news
#it 정보

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def scrape_weather():
    print("Today weather in Toronto")
    url="https://www.google.com/search?q=toronto+weather&rlz=1C1CHBF_enCA960CA961&oq=toronto+wea&aqs=chrome.0.0i512l2j69i57j0i512l7.1590j1j7&sourceid=chrome&ie=UTF-8"
    soup=create_soup(url)
    #현재 날씨
    curr_temp=soup.find("span",attrs={"class":"wob_t q8U8x"}).get_text().strip()
    print(curr_temp,"°C")
    #비 예상
    forcast_rain=soup.find("span",attrs={"id":"wob_pp"}).get_text()
    print("the percentege of rain or snow :",forcast_rain)
    weather_forcast = soup.find("span",attrs={"id":"wob_dc"}).get_text()
    print(weather_forcast)


def scrape_news():
    print("Today news in Toronto")
    url ="https://toronto.ctvnews.ca/more/local-news"
    soup=create_soup(url)
    #현재 탑 5 뉴스 / 제목/ 링 크
    title= soup.findAll("h2",attrs={"class":"teaserTitle"})
    for i in range(5):
        print(i,title[i].get_text().strip())
        link = title[i].a["href"]
        #print(link)
        print("https://toronto.ctvnews.ca{0}".format(link))

def team_name():
    url ="https://www.premierleague.com/tables"
    soup = create_soup(url)
    teams=soup.findAll("span",attrs={"class":"long"})
    print("This is premier league table")
    for i in range(20):
        print(i+1,teams[i].get_text())
    print("Please type number and teamname with lowercase without space")
    print("for example: 12 crystalpalace")
    team_number,input_teamname=input().split()
    team_number=int(team_number)
    input_teamname=input_teamname.lower()
    #여기까지 순위대로 뽑았음   
    before_url = "https://www.premierleague.com/clubs"
    endpoint = teams[team_number-1].get_text().lower().replace(" ", "-") + "-overview"
    if input_teamname=="arsenal":
        middle_url="/1/"
    elif input_teamname=="manchestercity":
        middle_url="/11/"
    elif input_teamname=="newcastleunited":
        middle_url="/23/"
    elif input_teamname=="manchesterunited":
        middle_url="/12/"
    elif input_teamname=="tottenhamhotspur":
        middle_url="/21/" 
    elif input_teamname=="brightonandhovealbion":
        middle_url="/131/"
    elif input_teamname=="fulham":
        middle_url="/34/"
    elif input_teamname=="brentford":
        middle_url="/130/"
    elif input_teamname=="liverpool":
        middle_url="/10/"
    elif input_teamname=="Chelsea":
        middle_url="/4/"   
    elif input_teamname=="astonvilla":
        middle_url="/2/"   
    elif input_teamname=="crystalpalace":
        middle_url="/6/"   
    elif input_teamname=="nottinghamforest":
        middle_url="/15/"   
    elif input_teamname=="leicestercity":
        middle_url="/26/"   
    elif input_teamname=="leedsunited":
        middle_url="/9/"   
    elif input_teamname=="westhamunited":
        middle_url="/25/"   
    elif input_teamname=="wolverhamptonwanderers":
        middle_url="/38/"   
    elif input_teamname=="bournemouth":
        middle_url="/127/"   
    elif input_teamname=="everton":
        middle_url="/7/"   
    elif input_teamname=="southampton":
        middle_url="/20/"   
    else:
        print("wrong number and name try again please")   
    url = before_url + middle_url + endpoint
    soup=create_soup(url)
    print("if u want to check overview here : ",url)

    # 받는값에 따라 다른 url 생성 성공 
    #schedule=soup.find("div",attrs={"class","fixturesAbridged matchListContainer"})
    # match_time=soup.find("div",attrs={"class","imspo_mt__ndl-p imspo_mt__pm-inf imspo_mt__pm-infc imso-medium-font"}).get_text()
    # teams = soup.find_all("div",attrs={"class","liveresults-sports-immersive__hide-element"})
    # home_team=teams[0].get_text()
    # away_team=teams[1].get_text()
    #print(schedule.get_text().strip())

if __name__ == "__main__": 
    scrape_weather()
    scrape_news()
    team_name()
