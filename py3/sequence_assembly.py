

def get_fragments():
    fragments = []
    while True:
        print(f"Enter fragment {len(fragments) + 1} or enter \"end\":", end=' ')
        frag = input()
        if frag.upper() == "END":
            break

        fragments.append(frag)
    return fragments


def find_overlap(frag1, frag2):
    if len(frag1) > len(frag2):
        smaller_len = len(frag2)
    else:
        smaller_len = len(frag1)
    best_overlap = 0
    for x in range(1, smaller_len):
        if frag1[-x:] == frag2[0:x]:
            best_overlap = x
    return best_overlap


def sequence_assembly(fragments):
    #  overlap length, prefix index, postfix index
    while not (len(fragments) == 1):
        best_overlap = (0, 0, 0)
        for x in range(len(fragments)):
            for y in range(len(fragments)):
                if x == y:
                    continue
                overlap = find_overlap(fragments[x], fragments[y])
                if overlap > best_overlap[0]:
                    best_overlap = (overlap, x, y)
        new_fragment = fragments[best_overlap[1]][0:best_overlap[0]] + fragments[best_overlap[2]]
        fragments.pop(best_overlap[1])
        fragments.pop(best_overlap[2])
        fragments.append(new_fragment)

    return fragments[0]


def main():

    fragments = get_fragments()
    assembled_sequence = sequence_assembly(fragments)
    print(assembled_sequence)
    return


main()
# ATCCGC
# CGCGTAA
# CGTTACT
# GCGATC
# TAACG

