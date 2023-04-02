from tabulate import tabulate


#UTILITY FUNCTIONS
def issublist(lst1, lst2):
    for val in lst2:
        if val not in lst1:
            return False
    return True

def LShift(lst,n):
        
        nlst = list(lst)
        for i in range(n):
            nlst.append(nlst[0])
            nlst.pop(0)
        #nlst.append(nlst[0])
        return nlst

def fancyPrint(L,r):

    hd = []
    for j in L:
        
        if (j[0:2] not in hd) and (j[1:2] == '#'):
            hd.append(j[0:2])
        elif (j[0] not in hd) and (j[1:2] != '#'):
            hd.append(j[0])

    data = [[],[],[],[]]
    for i in L:
        if ('maj7' in i or 'min7' in i):
            data[1].append(i)
        elif 'sus2' in i:
            data[2].append(i)
        elif 'sus4'in i:
            data[3].append(i)
        else:
            data[0].append(i)

    

    for i in range(1,len(data)):
        
        sublst = data[i]

        a = 0
        while True:

            if a >= (len(hd)-1):
                break

            elm = sublst[a]

            c_root = hd[a][0:2]
            root = elm[0:2]                

            if (root[0] == c_root[0]) and (root[1:2] != '#'):
                a += 1
                continue
            elif (root[0] != c_root[0]):
                sublst.insert(a,None)
                a += 2
            elif (root[0] == c_root[0]) and (root[1:2] != c_root[1:2]):
                sublst.insert(a,None)
                a += 2
            else:
                a += 1

    ft = ['maj/min/dim Chords:','maj7/min7 Chords:','sus2 Chords:','sus4 Chords:']
    for i in range(4):
        data[i].insert(0,ft[i])
    hd.insert(0,'Notes of the Scale: ')


    print(f'\n\tChords present in the {r} scale\n')
    print(tabulate(data,hd,tablefmt='fancy_grid',stralign='center'))


#MUSIC FUNCTIONS
def scale(root,key):
    l = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
        
    n = l.index(root)
    lst = LShift(l,n)
    if key == 'M':
        alg = [0,2,4,5,7,9,11]
    else:
        alg = [0,2,3,5,7,8,10]
    notes = []

    for i in alg:
        notes.append(lst[i])

    return notes

def possibleChords(scl):
    lst = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
 
    def Maj_Min(L):
        return [L[0],L[2],L[4]]

    def dim(L):
        return [L[0],L[3],L[6]]

    def maj7_min7(L):
        return [L[0],L[2],L[4],L[6]]

    def sus2(L):
        return [L[0],L[1],L[4]]

    def sus4(L):
        return [L[0],L[3],L[4]]
    
    chords = []
    for i in scl:
        maj_lst = scale(i,'M')
        min_lst = scale(i,'m')
        l1 = [  (f'{i}',Maj_Min(maj_lst)) , (f'{i}m',Maj_Min(min_lst)),
                (f'{i}maj7', maj7_min7(maj_lst)) , (f'{i}min7', maj7_min7(min_lst)),
                (f'{i}sus2',sus2(maj_lst)), (f'{i}sus4',sus4(maj_lst)) , (f'{i}dim',dim(LShift(lst,n=lst.index(i)))) ]

        for j in l1:
            chrd = j[1]
            if issublist(scl,chrd):
                chords.append(j[0])
    return chords



while True:
    inp = input("\n\nEnter the scale for which you want to find the notes[eg: C or Cm]: ")
    rt = inp[0].upper()

    if inp[-1] == 'm':
        k = 'm'
        ti = rt + ' Minor'
    elif inp[-1] == rt or inp[-1] == 'M':
        k = "M"  
        ti = rt + ' Major'
    

    if rt not in ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']:
        print("\n\tMusical notes only range from A to G.\n ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']\n")
    elif k not in ['M','m']:
            print("\n\tMake sure you enter only 'M' or 'm'\n")
    
    else:
        notes = scale(rt,k)

        lst = possibleChords(notes)

        fancyPrint(lst,ti)
