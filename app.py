from func import create-task


def menu():
    while True:
        op = int(input("1. crear"))
        if op == 1:
            i = str(input("escriba descripcion"))
            create_task(i)
