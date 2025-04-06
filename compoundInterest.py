def calculateCompoundInterest():
    
    principal = float(input("Principle (amount): "))
    time = float(input("Time:               "))
    rate = float(input("Rate:               "))
    
    principal2 = float(input("Principle (amount): "))
    time2 = float(input("Time:               "))
    rate2 = float(input("Rate:               "))

    principal3 = float(input("Principle (amount): "))
    time3 = float(input("Time:               "))
    rate3 = float(input("Rate:               "))

    amount = (principal)*(( 1 + (rate)/100)**time)
    CI = amount - principal
    rnd = round(CI, 2)
    print("Compound Interest: "+str(rnd)) 
    print("---")
    amount2 = (principal2)*(( 1 + (rate2)/100)**time2)
    CI2 = amount2 - principal2
    rnd2 = round(CI2, 2)
    print("Compound Interest: "+str(rnd2)) 
    print("---")
    amount3 = (principal3)*(( 1 + (rate3)/100)**time3)
    CI3 = amount3 - principal3
    rnd3 = round(CI3, 2)
    print("Compound Interest: "+str(rnd3)) 




    return 



if __name__ == "__main__":
    calculateCompoundInterest()






 #print("Compound Interest: "+str(intrest))


#A = P( 1 + R/100)^T

#CI = A - P

#A is Amount
#P is Principal Amount
#R is Interest Rate
#T is Time Span in Years
#CI is Compound Interest

    # end assignment

## If you want to test locally run > python compoundInterest.py

