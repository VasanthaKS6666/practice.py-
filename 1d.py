words = ["listen", "silent", "enlist", "google", "gogole", "cat"]
anagrams = {}

for word in words:
    key = "".join(sorted(word))
    anagrams.setdefault(key, []).append(word)

print([group for group in anagrams.values() if len(group) > 1])
# Output: [['listen', 'silent', 'enlist'], ['google', 'gogole']]
