def reverse_compliment(dna):
    compliment = ""
    for c in dna:
        if c == 'T':
            compliment += "A"
        if c == 'A':
            compliment += "T"
        if c == "G":
            compliment += "C"
        if c == "C":
            compliment += "G"
    return compliment[::-1]

print(reverse_compliment('AAGTGCG'))
