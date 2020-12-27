def mutiple():
    lst = []
    for i in range(1000):
        if i%3 == 0 or i%5 == 0 :
            lst.append(i)
    print(sum(lst))

if __name__ == '__main__':
    mutiple()