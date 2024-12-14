import requests
from bs4 import BeautifulSoup
import os

def crawl_nmixx_news():
    query = "엔믹스"
    url = f"https://search.naver.com/search.naver?query={query}"
    
    try:
        # 네이버는 User-Agent 설정 필요
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
            )
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # HTTP 에러 발생 시 예외를 던짐

        soup = BeautifulSoup(response.text, 'html.parser')
        # 네이버 뉴스 영역의 CSS 셀렉터
        news_items = soup.select('.news .news_tit')  

        if not news_items:
            print("No news items found. Check your CSS selector or page structure.")
            return

        results = []
        for item in news_items:
            title = item.get_text(strip=True)
            link = item['href']
            results.append(f"{title} ({link})")

        # 결과 저장
        result_file = "nmixx_latest_news.txt"
        with open(result_file, "w") as f:
            f.write("\n".join(results))
        print(f"Latest NMIXX news saved successfully to {result_file}!")

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching news: {e}")

if __name__ == "__main__":
    crawl_nmixx_news()
