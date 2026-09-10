def distance(word1: str, word2: str):
    """computes the minimum number (OSA distance) of single-character operations
    to transform source word to and target word

    Args:
        word1 (str): source word
        word2 (str): target word

    Returns:
        int: distance (differences) between two comparred words
    """
    m = len(word1)
    n = len(word2)

    matrix = []
    for i in range(m+1):
        matrix.append([0]*(n+1))

    for i in range(m+1):
        matrix[i][0] = i

    for j in range(n+1):
        matrix[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):

            if word1[i-1] == word2[j-1]:
                cost = 0
            else:
                cost = 1

            matrix[i][j] = min(
                matrix[i][j-1] + 1, #insertion
                matrix[i-1][j] + 1, #deletion
                matrix[i-1][j-1] + cost) #substitution

            if (i > 1
                and j > 1
                and word1[i-1] == word2[j-2]
                and word1[i-2] == word2[j-1]):
                matrix[i][j] = min(
                    matrix[i][j],
                    matrix[i-2][j-2] + 1) #transposition

    return matrix[m][n]
