from Online_store import Online_store
from Product import Product
from User import User
products_list=[]
users_list=[]
file_path = 'products.txt'  # Replace with the actual path to your file
file_path2='users.txt'
store = Online_store(products_list,users_list)
store.load_products_from_file(file_path)
store.load_users_from_file(file_path2)


print('\nWelcome in our Great Online Store !')

while True:


             try:
                    USID = int(input("Enter your id please .......... (6 digits number)\n"))
                    if 100000 <= USID <= 999999 :
                          print("You entered a valid 6-digit ID:", USID)
                          break  # Exit the loop if a valid input is provided
                    else:
                        print("You Are not in the system !!! Try again ")

             except ValueError:
                    print("Invalid input. Please enter a valid integer.")


user_exists=False
Role=None
for user in store.users_list:
    if user.User_id==USID:
        user_exists=True
        Role=user.Role
        break




print('you are accessed with user_id : ',str(USID),'As a ',Role)

while True:
    print('Enter Your choice, Note the Accessibility! ')
    store.printChoices()
    choice = input()
    if choice == '1':
        if Role == 'admin' and user_exists==True:
         print('You need to Add Product .....................')
         print('Before adding The product, you have :',str(len(store.product_list)),'Products')
         store.Add_product()
         print('After adding This product, you have :', str(len(store.product_list)),'Products')
        else:
            print('You are not admin ! Access Denied!!!!! ')

    elif choice == '2':
        if Role == 'admin' and user_exists == True:
          print('you need to Place an item on sale ..............')
          store.place_an_item_on_sale()
        else:
            print('Your are not Admin,,, Access denied !!!!!!!!')
    elif choice == '3':
        if Role == 'admin' and user_exists == True:
         print('you need to Update product ......................')
         store.Update_Product()
        else:
            print('Your are not Admin,,, Access denied !!!!!!!!')
    elif choice == '4':
        if Role == 'admin' and user_exists == True:
            print('you need to Add a new User............................')
            store.add_user()
        else:
            print('You are not an admin so you cant add users')
    elif choice == '5':
        if Role == 'admin' and user_exists == True:
            print('you need to Update user..................................')
            store.update_user()
        else:
            print('You are not an admin so you cant update any user')
    elif choice == '6':
        if Role == 'admin' and user_exists == True:
            print('you need to Display all users................................')
            store.display_all_users()
    elif choice == '7':
        if user_exists==True:
         print('you need to List Products ..................')
         store.list_products()
    elif choice == '8':
        if Role == 'admin' and user_exists == True:
          print('you need to List shoppers............')
          store.list_shoppers()
        else:
          print('Sorry ! you are not an admin , Access Denied!!!')
    elif choice == '9':
        if Role=='shopper' and user_exists==True:
         print('you need to Add product to the basket...............')
         store.add_Product_to_Basket(USID)
        else:
            print('You are not a shopper! sorry Access Denied!!!!!')
    elif choice == '10':
        if Role=='shopper' and user_exists== True:
         print('you need to Display basket...................')
         store.display_Basket(USID)

        else:
            print('You are not a shopper, Access denied!!!!')

    elif choice == '11':
        if Role == 'shopper' and user_exists == True:
         print('you need to update the basket................')
         store.update_basket(USID)
        else:
            print('Access Denied! you are not a shopper!!!!!')
    elif choice == '12':
        if Role == 'shopper' and user_exists == True:
            print('You need to place an order ........................ ')
            store.place_order(USID)
        else:
            print('You are not a shopper, you cant place order')
    elif choice == '13':
        if Role == 'admin' and user_exists == True:
            print('execute order')
            store.execute_order_for_shopper()
        else:
            print('You are not an admin so you cant execute order ')

    elif choice == '14':
        if Role == 'admin' and user_exists == True:
            print('Save products to a file')
            store.save_products_to_file()
        else:
            print('You are not an admin so you cant save products to a file ')

    elif choice == '15':
        if Role == 'admin' and user_exists == True:
            print('Save users to a text file')
            store.save_users_to_file()
        else:
            print('You are not an admin so you cant save users to a file ')


    elif choice == '16':
        print('remember to save users and products informations')
        break
    else:
        print('Your choice invalid!')






