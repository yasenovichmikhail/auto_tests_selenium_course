def greet(name, *args):
    folk = ' and '.join((name,) + args)
    return f"Hello, {folk}!"

print(greet('Roma'))


# Hello, Timur and Roman and Ruslan!