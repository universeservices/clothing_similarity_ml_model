  import requests
  from bs4 import BeautifulSoup
  import csv

  def scrape_clothing_data(url):
      response = requests.get(url)
      soup = BeautifulSoup(response.content, 'html.parser')
      
      items = soup.find_all('div', {'class': 'sg-col-inner'})
      
      data = []
      for item in items[:1000]:  
          url = item.find('a')['href']
          description = item.find('p', {'class': 'description'}).text.strip()
          label = item.find('span', {'class': 'label'}).text.strip()
          
          data.append((url, description, label))
      
      return data

  def store_data(data, filename):
      with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
          writer = csv.writer(csvfile)
          writer.writerow(['URL', 'Description', 'Label'])
          writer.writerows(data)

  # Usage example:
  url = 'https://www.amazon.com/s?k=women+black+dress'
  data = scrape_clothing_data(url)
  store_data(data, 'clothing_data.csv')

