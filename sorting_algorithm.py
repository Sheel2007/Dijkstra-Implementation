
def bubble(s):
        indexing_length = len(s) - 1
        sorted = False

        while not sorted:
            sorted = True
            for i in range(0, indexing_length):
                if s[i] > s[i + 1]:
                    sorted = False
                    s[i], s[i + 1] = s[i + 1], s[i]


        return s

print(bubble([16, 8, 47, 2, 63]))
