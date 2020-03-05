def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        pass
    else:
        raise ValueError("Bro, They're different")
     
    score = 0
    for char in range(0, len(strand_a)):
        score = score if strand_a[char] == strand_b[char] else score + 1

    return score
