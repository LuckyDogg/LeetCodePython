def lefttop():
    for i in range(1,10):
        for j in range(i,10):
            print('%d*%d=%2d'%(i, j, i*j), end=" ")
        print("")


def righttop():
    for i in range(1,10):
        for j in range(1, i+1):
            print(end="       ")
        for j in range(i, 10):
            print('%d*%d=%2d'%(i, j, i*j), end=" ")
        print("")


def leftbottom():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%d*%d=%2d'%(i, j, i*j), end=" ")
        print("")

def rightbottom():
    for i in range(1,10):
        for j in range(i, 10):
            print(end="       ")
        for j in range(1, i+1):
            print('%d*%d=%2d'%(i, j, i*j), end=" ")
        print("")

if __name__=='__main__':
    rightbottom()