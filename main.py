def check(point):
    global w
    if 80 <= point <= 100:
        w = 4.0
    elif 70 <= point:
        w = 3.0
    elif 60 <= point:
        w = 2.0
    elif 50 <= point:
        w = 1.0
    elif 0 <= point:
        w = 0
    else:
        pass
    return w


def Grade(check):
    global s
    check = int(check)
    if check == 0:
        s = 'F'
    elif check == 1:
        s = 'D'
    elif check == 2:
        s = 'C'
    elif check == 3:
        s = 'B'
    elif check == 4:
        s = 'A'

    return s


print("Program Calculate Grade")
print("Input Data:")
Sum = 0
Name1 = input("Enter subject name(1) : ")
Sub1 = float(input("Enter subject score(1) : "))
tmp1 = check(Sub1)
Sum += tmp1 * 3
Grade1 = Grade(check(Sub1))

Name2 = input("Enter subject name(2) : ")
Sub2 = float(input("Enter subject score(2) : "))
tmp2 = check(Sub2)
Sum += tmp2 * 3
Grade2 = Grade(check(Sub2))

Name3 = input("Enter subject name(3) : ")
Sub3 = float(input("Enter subject score(3) : "))
tmp3 = check(Sub3)
Sum += tmp3 * 3
Grade3 = Grade(check(Sub3))

Name4 = input("Enter subject name(4) : ")
Sub4 = float(input("Enter subject score(4) : "))
tmp4 = check(Sub4)
Sum += tmp4 * 3
Grade4 = Grade(check(Sub4))

Name5 = input("Enter subject name(5) : ")
Sub5 = float(input("Enter subject score(5) : "))
tmp5 = check(Sub5)
Sum += tmp5 * 3
Grade5 = Grade(check(Sub5))

Avg = Sum / 15

print(" " * 27 + "Grade Report")
print("=" * 67)
print("Sub No.  Subject Name \t\t\t Mark \tGrade \tCredits \tPoints")
print("=" * 67)
print(f"1 \t\t{Name1} \t\t\t\t\t {Sub1} \t\t{Grade1} \t\t 3 \t\t {int(tmp1 * 3)}")
print(f"2 \t\t{Name2} \t\t\t\t {Sub2} \t\t{Grade2} \t\t 3 \t\t {int(tmp2 * 3)}")
print(f"3 \t\t{Name3}\t {Sub3} \t\t{Grade3} \t\t 3 \t\t {int(tmp3 * 3)}")
print(f"4 \t\t{Name4} \t\t\t {Sub4} \t\t{Grade4} \t\t 3 \t\t {int(tmp4 * 3)}")
print(f"5 \t\t{Name5} \t {Sub5} \t\t{Grade5} \t\t 3 \t\t {int(tmp5 * 3)}")
print("=" * 67)
print(" " * 33 + f"Total   \t\t\t 15 \t {int(Sum)} ")
print("Grade Point Average(GPA) : {:.2f}".format(Avg))
