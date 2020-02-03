def score_transition_transversion(dna1, dna2, match_score, transition_penalty, transversion_penalty, gap_penatly):
    score = 0
    for i in range(len(dna1)):
        if dna1[i] == dna2[i]:
            score += match_score
        # transition penalties
        if (dna1[i] == "A") and (dna2[i] == "G"):
            score -= transition_penalty
        if (dna1[i] == "G") and (dna2[i] == "A"):
            score -= transition_penalty
        if (dna1[i] == "C") and (dna2[i] == "T"):
            score -= transition_penalty
        if (dna1[i] == "T") and (dna2[i] == "C"):
            score -= transition_penalty
        # transversion penalties
        if (dna1[i] == "C") and (dna2[i] == "A"):
            score -= transversion_penalty
        if (dna1[i] == "A") and (dna2[i] == "C"):
            score -= transversion_penalty
        if (dna1[i] == "G") and (dna2[i] == "T"):
            score -= transversion_penalty
        if (dna1[i] == "T") and (dna2[i] == "G"):
            score -= transversion_penalty
        if (dna1[i] == "G") and (dna2[i] == "C"):
            score -= transversion_penalty
        if (dna1[i] == "C") and (dna2[i] == "G"):
            score -= transversion_penalty
        if (dna1[i] == "A") and (dna2[i] == "T"):
            score -= transversion_penalty
        if (dna1[i] == "T") and (dna2[i] == "A"):
            score -= transversion_penalty

        if dna1[i] == "-" or dna2[i] == "-":
            if not(dna1[i-1] == "-" or dna2[i-1] == "-"):
                score -= gap_penatly

    return score


def main():
    print("Please enter first nucleotide:", end=' ')
    dna1 = input()
    print("Please enter second nucleotide:", end=' ')
    dna2 = input()
    print("Enter match score:", end=' ')
    match_score = int(input())
    print("Enter transition penalty:", end=' ')
    transition_penalty = int(input())
    print("Enter transversion penalty:", end=' ')
    transversion_penalty = int(input())
    print("Enter gap penalty:", end=' ')
    gap_penalty = int(input())
    print(f'{score_transition_transversion(dna1, dna2, match_score, transition_penalty, transversion_penalty, gap_penalty)}')
    return


main()
