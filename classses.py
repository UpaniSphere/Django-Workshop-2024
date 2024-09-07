class Calculator:
    def __init__(self):
        self.num1 = 4
        self.num2 = 5
        self.opr = 4

    def evaluation(self):
        self.num1 = 4
        self.num2 = 5
        self.opr = "/"

        # check1 = type(num1)
        # check2 = type(num2)

        self.ans = 0

        if self.operator == "+":
            ans = self.num1 + self.num2

        elif self.operator == "-":
            ans = self.num1 - self.num2


        elif self.operator == "/":
            ans = self.num1 / self.num2


        elif self.operator == "x":
            ans = self.num1 * self.num2

        else:
            print("Error")

        print(self.ans)

expr = Calculator()

print(expr.__dict__)