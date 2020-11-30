def vectornoe(a, b):
    if(a[0] * b[1] - a[1] * b[0] > 0):
        return 1
    elif(a[0] * b[1] - a[1] * b[0] == 0):
        return 0
    else:
        return -1

def scalarnoe(a, b):
    p = a[0] * b[0] + a[1] * b[1]
    return p