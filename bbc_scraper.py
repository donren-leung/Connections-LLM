import requests
import json, time
from bs4 import BeautifulSoup

BASE_URL = "https://ocdb.cc/episodes/"

def get_episode_links():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    episode_links = [a['href'] for a in soup.find_all('a', href=True) if "/episode/" in a['href']]
    return episode_links

def parse_episode(episode_url):
    response = requests.get(episode_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    walls_data = {}
    
    for wall_id in ['wall_1', 'wall_2']:
        wall = soup.find('div', id=wall_id)
        wall_data = {}
        
        for i in range(1, 5):  # For 4 groups
            clues = []
            for j in range(1, 5):
                clues.append(wall.find('div', class_=f'group{i}-clue{j}').get_text(strip=True))
            answer = wall.find('div', class_=f'group{i}-answer').find('div', class_='back').get_text(strip=True)
            wall_data[answer] = clues
        
        walls_data[wall_id] = wall_data
    
    return walls_data

def main():
    episode_links = get_episode_links()
    print(episode_links, len(episode_links))
    all_data = {}
    
    for link in episode_links:
        episode_data = parse_episode(link)
        print(episode_data)
        all_data[link] = episode_data
        # break
        time.sleep(3)

    # Write to a JSON file
    with open('only_connect_data.json', 'w+') as json_file:
        json.dump(all_data, json_file, indent=4)

if __name__ == "__main__":
    data = main()
