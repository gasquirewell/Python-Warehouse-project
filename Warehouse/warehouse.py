"""
        Program: Warehouse management system
        Author: Gerry Squirewell
    Description:
        1 - Register new item:
            title (input)
            cat (input)
            price (float)
            stock (int)

        2 - Display Catalog
        3 - Update Stock
        4 - Print Total Stock value
        5 - Print Stock Value
        6 - Report - out of stock
        7 - Total stock value
        8 - Categories (no duplicates)


"""
#imports
from menu import clear, print_menu, print_header, print_item
from item import Item 
import pickle


#global vars
catalog = []
data_file = 'warehouse.data'
last_id = 1


def serialize_catalog():
    global data_file
    writer = open(data_file, 'wb') #create/open a file to write Binary
    pickle.dump(catalog, writer)
    writer.close() #close stream, release the file
    print("*** Data serialized!")

def deserialize_catalog():
    try:
        global data_file
        global last_id
        reader = open(data_file, 'rb') #rb = open file to read binary data
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        last_item = catalog[-1]
        last_id = last_item.id +1
        print("** Deserialized " + str (len(catalog)) + "items" )
    
    except:
        print("Error: could not load data")

def register_item():
    global last_id
    try:
        print_header('Register New Item')
        title = input('Please provide the Title: ')
        cat = input('Please provide the Category: ')
        price = float(input('Please provide the Price: '))
        stock = int(input('Please provide the Stock: '))

        id = last_id
        last_id += 1
        item = Item(id, title, cat, price, stock)
        catalog.append(item)

        how_many = len(catalog)
        print("You now have: " + str(how_many) + "item on the catalog")
    
    # You are missing this:
        
    except ValueError:
        print("Error: could not save item")
    except:
        print("Error, something went wrong") 

def update_stock():
    try:
        display_catalog()
        id = input("Please provide the item id: ")
        found = False
        for item in catalog:
            if( str(item.id) == id):
                found = True
                val = input("Please provide new stock value: ")
                item.stock = int(val)
                print("Stock value updated")

        if( not found):
            print("** Error: Invalid ID: verify ad try again! **")
    
    except ValueError:
        print("Error: Invalid value - please enter numbers only")
    except:
        print("Error, something went wrong") 

def update_price():
    try:
        display_catalog()
        id = input("Please provide the item id: ")
        found = False
        for item in catalog:
            if( str(item.id) == id):
                found = True
                val = input("Please provide updated pricing: ")
                item.price = int(val)
                print("Price update alert")

        if( not found):
            print("** Error: Invalid ID: verify ad try again! **")
    
    except ValueError:
        print("Error: Invalid value - please enter numbers only")
    except:
        print("Error, something went wrong") 

def delete_item():
    display_catalog()
    id = input("Please provide the item id you would like to delete: ")
    for item in catalog:
        if( str(item.id)== id):
            del(item.id,item.category,item.price, item.stock, item.title)
    print(" Item was deleted")


def display_catalog():
    print_header("Your Current Catalog")
    for item in catalog:
        print_item(item)
      
 
def display_out_of_stock():
    print_header("Items currently out of stock")
    for item in catalog:
        if (item.stock == 0):
            print_item(item)

def total_stock_value():
    total = 0.0
    for item in catalog:
      total += item.price * item.stock
    
    print("Total value: " +str(total))

def list_categories():
    print_header("List of categories")
    for item in catalog:
        # while (item.category != item.category):
            print(item.category)
    
#instructions

deserialize_catalog()
input("Press Enter to continue: ")

opc= ''
while(opc != 'x'):
    clear()
    print_menu()

    opc = input("Please choose an option: ")

    # if comparisons
    if(opc =='1'):
        register_item()
        serialize_catalog()
    elif (opc == '2'):
        display_catalog()
    elif (opc == '3'):
        update_stock()
        serialize_catalog()
    elif (opc == '4'):
        update_price()
    elif (opc =='5'):
        delete_item()
        serialize_catalog()
    elif (opc == '6'):
        display_out_of_stock()
    elif (opc == '7'):
        total_stock_value()
    elif (opc == '8'):
        list_categories()
   

    input("Press enter to continue...")


