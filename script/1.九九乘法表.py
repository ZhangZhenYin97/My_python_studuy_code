'''
1x1=1
1x2=2 2x2=4
1x3=3 2x3=6 3x3=9
1x4=4 2x4=8 3x4=12 4x4=16
'''

for line in range(1, 10):
    for raw in range(1,line + 1):
        print(raw, 'x', line, '=', line * raw,end=' ')
    print()

