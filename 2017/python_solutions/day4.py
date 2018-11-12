import sys
sys.dont_write_bytecode = True


def is_valid(p):
    # assert there is no duplicate in the passphrase
    # complexity: O(n2) with n the number of words
    words = p.split('\t' if '\t' in p else ' ')
    return [w for w in words if words.count(w) > 1] == []

def solve_1(x):
    # complexity: O(n2 * p) with p the number of passphrases
    # and n the number of word by passphrase
    return len([p for p in x.split('\n') if is_valid(p)])

def is_anagram(a, b):
    # complexity: O(l2) with l the number of letter by word
    if len(a) != len(b):
        return False
    for l in a:
        if a.count(l) != b.count(l):
            return False
    return True

def is_valid_2(p):
    # assert there is no anagram in the passphrase
    # complexity: O(n2 * l2) with n the number of word
    # and l the number of letter by word
    words = p.split('\t' if '\t' in p else ' ')
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if is_anagram(words[i], words[j]):
                return False
    return True

def solve_2(x):
    # complexity: O(p * n2 * l2) with
    # p the number of pasphrases
    # n the number of word by passphrase
    # l the number of letter by word
    return len([p for p in x.split('\n') if is_valid_2(p)])
