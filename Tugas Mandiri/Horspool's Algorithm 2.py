def preprocess(pattern):
    """
    Fungsi untuk menghasilkan bad character shift table.
    """
    table = {}
    for i in range(len(pattern) - 1):
        table[pattern[i]] = len(pattern) - 1 - i
    return table

def horspool(text, pattern):
    """
    Horspool's algorithm untuk string searching.
    """
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1  # pola lebih panjang dari teks, tidak ada kecocokan

    table = preprocess(pattern)
    i = m - 1
    while i < n:
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
        if k == m:
            return i - m + 1  # Terdapat kecocokan
        else:
            i += table.get(text[i], m)  
    return -1  # tidak ada kecocokan

text = "the quick brown fox jumps over the lazy dog"
pattern = "fox"
print("Pola ditemukan pada index:", horspool(text, pattern))
