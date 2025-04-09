"""
This is a mobile baniking application that allow transfer of money from one person mobile wallet to another 
This application is aiming at SME's in transacting money during their normal day to day operations
The application can also be used by family and friends to transfer money from one person to another. 
I was inspired by MPESA to create this application.



"""

  
banner="""
  __  __           _       _   _            ____                    _      _                   
 |  \/  |         | |     (_) | |          |  _ \                  | |    (_)                  
 | \  / |   ___   | |__    _  | |   ___    | |_) |   __ _   _ __   | | __  _   _ __     __ _   
 | |\/| |  / _ \  | '_ \  | | | |  / _ \   |  _ <   / _` | | '_ \  | |/ / | | | '_ \   / _` |  
 | |  | | | (_) | | |_) | | | | | |  __/   | |_) | | (_| | | | | | |   <  | | | | | | | (_| |  
 |_|  |_|  \___/  |_.__/  |_| |_|  \___|   |____/   \__,_| |_| |_| |_|\_\ |_| |_| |_|  \__, |  
                                                                                        __/ |  
                                                                                       |___/   
"""

import time  #importing time module 

print(f"{banner} \n Welcome to Mobile Banking Applicion \n Developed by Serge Assi " ) 
user_name=input("Enter your full name:   ").capitalize()

phone_number=input("Enter your phone number with country code i.e +1234543275843:  ").strip()

account_balance=0  
savings_balance=0 

start_time= time.localtime()
starting_time = time.strftime("%B %D:%H:%M:%S" , start_time)

filename="logs.txt"  
with open(filename, 'a') as file: #saving user logs in the logs file.
        data_line = f"USER LOGS \n Time: {starting_time} \n User: {user_name} \n Phone Number: {phone_number}\n"
        file.write(data_line)

        
statement={
    
} #I will store all the transactions in this dictionary and generate a report if need be 
def main():
    """This is the entry point to my application """
    while True: 
        user_action=input("What would you like to do today?[deposit, save,send, invoice,withdraw, viewstatement,widthrawfromsaving]").strip().lower()

        if user_action=="deposit":
            deposit()
        elif user_action=="send":
            send_money()
        elif user_action=="save":
            save_money()
        elif user_action=="withdraw":
            withdraw_money()

        elif user_action=="invoice":
            invoice_payment()
        elif user_action=="widthrawfromsaving":
            widtraw_from_savings()
        elif user_action=="viewstatement":
            view_statement()


def send_money():
    """
    This function allows sending of money from one mobile wallet to another , then deducts the amount from the account balance """
    global account_balance
    global filename
    receivers_name= input("Enter Receivers Name: ").capitalize()
    receivers_number=input("Enter Receiver Phone Number with country code i.e +3242743274 : " ).strip()
    
    
    
    try:
        sent_amaount= int(input("Enter amount to transact in Dollars($):"))
        if account_balance<= 0:
            #calculate transaction cost which is 1 percent total cost
            transaction = sent_amaount*(1/100)
            print(f"Dear {user_name} Please Deposit {sent_amaount + transaction} in your account to transact with {receivers_name}.")
           
            when= time.localtime()
            send_fail_time = time.strftime("%B %D:%H:%M:%S" , when) #formating time 

            with open(filename, 'a') as file:
                data_line = f"\n FAILED: at {send_fail_time} To transfer Amount: {sent_amaount}"
                file.write(data_line)
            


        else:
            account_balance= account_balance-(sent_amaount+transaction)
            print(f"Dear {user_name}, You have transfered a total of {sent_amaount} to {receivers_name} , {receivers_number}.  Your new account balance is {account_balance}.")  

            when= time.localtime()
            send_time = time.strftime("%B %D:%H:%M:%S" , when)
            with open(filename, 'a') as file:
                data_line = f"\n SUCCESS: at time: {send_time}, {sent_amaount} Transfered to {receivers_name} "
                file.write(data_line)

    except:
        print("Transfered amount should be in digits, Try again") 
        when= time.localtime()
        failed_time = time.strftime("%B %D:%H:%M:%S" , when)
        with open(filename, 'a') as file:
            data_line = f"\n FAILED: at time: {failed_time}, To send {sent_amaount} Transfer to {receivers_name} "
            file.write(data_line)
    

    return receivers_name,receivers_number
   

def invoice_payment():
    """This function allows the user to Invoce/ request another application user of payment."""
    customer_name=input("Enter the Name of person You want to request Payment: ").capitalize()
    customer_phone=input("Enter His/Her phone Number: ").strip()
    request_amount=int(input("Enter amount to Request: "))
    count = [10,20,30,40,50,60,70,80,90,100] 
    for i in count:
        print(f"Sending Invoice request. at {i}")
        i= i +1 
    

        
        
    print(f"Invoice sent successfully to {customer_name}, phone number {customer_phone} Amount: $ {request_amount}")
    when= time.localtime()
    invoce_time = time.strftime("%B %D:%H:%M:%S" , when)
    with open(filename, 'a') as file:
        data_line = f"\n SUCCESS: at time: {invoce_time}, To send  Invoice to {customer_name} Phone Number: {customer_phone} Amount: {request_amount} "
        file.write(data_line)

    

