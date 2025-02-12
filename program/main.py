from approved import *

if __name__ == "__main__":
    login_gmail()
    
    table = import_data()
    send_email(table)
    
print("="*21)
print("Program Ended!")
print("="*21)
