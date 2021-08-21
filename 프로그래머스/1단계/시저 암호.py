def solution(s, n):
    answer = ''
    arr = list(s)
    for i in arr:
        if i.isupper():
            answer += chr(ord(i) + n) if ord(i) + \
                n < 91 else chr(ord(i) - 26 + n)
        elif i.islower():
            answer += chr(ord(i) + n) if ord(i) + \
                n < 123 else chr(ord(i) - 26 + n)
        elif i == ' ':
            answer += i
    return answer
