def distance_full(word1: str, word2: str):
    """computes the minimum number (true Damerau-Levenshtein distance) of single-character 
    operations to transform source word to and target word

    Args:
        word1 (str): source word
        word2 (str): target word

    Returns:
        int: distance (differences) between two comparred words
    """
    m = len(word1)
    n = len(word2)

    maxdist = m + n

    matrix = []
    for i in range(m+2):
        matrix.append([0]*(n+2))

    matrix[0][0] = maxdist

    for i in range(m+1):
        matrix[i+1][0] = maxdist
        matrix[i+1][1] = i

    for j in range(n+1):
        matrix[0][j+1] = maxdist
        matrix[1][j+1] = j

    da = {}

    for i in range(1, m+1):
        db = 0
        for j in range(1, n+1):
            if word2[j-1] in da:
                i1 = da[word2[j-1]]
            else:
                i1 = 0
            j1 = db

            if word1[i-1] == word2[j-1]:
                cost = 0
                db = j
            else:
                cost = 1

            matrix[i+1][j+1] = min(
                matrix[i+1][j] + 1, #insertion
                matrix[i][j+1] + 1, #deletion
                matrix[i][j] + cost, #substitution
                matrix[i1][j1]+(i - i1 - 1) + 1 + (j - j1 - 1)) #transposition

        da[word1[i-1]] = i

    return matrix[m+1][n+1]
