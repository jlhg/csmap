#!/usr/bin/env python

from random import random

fo_tr = open('tr.txt', 'w')
fo_st = open('tr_stats.txt', 'w')


def avg(f):
    return str(round(sum(f) / len(f), 3))


def tolist(f):
    fiter = iter(f)
    scores = []
    while True:
        try:
            scores.append(str(fiter.next()) + ', ')
            scores.append(str(fiter.next()) + ', ')
            scores.append(str(fiter.next()) + ', ')
            scores.append(str(fiter.next()) + ', ')
            scores.append(str(fiter.next()) + '\n')
        except StopIteration:
            break
    return ''.join(scores)

# Array 1
fo_tr.write('fixedStep chrom=chrTest start=1 step=1\n')
scores_1 = []
for i in range(10):
    s = round(random(), 3)
    scores_1.append(s)
    fo_tr.write('{:.3f}'.format(s))
    fo_tr.write('\n')

# Array 2
fo_tr.write('fixedStep chrom=chrTest start=21 step=1\n')
scores_2 = []
for i in range(10):
    s = round(random(), 3)
    scores_2.append(s)
    fo_tr.write('{:.3f}'.format(s))
    fo_tr.write('\n')

# Array 3
fo_tr.write('fixedStep chrom=chrTest start=41 step=1\n')
scores_3 = []
for i in range(10):
    s = round(random(), 3)
    scores_3.append(s)
    fo_tr.write('{:.3f}'.format(s))
    fo_tr.write('\n')

# Array 4
fo_tr.write('fixedStep chrom=chrTest start=61 step=1\n')
scores_4 = []
for i in range(10):
    s = round(random(), 3)
    scores_4.append(s)
    fo_tr.write('{:.3f}'.format(s))
    fo_tr.write('\n')

# Array 5
fo_tr.write('fixedStep chrom=chrTest start=81 step=1\n')
scores_5 = []
for i in range(10):
    s = round(random(), 3)
    scores_5.append(s)
    fo_tr.write('{:.3f}'.format(s))
    fo_tr.write('\n')

fo_tr.flush()
fo_tr.close()

# Test Requirement 1: Array1: 1-3
trscores = []
for i, s in enumerate(scores_1):
    if 1 <= i + 1 <= 3:
        trscores.append(s)

fo_st.write('# Test Requirement 1: Array1: 1-3\n')
fo_st.write('Avg: ' + avg(trscores) + '\n\n')
fo_st.write(tolist(trscores) + '\n\n')
fo_st.flush()


# Test Requirement 2: Array1: 2-8
trscores = []
for i, s in enumerate(scores_1):
    if 2 <= i + 1 <= 8:
        trscores.append(s)


fo_st.write('# Test Requirement 2: Array1: 2-8\n')
fo_st.write('Avg: ' + avg(trscores) + '\n\n')
fo_st.write(tolist(trscores) + '\n\n')
fo_st.flush()


# Test Requirement 3: Array1: 1-10
trscores = []
for i, s in enumerate(scores_1):
    if 1 <= i + 1 <= 10:
        trscores.append(s)

fo_st.write('# Test Requirement 3: Array1: 1-10\n')
fo_st.write('Avg: ' + avg(trscores) + '\n\n')
fo_st.write(tolist(trscores) + '\n\n')
fo_st.flush()


# Test Requirement 4: Array1: 1-13
trscores = []
for i, s in enumerate(scores_1):
    if 1 <= i + 1 <= 10:
        trscores.append(s)

fo_st.write('# Test Requirement 4: Array1: 1-13\n')
fo_st.write('Avg: ' + avg(trscores) + '\n\n')
fo_st.write(tolist(trscores) + '\n\n')
fo_st.flush()


# Test Requirement 5: Array1: 2-13
trscores = []
for i, s in enumerate(scores_1):
    if 2 <= i + 1 <= 10:
        trscores.append(s)

fo_st.write('# Test Requirement 5: Array1: 2-13\n')
fo_st.write('Avg: ' + avg(trscores) + '\n\n')
fo_st.write(tolist(trscores) + '\n\n')
fo_st.flush()


# Test Requirement 6: Array2: 19-30 (all)
trscores = []
for i, s in enumerate(scores_2):
    if 1 <= i + 1 <= 10:
        trscores.append(s)

fo_st.write('Test Requirement 6: Array2: 19-30 (all)\n')
fo_st.write('Avg: ' + avg(trscores) + '\n\n')
fo_st.write(tolist(trscores) + '\n\n')
fo_st.flush()


