def indian_to_nepali(money_amt):
    calc_money=money_amt*1.6
    return calc_money
def nepali_to_indian(money_amt):
    calc_money=money_amt/1.6
    return calc_money
def nepali_to_dollar(money_amt):
    calc_money=money_amt/132
    return calc_money
def dollar_to_nepali(money_amt):
    calc_money=money_amt*132
    return calc_money


def currency_converter():

    print("1. Nepali -------------> indian")
    print("2. indian -------------> Nepali")
    print("3. Nepali -------------> Dollar")
    print("4. Dollar -------------> Nepali")
    # print("5. Nep -------------> indian")

    while True:
        try: 

            choice=int(input("choose in which currncu you want to convert: "))
            if choice==1: 
                money_amt=int(input("Enter the amount of INDIAN money: "))
                converted_money_nep=indian_to_nepali(money_amt)
                print(f"RS.{converted_money_nep}")

            elif choice==2: 
                money_amt=int(input("Enter the amount of NEPALI money: "))
                converted_money_ind=nepali_to_indian(money_amt)
                print(f"RE. {converted_money_ind}")
    
            elif choice==3:
                money_amt=int(input("Enter the amountof NEPALI money: "))
                converted_money_dol=nepali_to_dollar(money_amt)
                print(f"{converted_money_dol} dollar")


            elif choice==4:
                money_amt=int(input("Enter the amountof Dollar: "))
                converted_money_nep=dollar_to_nepali(money_amt)
                print(f"RS. {converted_money_nep}")

            else:
                print("invalid input")

        except ValueError:
            print("oops! invalid error")



currency_converter()



    






