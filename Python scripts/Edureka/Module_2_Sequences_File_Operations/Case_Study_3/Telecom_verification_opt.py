# By Gaurav
# Problem : Optimize verification process
# Tale 12 digit alphanumeric string as input, encrypt, decrypt and print
################################################

import rsa
import re

publicKey, privateKey = rsa.newkeys(512)

def verify(var_list):
    match = re.match('^[a-zA-Z0-9_@]{12}$',var_list)

    if match:
        print("Reference ID is valid.")
        return True
    else:
        print("""Reference ID invalid !! :  
                    Following is the criteria for valid Reference ID:
                     1. Must be aplhanumeric
                     2. Must be 12 characters long 
                     3. Can contain @ and _
                     """)
        return False

ref_id = input('Please enter 12 digit reference id: ')

if verify(ref_id):
    enc_ref_id = rsa.encrypt(ref_id.encode(),publicKey)
    print("Encrypted Reference Id: ", enc_ref_id)
    var = input("Do you want to decript reference id (y/n) ? :")
    if var.upper() == 'Y':
        dec_ref_id = rsa.decrypt(enc_ref_id, privateKey).decode()
        print("Decrypted Reference Id: ",dec_ref_id)
