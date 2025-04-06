def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundInterest()
# This first 3 lines are provided for you
    try:
        client_one_principal = float(input("Principle (amount): "))
        client_one_time = float(input("Time:               "))
        client_one_rate = float(input("Rate:               "))

        CI = yougetACompoundInterest(client_one_principal, client_one_time, client_one_rate)
        
        return client_one_principal, client_one_time, client_one_rate
    
    except:
        print("Error, Please enter a numeric input.")


def yougetACompoundInterest(client_one_principal, client_one_time, client_one_rate):
    
    amount = client_one_principal((1 + client_one_rate/100)**client_one_time)
    CI = amount - client_one_principal

    return 
#

if __name__ == "__main__":
    calculateCompoundInterest()
    

