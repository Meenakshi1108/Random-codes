def insert_sorted_subsequence(original_str, indices, sorted_subsequence):
    result_list = list(original_str)

    for i, index in enumerate(indices):
        result_list[index] = sorted_subsequence[i]

    result_str = ''.join(result_list)
    return result_str

def get_sub(s, n):
    if is_lexicographically_sorted(s):
        return 0, []

    indx = []
    res = []

    cr = 0
    while cr < n:
        mx = max(s[cr:])
        lst = cr + s[cr:].index(mx)

        res.append(mx)
        indx.append(lst)
        cr = lst + 1

    return ''.join(res), indx

def min_cyclic_shifts(s):
    n = len(s)
    s += s
    min_lexico = s
    min_shifts = 0

    for i in range(1, n):
        current_shift = s[i:i + n]
        if current_shift < min_lexico:
            min_lexico = current_shift
            min_shifts = i

    return min_shifts

def rec(s, n):
    ans = 0
    while not is_lexicographically_sorted(s):
        res, indx = get_sub(s, n)
        if len(res) == 1 and res[0] == s[n - 1]:
            return -1

        sorted_subsequence = ''.join(sorted(res))
        result = insert_sorted_subsequence(s, indx, sorted_subsequence)
        ans += min_cyclic_shifts(res)
        s = result

    return ans

def is_lexicographically_sorted(s):
    return s == ''.join(sorted(s))

def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        s = input()
        answer = rec(s, n)
        print(answer)

if __name__ == "__main__":
    main()
