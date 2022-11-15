class Numbers:

    def __init__(self, n):
        self.n = n
        self.palindrome()
        self.prime()

    def palindrome(self):
        num = self.n
        sum = 0
        while num > 0:
            r = num % 10
            sum = r + (sum * 10)
            num = int(num / 10)
        if (sum == self.n):
            self.palin = "Number is palindrome."
        else:
            self.palin = "Number is not palindrome."

    def prime(self):
        flg = True
        num = 2

        while (num < self.n/2):
            if (self.n % num == 0):
                flg = False
                break
            num += 1

        if flg is True:
            self.p_msg = "Number is Prime"
        else:
            self.p_msg = "Number is not Prime"

    def showres(self):
        print(self.p_msg, self.palin, sep='\n')


obj = Numbers(121)

obj.showres()
