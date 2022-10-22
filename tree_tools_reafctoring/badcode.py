import sys, os, argparse

parser = argparse.ArgumentParser(description='tree')
parser.add_argument('path',type=str,)
parser.add_argument('-fo','--folders_only',action='store_true',)
parser.add_argument('-i','--include',type=str,action='store',)
parser.add_argument('-e','--exclude',type=str,action='store',)
parser.add_argument('-a','--all',action='store_true',)
parser.add_argument('-f','--full_name',action='store_true',)
args = parser.parse_args()
print(sys.argv[1])
if args.include:
    itext = args.include
if args.exclude:
    etext = args.exclude
def divine_crutch(path, n):
    dir = os.listdir(path)
    for i in range(len(dir)):
        if os.path.isfile(path + '\\' + dir[i]):
            if not(args.folders_only):
                if not(args.include and itext not in dir[i]):
                    if not(args.exclude and etext in dir[i]):
                        if not(not(args.all) and dir[i][0] == '.') and not(args.full_name):
                            print(n*' ', dir[i])
                        elif args.full_name and not(not(args.all) and dir[i][0] == '.'):
                            print(n*' ' ,path + '\\' + dir[i])
        if os.path.isdir(path + '\\' + dir[i]):
            if not(not(args.all) and dir[i][0] == '.') and not(args.full_name):
                print(n*' ', dir[i])
            elif args.full_name and not(not(args.all) and dir[i][0] == '.'):
                print(n*' ' ,path + '\\' + dir[i])
            n += 4
            divine_crutch(path + '\\' + dir[i], n)
            n -= 4
divine_crutch(sys.argv[1], 4)
