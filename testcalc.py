import calc
def test_add():
    if calc.add(1, 2) == 3:
        print("Test add(a, b) is OK")
        print("Result:", calc.add(1, 2))
        print()
    else:
        print("Test add(a, b) is Fail")
        print("Result:", calc.add(1, 2))
        print()
def test_sub():
    if calc.sub(4, 2) == 2:
        print("Test sub(a, b) is OK")
        print("Result:", calc.sub(4, 2))
        print()
    else:
        print("Test sub(a, b) is Fail")
        print("Result:", calc.sub(4, 2))
        print()
def test_mul():
    if calc.mul(2, 5) == 10:
        print("Test mul(a, b) is OK")
        print("Result:", calc.mul(2, 5))
        print()
    else:
        print("Test mul(a, b) is Fail")
        print("Result:", calc.mul(2, 5))
        print()
def test_div():
    if calc.div(8, 4) == 2:
        print("Test div(a, b) is OK")
        print("Result:", calc.div(8, 4))
        print()
    else:
        print("Test div(a, b) is Fail")
        print("Result:", calc.div(8, 4))
        print()
def test_sqrt():
    if calc.sqrt(25) == 5:
        print("Test sqrt(a) is OK")
        print("Result:", calc.sqrt(25))
        print()
    else:
        print("Test sqrt(a) is Fail")
        print("Result:", calc.sqrt(25))
        print()
def test_pow():
    if calc.pow(5, 3) == 125:
        print("Test pow(a, b) is OK")
        print("Result:", calc.pow(5, 3))
        print()
    else:
        print("Test pow(a, b) is Fail")
        print("Result:", calc.pow(5, 3))
        print()
def test_compare1():
    if calc.compare1(2, 1) == 1:
        print("Test compare1(a, b) is OK")
        print("Result:", calc.compare1(2, 1))
        print()
    else:
        print("Test compare1(a, b) is Fail")
        print("Result:", calc.compare1(2, 1))
        print()
def test_compare2():
    if calc.compare2(1, 2) == -1:
        print("Test compare2(a, b) is OK")
        print("Result:", calc.compare2(1, 2))
        print()
    else:
        print("Test compare2(a, b) is Fail")
        print("Result:", calc.compare2(1, 2))
        print()
def test_compare3():
    if calc.compare3(1, 1) == 0:
        print("Test compare3(a, b) is OK")
        print("Result:", calc.compare3(1, 1))
        print()
    else:
        print("Test compare3(a, b) is Fail")
        print("Result:", calc.compare3(1, 1))
        print()
def test_compare4():
    if calc.compare4(-1, -1) == 0:
        print("Test compare4(a, b) is OK")
        print("Result:", calc.compare4(-1, -1))
        print()
    else:
        print("Test compare4(a, b) is Fail")
        print("Result:", calc.compare4(-1, -1))
        print()



test_add()
test_sub()
test_mul()
test_div()
test_sqrt()
test_pow()
test_compare1()
test_compare2()
test_compare3()
test_compare4()
