## ls.py

import os

# 파일 또는 폴더 여부를 구분하는 메서드
def list_directory_contents() :
    file_list = []
    dir_list = []

    # 현재 디렉토리에 있는 모든 파일과 폴더 목록을 가져온다.
    entries = os.listdir()

    # 목록 길이 만큼 반복
    for entry in entries :
        # 파일인지 체크
        if os.path.isfile(entry) :
            file_list.append(entry)
            
        # 폴더인지 체크
        if os.path.isdir(entry) :
            dir_list.append(entry)
    
    # 리스트 정렬
    file_list = sorted(file_list)
    dir_list = sorted(dir_list)

    # 목록 출력
    list_print('File', file_list)
    list_print('Directory', dir_list)


# 리스트 출력
def list_print(category:str, L:list) :
    # 리스트 길이 만큼 반복
    for l in L :
        # 카테고리(파일/폴더)
        print(f"{category} : {l}")


if __name__ == "__main__" :
    # 메서드를 실행하여 파일과 폴더 목록을 출력
    list_directory_contents()