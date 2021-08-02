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

    for row in csv_reader:
        if csv_reader.line_num == 1:
            continue
        dictionary[row[0]] = row[1]
    price_list.close()
    return dictionary


# Create a Node class with key, value, and children
class Node:

    def __init__(self):
        self.key = None
        self.value = None
        self.children = {}


# Inheritance from class Node to create new function
class Trie:

    # Initiate the root of trie
    def __init__(self):
        self.root = Node()

    # Insert the dictionary of price list into tree,
    # each digit of prefix as the children node,
    # value as the value (leaf) of the last digit.
    def insert(self, prefix, value):
        current_word = prefix
        current_node = self.root

        while len(current_word) > 0:
            if current_word[0] in current_node.children:
                current_node = current_node.children[current_word[0]]
                current_word = current_word[1:]
            else:
                new_node = Node()
                new_node.key = current_word[0]
                if len(current_word) == 1:
                    new_node.value = value

                current_node.children[current_word[0]] = new_node
                current_node = new_node
                current_word = current_word[1:]

    # Search the tree by the prefix with the longest matching principle,
    # output the cheapest price (True) or the search result (False).
    def search(self, prefix):

        current_word = prefix
        current_node = self.root

        # For loop to traversal the prefix and find the longest match in the tree
        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
                current_word = current_word[1:]
        if current_node.value == None:
            print('No service in this Operator')
            return False
        else:
            print('The cheapest price is $ ' + current_node.value + ' / min in this Operator')
            return True


# Start insert function with the dictionary and
# search function with the input phone number
def make_tree(words):
    tree = Trie()
    for word, value in words.items():
        tree.insert(word, value)
    tree.search(phone)

    return tree


company_A = "companyA.csv"
company_B = "companyB.csv"
num_company = (company_A, company_B)
company_list = []

# For loop to add the dictionaries into one list
for item in range(len(num_company)):
    company_list.append(get_list(num_company[item]))


phone = input("Enter your telephone number: ")
print("Dialing:", phone)

# Insert and search for each dictionary my make_tree function
for dictionary in company_list:
    price_tree = make_tree(dictionary)


