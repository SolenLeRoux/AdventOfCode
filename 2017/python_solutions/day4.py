import sys
sys.dont_write_bytecode = True


def is_valid(p):
    """
    Asserts there is no duplicate in the passphrase
    complexity: O(n^2) with n the number of words
    """
    words = p.split('\t' if '\t' in p else ' ')
    return [w for w in words if words.count(w) > 1] == []

def solve_1(x):
    """
    Returns the number of rows where a string doesn't appear twice
    complexity: O(n^2 * p) with p the number of rows and n the number of string by row
    """
    return len([p for p in x.split('\n') if is_valid(p)])

def is_anagram(a, b):
    """
    Determines if a is an anagram of b or not
    complexity: O(l2) with l the number of letter by word
    """
    if len(a) != len(b):
        return False
    for l in a:
        if a.count(l) != b.count(l):
            return False
    return True

def is_valid_2(p):
    """
    Asserts there is no anagram in the passphrase
    complexity: O(n^2 * l^2) with n the number of words and l the number of letters
    """
    words = p.split('\t' if '\t' in p else ' ')
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if is_anagram(words[i], words[j]):
                return False
    return True

def solve_2(x):
    """
    Returns the number of valid passphrases, i.e. passphrases without anagrams
    complexity: O(p * n^2 * l^2) with
    p the number of pasphrases
    n the number of word by passphrase
    l the number of letter by word
    """
    return len([p for p in x.split('\n') if is_valid_2(p)])
