'''
즐겨찾기 기능 패키지
'''

from typing import List


favorites = []

def bookmark(bookmark : List):

    finish = False
    while not finish:

        select = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")
        
        if select == '?':
            print(" '목록' 입력시 현재 즐겨찾기 목록을 볼 수 있습니다.")
            print(" '추가' 입력시 즐겨찾기를 목록에 추가할 수 있습니다.")
            print(" '삭제' 입력시 즐겨찾기의 항목을 삭제할 수 있습니다.")
            print(" '종료' 입력시 프로그램을 종료할 수 있습니다.")

        elif select == '목록':
            showFavorites(bookmark)

        elif select == '추가':
            addFavorite(bookmark)

        elif select == '삭제':
            removeFavorite(bookmark)

        elif select == "종료":
            print("즐겨찾기를 종료합니다.")
            finish = True
        
        else:
            print("잘못 입력하셨습니다. 다시 입력해주세요.")

def showFavorites(bookmark: List):
    if not bookmark:
        print("현재 즐겨찾기 목록이 비어있습니다.")
    else:
        print("즐겨찾기 목록:")
        for i, favorite in enumerate(bookmark, 1):
            print(f"{i}. {favorite}")

def addFavorite(bookmark: List):
    """
    사용자에게 즐겨찾기 목록으로 추가할 파일의 경로를 받아 목록 안에 동일 파일 경로가 있는지를 확인한다
    없다면 즐겨찾기 목록에 새 항목으로 추가한다
    """
    path = input("즐겨찾기에 추가할 파일 경로를 입력하세요: ")
    if path in bookmark:
        print("이미 즐겨찾기에 추가된 파일입니다.")
    else:
        bookmark.append(path)
        print("즐겨찾기에 추가되었습니다.")

def removeFavorite(bookmark: List):
    """
    즐겨찾기 목록에 파일이 존재한다면 파일 번호를 포함한 즐겨찾기 목록을 출력
    제거할 파일의 번호를 입력받은 후, 해당 파일을 제거
    """

    if not bookmark:
        print("현재 즐겨찾기 목록이 비어있습니다.")
    else:
        print("즐겨찾기 목록:")
        for i, favorite in enumerate(bookmark, 1):
            print(f"{i}. {favorite}")

        index = int(input("제거할 파일의 번호를 입력하세요: "))
        if 1 <= index <= len(bookmark):
            removed_favorite = bookmark.pop(index - 1)
            print(f"{removed_favorite} 가 즐겨찾기에서 제거되었습니다.")
        else:
            print("해당 번호의 파일이 존재하지 않습니다. 제거할 파일의 번호를 다시 입력해주세요.")