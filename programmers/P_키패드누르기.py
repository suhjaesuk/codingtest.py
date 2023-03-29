def solution(numbers, hand):

    answer = ''
    left_x, left_y = (3,0)
    right_x, right_y = (3,2)

    table = {1: (0,0), 2: (0,1), 3: (0,2),
             4: (1,0), 5: (1,1), 6: (1,2),
             7: (2,0), 8: (2,1), 9:(2,2),
             0: (3,1)}

    for i in numbers:
        if i in[1,4,7]:
            answer += "L"
            left_x,left_y = table[i]
        elif i in [3,6,9]:
            answer += "R"
            right_x,right_y=table[i]

        #중앙에 있는 버튼일 경우 3가지로 조건으로 나뉜다.
        else:
            current_x,current_y=table[i]
            left = abs(current_x - left_x) + abs(current_y - left_y)
            right = abs(current_x - right_x) + abs(current_y - right_y)

            # 1.오른쪽의 거리가 더 가까울 경우
            if left> right:
                answer += "R"
                right_x, right_y = current_x, current_y

            # 2.왼족의 거리가 더 가까울 경우
            elif left<right:
                answer += "L"
                left_x, left_y = current_x, current_y

            # 3.거리가 같을 경우
            else:
                if hand == "right":
                    answer += "R"
                    right_x, right_y = current_x, current_y
                else:
                    answer += "L"
                    left_x,left_y = current_x, current_y

    return answer