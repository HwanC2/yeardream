# prac4.py

def read_file():
    '''
    file_name을 입력받고, file_name에 해당하는 파일이 있다면, 해당 파일에 이름을 출력하는 코드를 작성하여라.
    단, 만약 파일이 존재하지 않는 경우에는 해당 에러를 예외처리하는 코드를 작성하여라.
    '''

    # 검색할 파일 이름 입력받기
    file_name = input("검색할 파일 이름을 입력하세요. : ")

    try:
        # 목록에서 입력한 파일명을 가진 파일 찾기
        with open(file_name) as f :
            # 파일을 찾았을 때
            print(f"검색한 파일 '{file_name}'을(를) 찾았습니다.")

    # 파일을 찾지 못한 에러 예외처리
    except FileNotFoundError:
        # 오류 문구 출력
        print("파일이 존재하지 않습니다.")

if __name__ == "__main__":
    read_file()
