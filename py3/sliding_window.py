def sliding_window(dna1, dna2, window_size, mismatch_limit):
    graph = [["_" for x in range(len(dna1) + 1)] for y in range(len(dna2) + 1)]
    graph[0][0] = "#"
    for y in range(len(dna2)):
        graph[y + 1][0] = dna2[y]

    for x in range(len(dna1)):
        graph[0][x + 1] = dna1[x]

    for y in range(len(dna2)):
        for x in range(len(dna1)):
            graph[y+1][x+1] = " "

    for y in range(len(dna2)-(window_size-1)):
        for x in range(len(dna1)-(window_size-1)):
            mismatch_count = 0
            for i in range(window_size):
                if dna1[x+i] != dna2[y+i]:
                    mismatch_count += 1

            if mismatch_count <= mismatch_limit:
                graph[y+1][x+1] = "*"
    return graph


def main():
    print("Enter first nucleotide:", end=" ")
    dna1 = input()
    print("Enter second nucleotide:", end=" ")
    dna2 = input()
    print("Enter window size:", end=" ")
    window_size = int(input())
    print("Enter mismatch limit:", end=" ")
    mismatch_limit = int(input())

    graph = sliding_window(dna1, dna2, window_size, mismatch_limit)
    for y in range(len(graph)):
        for x in range(len(graph[0])):
            print(graph[y][x], end=' | ')
        print()

    return


main()
