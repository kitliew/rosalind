string_a = "ACGTGCGT"
string_b = "GCGTATGC"
dic_a = dict(enumerate(string_a, start=1))
dic_b = dict(enumerate(string_b, start=1))

def match_score(x,y):
    if x == 0 or y == 0:
        return 0
    i = dic_a[x]
    j = dic_b[y]
    if i == j:
        return 5
    else:
        return -3

#drawing matrix
n = len(string_a) + 1
a = [[0] * n for i in range(n)]
for i in range(n):              #each row
    for j in range(n):          #each column
        if i-1 < 0 or j-1 < 0:
            a[i][j] = 0
        else:
            a[i][j] = max(0,                                #no negative value
                        match_score(j,i) + a[i-1][j-1],     #diagonal
                        a[i][j-1] - 4,                      #above gap penalty = -4
                        a[i-1][j] - 4)                      #left side gap penalty = -4

for row in a:
    print(' '.join([str(elem) for elem in row]))
