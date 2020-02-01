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

def reverse_palindromes(dna):
    palindromes = []
    if len(dna) >= 6:
        for x in range(len(dna)-5):
            if dna[x:x+6] == reverse_compliment(dna[x:x+6]):
                palindromes.append(dna[x:x+6])
            print(dna[x:x+6])

    return palindromes


print(reverse_compliment('AAGTGCG'))
print(reverse_palindromes('AAGTGCTCG'))
