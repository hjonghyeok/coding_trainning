def solution(keyinput, board):
    x_max, x_min = board[0]//2, -(board[0]//2)
    y_max, y_min = board[1]//2, -(board[1]//2)
    x_pos, y_pos = 0, 0
    for i in keyinput:
        if i == "up" and y_pos + 1 <= y_max:
            y_pos += 1
        elif i == "down" and y_pos - 1 >= y_min:
            y_pos -= 1
        elif i == "left" and x_pos - 1 >= x_min:
            x_pos -= 1
        elif i == "right" and x_pos + 1 <= x_max:
            x_pos += 1
        
    return x_pos, y_pos

print(solution(["left", "right", "up", "right", "right"], [11, 11]))
print(solution(["down", "down", "down", "down", "down"], [7, 9]))