import re
import pandas as pd
import Customer
import Custom_Error

data= pd.read_csv("FairDealCustomerData.csv", names = ["LAST_NAME","FIRST_NAME","BLACKLISTED"])
df = pd.DataFrame(data)


def create_order(Customer):
    if str(Customer.isblacklisted) == str(1):
        raise Custom_Error(' : CustomerNotAllowedException')
    else:
        print("Valid Customer")

# print(df)
for i in df.index:
    mid_name = ''
    # name = 'Joshi, Mr. Gaurav Shyam, 0'
    # print(list(df.loc[i]))

    details = list(df.loc[i])
    temp_name = str(details[1])
    temp_name = temp_name.strip()
    temp_name = re.split(" ", temp_name)
    title = temp_name[0]
    first_name = temp_name[1]
    # Middle name only if exists
    if len(temp_name) == 3:
        mid_name = temp_name[2]

    last_name = details[0]
    blacklist = details[2]

    # print(title,first_name,mid_name,last_name,blacklist)


    # Create class objects
    Cust = Customer.Customer()

    Cust.setTitle(title)
    Cust.setFname(first_name+' '+mid_name)
    Cust.setLname(last_name)
    Cust.setIsblacklisted(str(blacklist))

    # print(Cust.__str__())

    try:
        create_order(Cust)
    except:
        print('CustomerNotAllowedException :', Cust.__str__())


