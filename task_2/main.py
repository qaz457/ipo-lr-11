from bs4 import BeautifulSoup
import requests
import json
try:
    data = []
    url = 'https://news.ycombinator.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    tag_span_titleline = soup.find_all('span', class_='titleline')
    titles = []
    for title in tag_span_titleline:
        titles.append(title.find('a').text)


    comments = []
    subtexts = soup.find_all('td',class_ = 'subtext')
    for i,subtext in enumerate(subtexts,1):
        links = subtext.find_all('a')
        if len(links) >= 3:
            comment_link = links[-1]
            comment_text = comment_link.text
            print(f'{i}. Title: {titles[i-1]}; {comment_text};')
            data.append({
                'rank':i,
                'Title':titles[i-1],
                'Comments':comment_text
                })
        else:
            data.append({
                'rank':i,
                'Title':titles[i-1],
                'Comments':"no comment"
                })
            
    with open('data.json','w', encoding='utf-8') as file:
        json.dump(data,file)

except requests.RequestException as e:
    print(f"Ошибка при запросе к сайту: {e}")
except Exception as e:
    print(f"Общая ошибка: {e}")

    
