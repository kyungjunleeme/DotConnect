import requests
from bs4 import BeautifulSoup

def crawl_nmixx_news():
    query = "엔믹스"
    url = f"https://search.naver.com/search.naver?query={query}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # 최신 뉴스 섹션 크롤링
        news_items = soup.select('.news .news_tit')  # 네이버 뉴스 제목 CSS 셀렉터
        results = []
        for item in news_items:
            title = item.get_text(strip=True)
            link = item['href']
            results.append(f"{title} ({link})")
        # 결과 저장
        with open("nmixx_latest_news.txt", "w") as f:
            f.write("\n".join(results))
        print("Latest NMIXX news saved successfully!")
    else:
        print(f"Failed to fetch news. Status code: {response.status_code}")

if __name__ == "__main__":
    crawl_nmixx_news()
