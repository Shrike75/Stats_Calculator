c = int(input("# of data points: "))
a = 1
set1 = []
while a <= c:
    if a == 1:
        set1.append(float(input(f"{a}st x-value: "))) 
    if a == 2:
        set1.append(float(input(f"{a}nd x-value: ")))
    if a == 3:
        set1.append(float(input(f"{a}rd x-value: ")))
    elif a > 3:
        set1.append(float(input(f"{a}th x-value: ")))
    a += 1
mean_x = sum(set1)/c
a = 1
set2 = []
while a <= c:
    if a == 1:
        set2.append(float(input(f"{a}st y-value: ")))
    if a == 2:
        set2.append(float(input(f"{a}nd y-value: ")))
    if a == 3:
        set2.append(float(input(f"{a}rd y-value: ")))
    elif a > 3:
        set2.append(float(input(f"{a}th y-value: "))) 
    a += 1
mean_y = sum(set2)/c
a = 0
n = 0
e = 0 
while a < c:
    n += (set1[a]-mean_x)*(set2[a]-mean_y)
    e += (set1[a]-mean_x)**2
    a += 1
m = n/e
b = mean_y-m*mean_x
def lbf(inp):
    return m*inp + b
a = 0
i = 0
h = 0
while a < c:
    i += (set2[a]-lbf(set1[a]))**2
    h += (set2[a]-mean_y)**2
    a += 1
o = n/((e*h)**0.5)
r = 1 - i/h
s = (n/c)**0.5
print(f"Correlation coefficient: {o}")
print(f"Line of best fit: \x1B[3my\x1B[0m = {m}\x1B[3mx\x1B[0m + {b}")
print(f"R squared: {r}")
print(f"RMSE: {s}")


