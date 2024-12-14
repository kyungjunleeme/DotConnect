import requests
from bs4 import BeautifulSoup

def crawl_nmixx_news():
    query = "엔믹스"
    url = f"https://search.naver.com/search.naver?query={query}"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # HTTP 요청 에러 처리
        soup = BeautifulSoup(response.text, 'html.parser')

        # 네이버 뉴스 섹션 크롤링
        news_items = soup.select('.news_tit')  # 최신 구조 반영: 뉴스 제목과 링크가 포함된 클래스

        if not news_items:
            print("No news items found. Check your CSS selector or page structure.")
            print(response.text[:1000])  # HTML 일부 출력
            return

        results = []
        for item in news_items:
            title = item.get_text(strip=True)  # 뉴스 제목
            link = item['href']  # 뉴스 링크
            results.append(f"{title} ({link})")

        # 결과 저장
        with open("nmixx_latest_news.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(results))
        print(f"Latest NMIXX news saved successfully to nmixx_latest_news.txt!")

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching news: {e}")

if __name__ == "__main__":
    crawl_nmixx_news()
