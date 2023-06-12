def count_args(*args):
    print(args)
    return (len(args))

print(count_args([], (''), 'a', 12, False))

count_args()