#보드
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
def display_board():
    print(board[0]+ "|" + board[1]+ "|" + board[2])
    print(board[3]+ "|" + board[4]+ "|" + board[5])
    print(board[6]+ "|" + board[7]+ "|" + board[8])
#보드판
def play_game():
    #첫 보드 보여주기 
    display_board()

#차례 바꾸기
def handle_turn():
        position = input("1-9중에 표시할 자리를 입력하세요 : ")
        position = int(position) - 1
        #index가 0부터 시작하므로 1빼주기
        
        board[position] = "X"
        display_board()
    play_game()

#게임 시작
#이겼는지 체크
    #가로 체크
    #세로 체크
    #대각선 체크
#비겼는지 체크
#플레이어 바꾸기