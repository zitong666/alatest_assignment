import csv
import os.path


# Import the price list from csv files to the code for use
def get_list(company_list):

    # Create a data structure to save the prefix and price
    price_list = open(company_list, "r")
    csv_reader = csv.reader(price_list)
    dictionary = {}

    # Start to write in to dictionary
    file_name = os.path.splitext(company_list)
    dictionary['name_operation'] = file_name[0]

    # Defind and find the max length of the prefix for use
    global max_len
    for row in csv_reader:
        if csv_reader.line_num == 1:
            continue
        dictionary[row[0]] = row[1]
        if len(row[0]) > max_len:
            max_len = len(row[0])
    price_list.close()

    return dictionary

# Search the cheapest price and corresponding operator for the input telephone number
def find_price(phoneNumber, companyName, currentPrice):

    # Create an empty dictionary to record the operator who has the matched prefix
    chosenCompany = {}

    # Traversal all of the operators to find the price by for loop
    for company in company_list:
        if company.get(phoneNumber):
            if company.get(phoneNumber) < currentPrice:
                companyName = company.get('name_operation')
                currentPrice = company.get(phoneNumber)
                chosenCompany = company
            else:
                company_list.remove(company)

    # If find the matched price and operator, remove the item in the dictionary
    # Just record the value of price and operator name
    if chosenCompany != {}:
        company_list.remove(chosenCompany)

    # After finishing the recrusion (the length of the decrease to 1
    # and there is no more opreator's price list to search), we can
    # output the result
    if len(phoneNumber) == 1 or len(company_list) == 0:
        if companyName != "":
            print("The cheapest price is $ " + currentPrice + "/min with " + companyName)
            return True
        else:
            print("Sorry, number you have dialed is not available.")
            return False

    # If the recursion is not finished, we can continue to find the
    # cheapest price and corresponding operator
    else:
        phoneNumber = phoneNumber[0:len(phoneNumber)-1]
        return find_price(phoneNumber, companyName, currentPrice)

# Defind the location of the operators' price list
# and create an empty list to put their locations
company_A = "companyA.csv"
company_B = "companyB.csv"
num_company = (company_A, company_B)
company_list = []

# Using the for loop to finish the input of all price lists and
# set the initial value of the max length of the prefix to 0
max_len = 0
for item in range(len(num_company)):
    company_list.append(get_list(num_company[item]))

# Input the telephone number which want to find the
# matched operator and cheapest price
phone = input("Enter your telephone number: ")
print("Dialing:", phone)

# Defind the final price as $ 999/min, and then
# compare it with operator's price list
final_price = "999"

# Cut the telephone number into the suitable length
# to avoid the meaningless search loop
phoneNumber = phone[0:max_len]

# Launch the find_price function to finish the price search
find_price(phoneNumber, "", final_price)
