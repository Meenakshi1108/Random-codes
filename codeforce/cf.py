# t = int(input())

# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     arr.sort()
#     ans = []
#     d = 0

#     for i in range(1, n):
#         d += (arr[i] - arr[i - 1])
#         ans.append(arr[i - 1])
#         d += (arr[i + n] - arr[i + n - 1])
#         ans.append(arr[i + n - 1])

#     ans.append(arr[n - 1])
#     ans.append(arr[2 * n - 1])

#     print(d)
#     for i in range(0, len(ans), 2):
#         print(ans[i], ans[i + 1])


n = int(input())
s = list(map(str, input().split()))
le = []
lo = []
cnt = 0

for i in range(n):
    if len(s[i]) % 2 == 0:
        le.append(s[i])
    else:
        lo.append(s[i])

# odd+odd=even, even+odd=odd, even+even=even

for i in range(len(le)):
    for j in range(len(le)):
        if(i==j):
        	cnt+=1
        else:
        	combined = le[i] + le[j]
        	half_length = len(combined) // 2
	        first_half = sum(int(char) for char in combined[:half_length])
	        second_half = sum(int(char) for char in combined[half_length:])
	        if first_half == second_half:
	            cnt += 1

for i in range(len(lo)):
    for j in range(len(lo)):
        if(i==j):
        	cnt+=1
        else:
        	combined = lo[i] + lo[j]
        	half_length = len(combined) // 2
	        first_half = sum(int(char) for char in combined[:half_length])
	        second_half = sum(int(char) for char in combined[half_length:])
	        if first_half == second_half:
	            cnt += 1

print(cnt)


# def solve(n, a):
#     def construct_b(index, b_values):
#         if index == n:
#             return b_values

#         for i in range(n):
#             if not used[i]:
#                 if index == 0 or (b_values[index - 1] ^ i) == a[index - 1]:
#                     used[i] = True
#                     b_values[index] = i
#                     result = construct_b(index + 1, b_values)
#                     if result is not None:
#                         return result
#                     used[i] = False

#     used = [False] * n
#     b = [0] * n

#     result = construct_b(0, b)
#     return result

# n = int(input())
# a = list(map(int, input().split()))

# b = solve(n, a)
# print(*b)