from collections import deque

def solution(s):
    answer = []
    for string in s:
        stack = []
        count = 0
        for s in string:
            if s == '0'
                if stack[-2:] == ['1','1'] :
                    count += 1
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(s)
            else:
                stack.append(s)

        if count == 0:
            answer.append(string)
        else:
            final = deque()

            while stack:
                if stack[-1] == '1':
                    final.append(stack.pop())
                    elif stack[-1] == '0':
                        break

            while count > 0:
                final.appendleft('0')
                final.appendleft('1')
                final.appendleft('1')
                count -= 1

            while stack:
                final.appendleft(stack.pop())
            answer.append(''.join(final))

        return answer
