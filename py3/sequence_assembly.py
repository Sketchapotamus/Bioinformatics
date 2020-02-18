

def get_fragments():
    fragments = []
    while True:
        print(f"Enter fragment {len(fragments) + 1} or enter \"end\":", end=' ')
        frag = input()
        if frag.upper() == "END":
            break

        fragments.append(frag)
    return fragments


def main():

    fragments = get_fragments()
    print(fragments)

    return


main()


