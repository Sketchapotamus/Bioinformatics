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
                palindromes.append((dna[x:x+6], x))

    return palindromes


def main():
    cont = True
    print(input())
    while cont:
        print("Functions:\n"
              "* 1 - Reverse Compliment\n"
              "* 2 - Reverse Palindrome\n"
              "* 3 - Quit\n"
              "Please enter request:", end=' ')
        request = input()
        if request == "1":
            print("Please enter the nucleotide sequence:", end=' ')
            print(reverse_compliment(input()))
        if request == "3":
            cont = False

    return


main()
