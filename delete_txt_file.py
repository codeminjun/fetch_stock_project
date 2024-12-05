import os

def delete_file(ticker):
    """
    지정된 종목 티커에 따른 EPS/PE Ratio 결과 파일을 삭제합니다.
    """
    # 파일 이름 생성
    output_file = f"{ticker}_per_eps.txt"
    
    try:
        # 파일 존재 여부 확인 후 삭제
        if os.path.exists(output_file):
            os.remove(output_file)
            print(f"{output_file} 파일이 성공적으로 삭제되었습니다.")
        else:
            print(f"{output_file} 파일이 존재하지 않습니다.")
    except Exception as e:
        print(f"파일 삭제 중 오류가 발생했습니다: {e}")

# 사용 예시
if __name__ == "__main__":
    ticker = input("삭제할 종목 티커를 입력하세요 (예: TSLA): ").strip()
    delete_file(ticker)