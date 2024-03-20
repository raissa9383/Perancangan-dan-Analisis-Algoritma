def horspool(pola, teks):
    m = len(pola)
    n = len(teks)
    if m > n:
        return -1

    # inisialisasi tabel skip dengan nilai default (m)
    skip = [m] * 256

    # hitung nilai skip sebenarnya untuk karakter pada pola
    for k in range(m - 1):
        skip[ord(pola[k])] = m - k - 1

    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and teks[i] == pola[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i + 1
        k += skip[ord(teks[k])]

    return -1

print("Pola ditemukan pada index:", horspool('def', 'abcdefabc'))
