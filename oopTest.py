class Counter():
    counter=0
    def __init__(self):
        self.counter+=1

    def printCounter(self):
        print(self.counter)

class Account(Counter):
    def __init__(self,name,number,balance):
        self.__name=name
        self.__number=number
        self.__balance=balance
        Counter.__init__(self)

    def deposit(self,val):
        self.__balance+=val

    def withdrawal(self,val):
        if self.__balance-val>=0:
            print("Withdrawal of: ",val)
            print("Balance: ",self.__balance)
        else:
            print("No Withdrawal")

    def getBalance(self):
        print("Balance: ",self.__balance)

    def getBalance(self,b):
        print(str((self.__balance*(b/100))+self.__balance))

    def print(self):
        print("Name: ",self.__name)
        print("Balance: \n",self.__balance)


class Savings(Account):
    def __init__(self,name,number,balance,interestRate):
        self.__interest=interestRate
        self.account=Account(name,number,balance)

    def print(self):
        print("Interest Rate: ",self.__interest)
        self.account.print()

    def balanceAfterYear(self):
        #print("interest: ",self.__interest)
        print("Balance after 1 year: ",sep=" ")
        self.account.getBalance(self.__interest)

class fixedDeposit(Account):
    def __init__(self,name,number,balance,interestRate,minBalance):
        self.account=Account(name,number,balance)
        self.__interest=interestRate
        self.__minBalance=minBalance

    def print(self):
        print("Interest Rate: ",self.__interest)
        self.account.print()

cus1=Savings("Siddhart",1,1000,4)
cus1.print()
cus1.balanceAfterYear()

cus2=fixedDeposit("Vinit",22,2000,8,100)
cus2.print()

c=Counter()
c.printCounter()