def withdraw_money():
    """This function allows users to widthraw money from their account balance.
    Users are not allowed to widthraw balance less than zero."""
    global account_balance


    withdraw_amount= int(input("Enter amount to Widthraw:  "))  
    if account_balance >= withdraw_amount and account_balance>0:
        account_balance = account_balance- withdraw_amount

        when= time.localtime()
        withdrawal_time = time.strftime("%B %D:%H:%M:%S" , when)
        

        print(f"Dear{user_name} , You have widthrawn $ {withdraw_amount} at {withdrawal_time}")
        with open(filename, 'a') as file:
            data_line = f"SUCCESS: at time: {withdrawal_time} Widthrawal of $ {withdraw_amount} "
            file.write(data_line)
    else:
        when= time.localtime()
        withdrawal_time = time.strftime("%B %D:%H:%M:%S" , when)
        print(f"Dear {user_name}, You have insufficient balance in your account to widthraw : $ {withdraw_amount} at {withdrawal_time} ")
        with open(filename, 'a') as file:
            data_line = f"\n FAILED: at time: {withdrawal_time} Widthrawal of $ {withdraw_amount} "
            file.write(data_line)

    return withdraw_amount, account_balance    



def save_money():
    """This functions transfers money from the account balance to savings account.
    Users are not allowed to transfer when balance is 0"""
    global account_balance
    global savings_balance

    saving_amount = int(input(" Enter amount to send to your savings account: "))
    interest_type=input("Which type of interest do you want? (Simple,Compund ?  )").strip().lower()
    saving_duration =int(input("Enter saving duration(in years): "))
    desired_rate=int(input("Enter your desired Rate : (in percentage ):  "))
    
    
    


    if interest_type=="simple":
         #simple interest calculator 

        interest= (saving_amount*saving_duration*desired_rate)/ 100
        
        total_amount=saving_amount+interest
        account_balance=account_balance-saving_amount
        when= time.localtime()
        savings_time = time.strftime("%B %D:%H:%M:%S" , when)
        print(f"{savings_time}  Dear {user_name}, You have deposited $ {saving_amount} into your Simple Interest savings account.\n Your new Account balance is $ {account_balance}. \n Your Savings Balance is: $ {saving_amount} \n Your savings Balance will be $ {total_amount} after {saving_duration}" )

        when= time.localtime()
        simple_int_time = time.strftime("%B %D:%H:%M:%S" , when)
        
        with open(filename, 'a') as file:
            data_line = f"SUCCESS: at time: {simple_int_time} SAVINGS  of $ {saving_amount} "
            file.write(data_line)

    elif interest_type=="compound":

      #compund interest calculator 
        total_amount = saving_amount * (pow((1 + desired_rate / 100), savings_time))
        interest = total_amount - saving_amount
        when= time.localtime()
        savings_time = time.strftime("%B %D:%H:%M:%S" , when)
        print(f"Dear {user_name}, You have deposited $ {saving_amount} into your Compound Interest savings account.\n Your new Account balance is $ {account_balance}. \n Your Savings Balance is: $ {saving_amount} \n Your savings Balance will be $ {total_amount} after {saving_duration}" )
        when= time.localtime()
        compund_int_time = time.strftime("%B %D:%H:%M:%S" , when)
        
        with open(filename, 'a') as file:
            data_line = f"\n SUCCESS: at time: {compund_int_time} SAVINGS  of $ {saving_amount} "
            file.write(data_line)

    return savings_balance,savings_time,account_balance

def deposit():
    """This function allows users to deposit money to their main account balance"""
    global account_balance 
    deposit_ammount= int(input("Enter amount to  Deposit in Dollars ($):  "))

    account_balance = account_balance+deposit_ammount
    when= time.localtime()
    deposit_time = time.strftime("%B %D:%H:%M:%S" , when)
    print(f"Dear {user_name} , You have Deposited {deposit_ammount}.  Your New account Balance is $ {account_balance} at {deposit_time}")

    when= time.localtime()
    deposit_time = time.strftime("%B %D:%H:%M:%S" , when)
        
    with open(filename, 'a') as file:
        data_line = f"SUCCESS: at time: {deposit_time} Deposit  of $ {deposit_ammount} "
        file.write(data_line)
    
    return deposit_ammount,account_balance,deposit_time


    
def view_statement():
  

    with open("logs.txt", "r") as file:
        content = file.read()


    print(content)
    when= time.localtime()
    view_time = time.strftime("%B %D:%H:%M:%S" , when)
        
    with open(filename, 'a') as file:
        data_line = f"SUCCESS: at time: {view_time} Viewing of Transaction Statements "
        file.write(data_line)


  

def generate_report():
    """My goal was to implement a function that can convert my statemnt to a pdf/word report."""
#CONVERT THE TXT FILE TO PDF REPORT 
    pass


    
def widtraw_from_savings():
    """This function allows windthrawal of money from savings account to the balance account."""
    global savings_balance
    global account_balance

    amount_widtraw= int(input("Enter amount to Widthraw from savings account: "))
    if amount_widtraw<account_balance:
        print(f"Failed, You cannot widthraw {amount_widtraw} while your savings balance is {savings_balance} ")

        when= time.localtime()
        withd_time = time.strftime("%B %D:%H:%M:%S" , when)
        
        with open(filename, 'a') as file:
            data_line = f"FAILED: at time: {withd_time} To widthraw from savings account "
            file.write(data_line)
    else:
        account_balance=account_balance+amount_widtraw

        when= time.localtime()
        swidth_time = time.strftime("%B %D:%H:%M:%S" , when)
        print(f"Success, You have widthraw {amount_widtraw} savings balance is {account_balance} ")
        
        with open(filename, 'a') as file:
            data_line = f"SUCCESS: at time: {swidth_time} Widthrawing {amount_widtraw} from savings."
            file.write(data_line)



    return account_balance
if __name__ == "__main__":
    main()