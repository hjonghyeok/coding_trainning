def solution(A, B):
    s = A
    for i in range(len(A)):
        if s == B:
            return i
        s =  s[-1] + s[:-1]
    
    return -1

print(solution("hello", "ohell"))
print(solution("apple", "elppa"))
print(solution("atat", "tata"))
print(solution("abc", "abc"))