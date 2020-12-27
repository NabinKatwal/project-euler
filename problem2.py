def fibonacci():
    series = [1,2] 
    count = 0
    while True:
        series.append(series[count]+series[count+1])
        count += 1
        if max(series)>4000000:
            break

    even = []
    for i in range(len(series)):
        # odd = []
        if series[i] % 2 == 0:
            # print(series[i])
            even.append(series[i])
    print(sum(even))
    # print(odd)

if __name__ == '__main__':
    fibonacci()