def levenshteinDistance(str1, str2):
    """
    Calculates the Levenshtein distance between two strings.

    The Levenshtein distance is a measure of the minimum number of single-character edits 
    (insertions, deletions, or substitutions) required to change one string into the other.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        int: The Levenshtein distance between the two strings.

    Example:
        >>> levenshteinDistance("kitten", "sitting")
        3
    """

    # Initialize a 2D list to store the edit distances
    edits = [[j for j in range(len(str1)+1)] for y in range(len(str2) + 1)]
    for i in range(1, len(str2)+1):
        edits[i][0] = i  # Set the first column values

    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            if str2[i-1] == str1[j-1]:
                # Characters match, no edit needed
                edits[i][j] = edits[i-1][j-1]
            else:
                # Take the minimum of the three possible edits (insert, delete, substitute)
                edits[i][j] = 1 + min(edits[i-1][j-1],
                                      edits[i][j-1], edits[i-1][j])

    return edits[-1][-1]  # Return the final edit distance
