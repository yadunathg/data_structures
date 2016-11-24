# python2

def read_input():
    return (raw_input().rstrip(), raw_input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # return [
    #     i
    #     for i in range(len(text) - len(pattern) + 1)
    #     if text[i:i + len(pattern)] == pattern
    # ]
    p = 500000003
    x = 31
    result = []

    p_hash = poly_hash(pattern, p, x)
    hash_list = precompute_hashes(text, len(pattern), p, x)
    for i in range(len(text)-len(pattern)+1):
        if hash_list[i] == p_hash and pattern == text[i:i+len(pattern)]:
            result.append(i)
    return result

def poly_hash(pattern, p, x):
    h = 0
    for c in pattern[::-1]:
        h = (h * x + ord(c)) % p
    return h

def precompute_hashes(text, n, p, x):
    hash_list = [None] * (len(text) - n + 1)
    hash_list[len(text) - n] = poly_hash(text[-n:], p, x)

    y = 1
    for i in range(n):
        y = (y * x) % p

    for i in range(len(text) - n - 1, -1, -1):
        hash_list[i] = (hash_list[i+1] * x + ord(text[i]) - y * ord(text[i+n]) + p) % p
    return hash_list

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

