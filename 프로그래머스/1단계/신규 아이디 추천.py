def solution(new_id):
    answer = ''
    special = '~!@#$%^&*()=+[{]}:?,<>/'
    special = list(special)
    new_id = new_id.lower()
    a = list(new_id)
    result = []
    for i in a:
        if i not in special:
            result.append(i)
    result = ''.join(result)
    while '..' in result:
        result = result.replace('..', '.')
    result = list(result)
    if result:
        if result[0] == '.':
            del result[0]
    if result:
        if result[-1] == '.':
            result.pop()

    if not result:
        result.append('a')

    if len(result) > 15:
        for i in range(len(result) - 15):
            result.pop()

    if result[-1] == '.':
        result.pop()

    if len(result) < 3:
        for i in range(3 - len(result)):
            result.append(result[-1])

    answer = ''.join(result)
    return answer