# Test Requirement 7: Array2: 19-35 (all)
trscores = []
for i, s in enumerate(scores_2):
    if 1 <= i + 1 <= 10:
        trscores.append(s)

fo_st.write('# Test Requirement 7: Array2: 19-35 (all)\n')
fo_st.write('Avg: ' + avg(trscores) + '\n\n')
fo_st.write(tolist(trscores) + '\n\n')
fo_st.flush()


# Test Requirement 8: Array2: 18- (all), Array3: 41-45
trscores = []
for i, s in enumerate(scores_2):
    trscores.append(s)

for i, s in enumerate(scores_3):
    if 1 <= i + 1 <= 5:
        trscores.append(s)

fo_st.write('# Test Requirement 8: Array2: 18- (all), Array3: 41-45\n')
fo_st.write('Avg: ' + avg(trscores) + '\n\n')
fo_st.write(tolist(trscores) + '\n\n')
fo_st.flush()


# Test Requirement 9: Array2: 21- (all), Array3: -50 (all)
trscores = []
for i, s in enumerate(scores_2):
    trscores.append(s)

for i, s in enumerate(scores_3):
    trscores.append(s)

fo_st.write('# Test Requirement 9: Array2: 21- (all), Array3: -50 (all)\n')
fo_st.write('Avg: ' + avg(trscores) + '\n\n')
fo_st.write(tolist(trscores) + '\n\n')
fo_st.flush()


# Test Requirement 10: Array2: 24- , Array3: -45 (all)
trscores = []
for i, s in enumerate(scores_2):
    if 4 <= i + 1 <= 10:
        trscores.append(s)

for i, s in enumerate(scores_3):
    if 1 <= i + 1 <= 5:
        trscores.append(s)

fo_st.write('# Test Requirement 10: Array2: 24- , Array3: -45 (all)\n')
fo_st.write('Avg: ' + avg(trscores) + '\n\n')
fo_st.write(tolist(trscores) + '\n\n')
fo_st.flush()

# Test Requirement 11: Array2: 24- , Array3: -50 (all)
trscores = []
for i, s in enumerate(scores_2):
    if 4 <= i + 1 <= 10:
        trscores.append(s)

for i, s in enumerate(scores_3):
    if 1 <= i + 1 <= 10:
        trscores.append(s)

fo_st.write('# Test Requirement 11: Array2: 24- , Array3: -50 (all)\n')
fo_st.write('Avg: ' + avg(trscores) + '\n\n')
fo_st.write(tolist(trscores) + '\n\n')
fo_st.flush()


# Test Requirement 12: Array2: 24- , Array3: -55 (all)
trscores = []
for i, s in enumerate(scores_2):
    if 4 <= i + 1 <= 10:
        trscores.append(s)

for i, s in enumerate(scores_3):
    if 1 <= i + 1 <= 10:
        trscores.append(s)

fo_st.write('# Test Requirement 12: Array2: 24- , Array3: -55 (all)')
fo_st.write('Avg: ' + avg(trscores) + '\n\n')
fo_st.write(tolist(trscores) + '\n\n')
fo_st.flush()


# Test Requirement 13: Array2: 25- , Array3: all, Array4: -66
trscores = []
for i, s in enumerate(scores_2):
    if 5 <= i + 1 <= 10:
        trscores.append(s)

for i, s in enumerate(scores_3):
    if 1 <= i + 1 <= 10:
        trscores.append(s)

for i, s in enumerate(scores_4):
    if 1 <= i + 1 <= 6:
        trscores.append(s)


fo_st.write('# Test Requirement 13: Array2: 25- , Array3: all, Array4: -66\n')
fo_st.write('Avg: ' + avg(trscores) + '\n\n')
fo_st.write(tolist(trscores) + '\n\n')
fo_st.flush()


# Test Requirement 14: Array2: 18- (all) , Array3: all, Array4: -75 (all)
trscores = []
for i, s in enumerate(scores_2):
    if 1 <= i + 1 <= 10:
        trscores.append(s)

for i, s in enumerate(scores_3):
    if 1 <= i + 1 <= 10:
        trscores.append(s)

for i, s in enumerate(scores_4):
    if 1 <= i + 1 <= 10:
        trscores.append(s)

fo_st.write('# Test Requirement 14: Array2: 18- (all) , Array3: all, Array4: -75 (all)\n')
fo_st.write('Avg: ' + avg(trscores) + '\n\n')
fo_st.write(tolist(trscores) + '\n\n')
fo_st.flush()
