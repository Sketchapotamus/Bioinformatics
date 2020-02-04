def sliding_window(dna1, dna2, window_size, mismatch_limit):
    graph = [[0 for x in range(len(dna1))] for y in range(len(dna2))]
    for y in range(len(dna2)-window_size):
        for x in range(len(dna1)-window_size):
            mismatch_count = 0
            for i in range(window_size):
                if(dna1[x+i]!=dna2[y+i]):
                    mismatch_count+=1
            
            #if mismatch_count <= mismatch_limit:
    

    return

            

def graph_test(dna1, dna2):
    graph = [["_" for x in range(len(dna1)+1)] for y in range(len(dna2)+1)]
    graph[0][0] = "#"
    for y in range(len(dna2)):
        for x in range(len(dna1)):
            if y==0:
                graph[y][x+1] = dna1[x]
            elif x==0:
                graph[y][x] = dna2[y]
            else:
                graph[y][x] = " "

    return graph


def main():
    graph = graph_test("GCGGTCCC", "CCGGCT")
    #graph = [[x+y for x in range(6)] for y in range(4)]
    for y in range(len(graph)):
        for x in range(len(graph[0])):
            print(graph[y][x], end=' ')
        print()
    
    return

main()



