def areAnagrams(self, s1, s2):
    """
    Function to check if two strings are anagrams of each other using frequency counts.

    Approach:
    - Use a fixed-size frequency list (size 26, for lowercase English alphabets) to count character occurrences.
    - Increment the count for characters in s1 and decrement for characters in s2.
    - Check if all frequency counts are zero to confirm an anagram.

    Time Complexity: O(n)
        - Single iteration through the strings to update the frequency list.
        - Final pass through the frequency list is O(26), effectively constant.
    Space Complexity: O(1)
        - Uses a fixed-size list for frequency counts (constant space).

    Parameters:
    - s1 (str): First string
    - s2 (str): Second string

    Returns:
    - bool: True if s1 and s2 are anagrams, False otherwise.
    """
    if len(s1) != len(s2):
        return False  # Return 'false' if lengths differ

    # Initialize frequency list for 26 letters
    freq = [0] * 26

    # Update frequency list
    for i in range(len(s1)):
        freq[ord(s1[i]) - ord('a')] += 1
        freq[ord(s2[i]) - ord('a')] -= 1

    # Check if all frequencies are zero
    for count in freq:
        if count != 0:
            return False

    return True
