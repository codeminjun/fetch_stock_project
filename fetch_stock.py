import yfinance as yf
import requests
from bs4 import BeautifulSoup

def fetch_per_eps(ticker):
    """
    주어진 종목 티커에서 EPS와 PE Ratio 데이터를 가져와 텍스트 파일에 저장합니다.
    """
    try:
        # EPS 데이터 가져오기 (Yahoo Finance API)
        stock = yf.Ticker(ticker)
        info = stock.info
        eps = info.get("trailingEps", None)
        if eps is None:
            raise ValueError("EPS 데이터를 가져올 수 없습니다.")

        # Yahoo Finance에서 PE Ratio 가져오기
        url = f"https://finance.yahoo.com/quote/{ticker}"
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            raise ConnectionError("Yahoo Finance 페이지에 접근할 수 없습니다.")
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # PE Ratio 데이터 추출 (data-field="trailingPE" 속성 사용)
        pe_ratio_element = soup.find("fin-streamer", {"data-field": "trailingPE"})
        if pe_ratio_element is None or not pe_ratio_element.text.strip():
            raise ValueError("PE Ratio 데이터를 가져올 수 없습니다.")
        
        # PE Ratio 값 변환
        try:
            pe_ratio = float(pe_ratio_element.text.replace(",", ""))
        except ValueError:
            raise ValueError("PE Ratio 값을 숫자로 변환할 수 없습니다.")

        # 결과 저장
        output_file = f"{ticker}_per_eps.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"종목명: {ticker}\n")
            f.write(f"EPS: ${eps:.2f}\n")
            f.write(f"PE Ratio: {pe_ratio:.2f}\n")

        print(f"EPS와 PE Ratio 값이 {output_file} 파일에 저장되었습니다.")

    except Exception as e:
        print(f"오류 발생: {e}")

# 사용 예시
if __name__ == "__main__":
    ticker = input("종목 티커를 입력하세요 (예: TSLA): ").strip()
    fetch_per_eps(ticker)