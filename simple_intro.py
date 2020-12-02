#Takes in a list of Account objects accountList, and a string name
#Returns the balance of the first Account in accountList with the given name
#or returns the string "Account Not Found" if there is no Account
#in accountList with the specified name
def getBalance(accountList,name):
    #Precondition: check if list is empty
    if len(accountList) == 0:
            return "Account Not Found"
    for i in range(len(accountList)): 
       #print(accountList[i].name)
        if accountList[i].name == name:       
            return accountList[i].balance      
    return "Account Not Found"

    


# DO NOT EDIT ANYTHING BELOW THIS LINE

#Account class
class Account:
    #Initialize an Account object.  Account objects have two instance variables
    #self.name is a string, representing the name associated with the Account
    #self.balance is a float, representing the balance of the account in $.
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    #String representation of an Account object - "name: $balance"
    def __repr__(self):
        return self.name + ": $" + str(self.balance)

#Create some accounts
a1 = Account("Scrooge McDuck", 10000000000)
a2 = Account("Macklemore",20)
a3 = Account("Loch Ness Monster",3.5)
a4 = Account("College Student",-78000)
a5 = Account("Bruce Wayne", 212013114)
a6 = Account("The Shoe from Monopoly",200)

bank1 = [a1,a2,a3,a4,a5,a6]
bank2 = [a4]
bank3 = []

testBanks = [bank1, bank1, bank1, bank2, bank2, bank3]
testNames = ["Scrooge McDuck","Dr. Horrible","College Student",
             "Scrooge McDuck","College Student","Bruce Wayne"]
correct = [10000000000,"Account Not Found",-78000,
           "Account Not Found",-78000,"Account Not Found"]

count = 0

for i in range(len(correct)):
    print("TEST #"+str(i+1))
    try:
        print("Running: getBalance(",testBanks[i],",",testNames[i],")\n")
        output = getBalance(testBanks[i],testNames[i])
        print("Expected:",correct[i],"\n\nGot:",output)
        if (correct[i] == output):
            count=count+1
        else:
            print("FAIL: Incorrect output")
    except Exception as e:
        print("FAIL: Error ", e)
    print()

print(count,"out of",len(testBanks),"tests passed.")
