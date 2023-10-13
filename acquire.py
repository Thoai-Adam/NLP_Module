import requests
from bs4 import BeautifulSoup

def get_blog_articles():
    url = 'https://codeup.edu/blog/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = []
        post_elements = soup.find_all('div', class_='mk-blog-single')
        
        for post in post_elements:
            title = post.find('h1', class_='page-title').text
            content = post.find('div', class_='entry-content').text
            
            article_data = {
                'title': title,
                'content': content
            }
            
            articles.append(article_data)
        
        return articles


if __name__ == '__main__':
blog_articles = get_blog_articles()

# Print the scraped blog articles
for article in blog_articles:
    print(article)
