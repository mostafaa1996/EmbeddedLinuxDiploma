from bs4 import BeautifulSoup as BS 
import requests
import pandas

YallaKora_url = "https://www.yallakora.com/match-center/?date="
date = input("Please enter the date in the following format (MM/DD/YYYY) :")
urlWithdate = YallaKora_url + date
page = requests.get(urlWithdate)
Matches = []
def main(page):
    Content = page.content
    soup = BS(Content , "lxml")
    championships = soup.find_all("div" , {'class' : 'matchCard'})
    
    def get_match_info(championship):
        championship_title = championship.find("div" , {'class' : 'title'}).find("h2").text.strip()
        Team1_group_html  = championship.find("div" , {'class' : 'ul'}).find_all("div",{'class' : 'teamA'})
        Team1_list = []

        for team in Team1_group_html:
          Team1_group_p = team.find("p")
          if Team1_group_p :
             Team1_list.append(Team1_group_p.text)

        #print(Team1_list)

        Team2_group_html  = championship.find("div" , {'class' : 'ul'}).find_all("div",{'class' : 'teamB'})
        Team2_list = []

        for team in Team2_group_html:
          Team2_group_p = team.find("p")
          if Team2_group_p :
             Team2_list.append(Team2_group_p.text)
        
        # print(Team2_list)  

        Results = championship.find("div" , {'class' : 'ul'}).find_all("div",{'class' : 'MResult'})
        # print(Results)
        Data_Results_list = []
        for Result in Results :
          result_of_teams = Result.find_all("span" , {'class':'score'})
          Match_time = Result.find("span" , {'class':'time'}).text
          Result_team1 = result_of_teams[0].text
          Result_team2 = result_of_teams[1].text 
          Data_Results_list.append((Result_team1 , Result_team2 , Match_time))
        # print(Data_Results_list)
        Match_details = {}
        for i in range(0,len(Team1_list),1) :
           Match_details["Team1"] = Team1_list[i]
           Match_details["Team2"] = Team2_list[i]
           Match_details["Team1Result"] = Data_Results_list[i][0]
           Match_details["Team2Result"] = Data_Results_list[i][1]
           Match_details["Date"] = Data_Results_list[i][2]
           Match_details["ChampionTitle"] = championship_title
           Matches.append(Match_details.copy()) #To solve the issue of shallow copying that occurred when I removed the copy keyword, I need to make a deep copy.

    get_match_info(championships[0])
    print(Matches)


main(page)
data = pandas.DataFrame(Matches)
data.to_excel("./Python/Web_scraping/Matches_DataBase.xlsx" , index=False)
