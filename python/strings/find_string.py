def count_substring(s, ss):
    count = 0
    for i in range(len(s)):
        count += s.count(ss, i, i + len(ss))
    return count
