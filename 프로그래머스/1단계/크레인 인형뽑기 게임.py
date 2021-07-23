def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] == 0:
                continue
            else:
                basket.append(board[j][i - 1])
                board[j][i - 1] = 0
                break
        if len(basket) >= 2:
            for k in range(1, len(basket)):
                if basket[k] == basket[k - 1]:
                    basket.pop()
                    basket.pop()
                    answer += 2
    return answer
