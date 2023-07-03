x = 'cate Frog cat FROGs bee CATERS mouse cATwalk dolphin mOus Cats CatAlo'
x = x.split()

print(*sorted(input().split(), key=lambda x: x.lower()))