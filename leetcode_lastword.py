# find the length of the last word
def lengthOfLastWord(s):
  return len(s.split()[-1])

print(lengthOfLastWord("  fly me  to   the moon  "))
