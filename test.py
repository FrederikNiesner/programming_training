s1, s2 = "adc", "dcda"



def checkInclusion(s1, s2):

    import collections
    ctr1 = collections.defaultdict(int)
    ctr2 = collections.defaultdict(int)
    for x in s1:
        ctr1[x] += 1
    for x in s2[:len(s1)]:  # set initial dict of same length s1
        ctr2[x] += 1

    i = 0; j = len(s1)  # window: j - i

    while j < len(s2):  # loop until end of window j = end of string s2

        if ctr2 == ctr1:
            return True

        ctr2[s2[i]] -= 1
        if ctr2[s2[i]] < 1:
            ctr2.pop(s2[i])
        ctr2[s2[j]] = ctr2.get(s2[j], 0) + 1
        i += 1; j += 1

    return ctr2 == ctr1


checkInclusion(s1, s2)
