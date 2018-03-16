def series(n):
    pi=0
    for i in range(n):
        pi+=(4*((-1)**(i+1)))/(2*(i+1)-1)

    return pi


print(series(1000000000))
input()
