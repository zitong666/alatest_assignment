import csv
import os.path


def get_list(company_list):

    # Create a data structure to save the prefix and price
    price_list = open(company_list, "r")
    csv_reader = csv.reader(price_list)

    # Start to write in to dictionary
    file_name = os.path.splitext(company_list)
    key_a = file_name[0]

    # Defind and find the max length of the prefix for use
    global max_len
    for row in csv_reader:
        if csv_reader.line_num == 1:
            continue

        # Create the nested dictionary to store all price lists in one dictionary
        dictionary.setdefault(key_a, {})[row[0]] = row[1]
        if len(row[0]) > max_len:
            max_len = len(row[0])
    price_list.close()

    return dictionary


def find_price(phone_number, company_name, current_price):

    # Create an empty dictionary to record the operator who has the matched prefix
    chosen_company = {}

    # Traversal all of the operators to find the price by for loop
    for company in dictionary.keys():
        if dictionary.get(company).get(phone_number):
            if dictionary.get(company).get(phone_number) < current_price:
                company_name = company
                current_price = dictionary.get(company).get(phone_number)
                chosen_company = company
            else:
                del dictionary[company]
                # dictionary.remove(company)

    # If find the matched price and operator, remove the item in the dictionary
    # Just record the value of price and operator name
    if chosen_company != {}:
        del dictionary[chosen_company]

    # After finishing the recrusion (the length of the decrease to 1
    # and there is no more opreator's price list to search), we can
    # output the result
    if len(phone_number) == 1 or len(dictionary) == 0:
        if company_name != "":
            print("The cheapest price is $ " + current_price + "/min with " + company_name)
            return True
        else:
            print("Sorry, number you have dialed is not available.")
            return False

    # If the recursion is not finished, we can continue to find the
    # cheapest price and corresponding operator
    else:
        phone_number = phone_number[0:len(phone_number)-1]
        return find_price(phone_number, company_name, current_price)


# Defined a new function to get the input telephone number.
def get_phone():
    phone = input("Enter your telephone number: ")
    print("Dialing:", phone)
    phone_number = phone[0:max_len]
    return phone_number

company_A = "companyA.csv"
company_B = "companyB.csv"
num_company = (company_A, company_B)
company_list = []
dictionary = {}
max_len = 0
for company in num_company:
    get_list(company)

final_price = "999"
find_price(get_phone(), "", final_price)




