
def bubble(s):
        sorted = False

        while not sorted:
            sorted = True
            for i in range(0, len(s) - 1):
                if s[i] > s[i + 1]:
                    sorted = False
                    s[i], s[i + 1] = s[i + 1], s[i]


        return s

print(bubble([16, 8, 47, 2, 63]))
