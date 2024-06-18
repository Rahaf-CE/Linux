import ast
from Product import *
from User import *
from datetime import datetime
class Online_store:

    def __init__(self,product_list,users_list):
        # Define a list to store the product information
        self.product_list = product_list
        self.users_list = users_list



    def load_products_from_file(self, file_path):
        # Open the file for reading
        try:
            with open(file_path, 'r') as file:
                # Iterate through each line in the file
                for line in file:
                    # Split the line into components using the semicolon delimiter
                    components = line.strip().split(';')

                    if (len(components) == 9):

                        Product_id, Product_name, Product_category, \
                            Price, Inventory, Supplier, Has_an_offer, Offer_Price, \
                            valid_Until = components
                        product = Product(int(Product_id), Product_name, Product_category, int(Price)
                                          , Inventory, Supplier, int(Has_an_offer), int(Offer_Price), valid_Until)
                        self.product_list.append(product)



        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    # Now you have the product information loaded into the product_list
    # You can access and manipulate the data as needed
    def load_users_from_file(self, file_path2):
        # Open the file for reading
        try:
            with open(file_path2, 'r') as file:
                # Iterate through each line in the file
                for line in file:
                    # Split the line into components using the semicolon delimiter
                    components2 = line.strip().split(';')

                    if (len(components2) == 7):
                        User_id, User_name, User_DoB,\
                        Role, Active, Basket,\
                        Order = components2
                        user = User(int(User_id), User_name, User_DoB, Role
                        , Active, ast.literal_eval(Basket),int(Order))
                        self.users_list.append(user)
                    elif (len(components2) == 5):
                        User_id, User_name, User_DoB,\
                        Role, Active = components2
                        user = User(int(User_id), User_name, User_DoB, Role
                        , Active)
                        self.users_list.append(user)






        except FileNotFoundError:
            print(f"File not found: {file_path2}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def display_users(self):
        for user in self.users_list:
            print(f"user ID: {user.User_id}")
            print(f"Name: {user.User_name}")
            print(f"Date Of Birth: {user.User_DoB}")
            print(f"Role: {user.Role}")
            print(f"Basket: {user.Basket}")
            print(f"Active: {user.Active}")
            print(f"On Sale: {user.Order}")
            print()  # Add an empty line to separate products
    def printChoices(self):
        print('1. Add product (Admin Only)')
        print('2. Place an item on sale (Admin Only)')
        print('3. Update product (admin-only)')
        print('4. Add a new user (admin-only)')
        print('5. Update user (admin-only)')
        print('6. Display all users (admin-only)')
        print('7. List products (admin and shopper)')
        print('8. List shoppers (admin)')
        print('9. Add product to the basket (shopper-only)')
        print('10. Display basket (shopper-only)')
        print('11.  Update basket (shopper-only)')
        print('12. Place order (shopper-only)')
        print('13. Execute order (admin-only)')
        print('14. Save products to a file (admin-only)')
        print('15. Save users to a text file (admin-only)')
        print('16. Exit')

    def Add_product(self):
        while True:

            while True:
                try:
                    Product_id = int(input("Enter the product id (6 digits number)"))
                    if 100000 <= Product_id <= 999999:
                        print("You entered a valid 6-digit integer:", Product_id)
                        break  # Exit the loop if a valid input is provided
                    else:
                        print("Please enter a 6-digit integer.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            # Check if the entered ID already exists in the list
            if any(product.Product_id == Product_id for product in self.product_list):
                print("Product with this ID already exists.")

            else:
               Product_name=input('Product name :\n')
               Product_category=input('Product category :\n')
               Price= input('Price :\n')
               Price=int(Price)
               Inventory = input('Inventory :\n')
               Supplier = input('Supplier :\n')
               Has_an_Offer = input('Does your product Has an offer ?\n')
               Has_an_Offer=int(Has_an_Offer)
               Offer_Price=input('Offer Price :')
               Offer_Price=int(Offer_Price)
               valid_until=input('valid until :')
               product=Product(Product_id,Product_name,Product_category,
               Price,Inventory,Supplier,Has_an_Offer,
               Offer_Price,valid_until)
               self.product_list.append(product)

               another_product = input("Do you want to add another product? (yes/no): ")
               if another_product=='no':
                   break

    def place_an_item_on_sale(self):
        product_id=input('Enter the id of the item that you want to put on sale :')
        product_id=int(product_id)
        if any(product.Product_id == product_id for product in self.product_list):
            print('Ok! The product exists, You can place it on sale ')
            for product in self.product_list:
                if(product.Product_id==product_id):
                    product.Has_an_offer=1
                    offerPrice=input('Enter the offer Price :')
                    offerPrice=int(offerPrice)
                    product.Offer_Price=offerPrice
                    # Prompt the user to enter a date in a specific format
                    date_string = input("this sale is valid until (YYYY-MM-DD): ")

                    # Attempt to parse the user input into a datetime object
                    try:
                        date = datetime.strptime(date_string, "%Y-%m-%d")
                        print("You entered a valid date and it was set successfully:")
                        product.valid_Until=date
                        print(product.valid_Until)
                    except ValueError:
                        print("Invalid date format. Please use YYYY-MM-DD format.")


    def Update_Product(self):
        product_id = input('Enter the id of the item that you want to update :')
        product_id = int(product_id)
        if any(product.Product_id == product_id for product in self.product_list):
            print('Ok! The product exists, You can update it ')
            for product in self.product_list:
                if (product.Product_id == product_id):
                    print('what is the field that you want to update : ')
                    print('1.Product Name')
                    print('2.Category')
                    print('3.Price')
                    print('4.Inventory')
                    print('5.Supplier')
                    print('6.Has_an_Offer')

                    choice=input()
                    if(choice == '1'):
                        newName=input('Enter the new Name:\n')
                        product.Product_name=newName
                    elif (choice == '2'):
                        newCategory = input('Enter the new category:\n')
                        product.Product_category = newCategory
                    elif (choice == '3'):
                        newPrice = input('Enter the new price:\n')
                        product.Price = newPrice
                    elif (choice == '4'):
                        newInventory = input('Enter the new inventory:\n')
                        product.Inventory = newInventory
                    elif (choice == '5'):
                        newSupplier = input('Enter the new Supplier:\n')
                        product.Supplier = newSupplier
                    elif (choice == '6'):
                        self.place_an_item_on_sale()

            print('Updating Process finished successfully!')
            for product in self.product_list:
                print(product.Product_name)

        else:
            print('This id doesnt match any product!!!')


    def add_user(self):
        while True:
            try:
                User_id = int(input("Enter the user id (6 digits number)"))
                if 100000 <= User_id <= 999999:
                    print("You entered a valid 6-digit integer:", User_id)
                    break  # Exit the loop if a valid input is provided
                else:
                    print("Please enter a 6-digit integer.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        if any(user.User_id == User_id for user in self.users_list):
             print("User already exists.")
        else:
             User_name = input("Enter User Name: ")
             User_DoB = input("Enter User Date of Birth (YYYY-MM-DD): ")
             Role = input("Enter Role (admin or shopper): ")
             Active = input("Enter Active (1 for active, 0 for not active): ")

             user = User(User_id, User_name, User_DoB, Role, int(Active), {}, 0)
             self.users_list.append(user)
             print(f"User {User_id} added successfully.")



    def update_user(self):
            User_id = input("Enter the User ID of the user you want to update: ")
            User_id = int(User_id)
            # Find the user
            user_to_update = None
            for user in self.users_list:
                if user.User_id == User_id:
                    user_to_update = user
                    break

            if user_to_update:
                print("User found. choose the field that you want to update:")
                print("1. User name")
                print("2. User date of birth")
                print("3. Role")
                print("4. Active")
                choice = input("Enter number of the field you want to update: ")

                if choice == '1':
                    new_name = input("Enter the new user name: ")
                    user_to_update.User_name = new_name
                elif choice == '2':
                    new_dob = input("Enter the new date of birth (YYYY-MM-DD): ")

                    # Attempt to parse the user input into a datetime object
                    try:
                        date = datetime.strptime(new_dob, "%Y-%m-%d")
                        print("You entered a valid date and it was set successfully:")
                        user_to_update.User_DoB = new_dob
                    except ValueError:
                        print("Invalid date format. Please use YYYY-MM-DD format.")

                elif choice == '3':
                    while True:
                        new_role = input("Enter the new role (admin or shopper): ")
                        if new_role in ['admin', 'shopper']:
                            user_to_update.Role = new_role
                            break
                        else:
                            print(" Please enter 'admin' or 'shopper'.")

                elif choice == '4':
                    while True:
                        new_active = input("Enter the new active status (1 for active, 0 for not active): ")
                        if new_active in ['0', '1']:
                            user_to_update.Active = int(new_active)
                            break
                        else:
                            print(" Please enter 0 or 1 .")

                else:
                    print("Invalid field choice.")

                print("User updated successfully.")
            else:
                print("User not found with the provided User ID.")


    def display_all_users(self):
        print("All Users :")
        for user in self.users_list:
            print(f"User ID: {user.User_id}")
            print(f"User Name: {user.User_name}")
            print(f"User Date of Birth: {user.User_DoB}")
            print(f"Role: {user.Role}")
            print(f"Active: {user.Active}")
            print(f"Basket: {user.Basket}")
            print(f"Order: {user.Order}")
            print('============================================================')



    def list_products(self):
        print('Choose one of the following options :')
        print('1. Print all products')
        print('2. Print Products that have offers')
        print('3. Print Products that belonging to a specific category')
        print('4. Print Products with same entered name')

        choice=input()
        if(choice == '1'):
            print('list size : ',len(self.product_list))
            for product in self.product_list:
                print('product_id :',product.Product_id)
                print('product name:', product.Product_name)
                print('product category :', product.Product_category)
                print('price :', product.Price)
                print('Inventory :', product.Inventory)
                print('supplier :', product.Supplier)
                print('has an offer :', product.Has_an_offer)
                print('offer price :', product.Offer_Price)
                print('valid until :', product.valid_Until)
                print('=========================================================================================')

        elif(choice == '2'):
            for product in self.product_list:
                if product.Has_an_offer == 1:
                    print('product_id :', product.Product_id)
                    print('product name:', product.Product_name)
                    print('product category :', product.Product_category)
                    print('price :', product.Price)
                    print('Inventory :', product.Inventory)
                    print('supplier :', product.Supplier)
                    print('has an offer :', product.Has_an_offer)
                    print('offer price :', product.Offer_Price)
                    print('valid until :', product.valid_Until)
                    print('=========================================================================================')

        elif (choice == '3'):
            category=input('Enter the category to list its products :')
            for product in self.product_list:
                if product.Product_category==category:
                    print('product_id :', product.Product_id)
                    print('product name:', product.Product_name)
                    print('product category :', product.Product_category)
                    print('price :', product.Price)
                    print('Inventory :', product.Inventory)
                    print('supplier :', product.Supplier)
                    print('has an offer :', product.Has_an_offer)
                    print('offer price :', product.Offer_Price)
                    print('valid until :', product.valid_Until)
                    print('=========================================================================================')

        elif (choice == '4'):
            name=input('Enter the name to list its products :')
            for product in self.product_list:
                if product.Product_name==name:
                    print('product_id :', product.Product_id)
                    print('product name:', product.Product_name)
                    print('product category :', product.Product_category)
                    print('price :', product.Price)
                    print('Inventory :', product.Inventory)
                    print('supplier :', product.Supplier)
                    print('has an offer :', product.Has_an_offer)
                    print('offer price :', product.Offer_Price)
                    print('valid until :', product.valid_Until)
                    print('=========================================================================================')


    def list_shoppers(self):
        print('Choose one of the  following :')
        print('1.List all Shoppers')
        print('2.List Shoppers with items in the basket')
        print('3.Has unprocessed orders')
        print('4. Requested an order')
        choice=input()
        if choice== '1':
            for user in self.users_list:
                if user.Role=='shopper':
                    print('User id :',user.User_id)
                    print('user name: ',user.User_name)
                    print('user date of birth :',user.User_DoB)
                    print('Role :',user.Role)
                    print('Active: ',user.Active)
                    print('Basket: ',user.Basket)
                    print('Order: ',user.Order)
                    print('========================================================================')


        if choice== '2':
            for user in self.users_list:
               if len(user.Basket) >0 and user.Role == 'shopper':
                   print(len(user.Basket))
                   print('User id :', user.User_id)
                   print('user name: ', user.User_name)
                   print('user date of birth :', user.User_DoB)
                   print('Role :', user.Role)
                   print('Active: ', user.Active)
                   print('Basket: ', user.Basket)
                   print('Order: ', user.Order)
                   print('========================================================================')



        if choice== '3':
            for user in self.users_list:
                if user.Order==0 and user.Role== 'shopper':
                    print(len(user.Basket))
                    print('User id :', user.User_id)
                    print('user name: ', user.User_name)
                    print('user date of birth :', user.User_DoB)
                    print('Role :', user.Role)
                    print('Active: ', user.Active)
                    print('Basket: ', user.Basket)
                    print('Order: ', user.Order)
                    print('========================================================================')


    def display_Basket(self,USID):
        for user in self.users_list:
          if user.User_id==USID:
            Basket_Cost=0
            Basket_Cost=int(Basket_Cost)
            purchase_Cost=0
            purchase_Cost=int(purchase_Cost)
            print('Your Basket :\n')
            for key in user.Basket:

               for product in self.product_list:
                   if product.Product_id==int(key):
                       print('product_id :', product.Product_id)
                       print('product name:', product.Product_name)
                       print('product category :', product.Product_category)
                       print('price :', product.Price)
                       print('Inventory :', product.Inventory)
                       print('supplier :', product.Supplier)
                       print('has an offer :', product.Has_an_offer)
                       print('offer price :', product.Offer_Price)
                       print('valid until :', product.valid_Until)
                       print('Number of items : ',user.Basket[key])
                       if product.Has_an_offer== 1:
                           purchase_Cost=(int(user.Basket[key])*product.Offer_Price)
                           Basket_Cost+=purchase_Cost
                           print('Cost of purchase of the product = ',str(purchase_Cost))
                       elif product.Has_an_offer ==0:
                           purchase_Cost = (int(user.Basket[key])* product.Price)
                           Basket_Cost += purchase_Cost
                           print('Cost of purchase of the product = ', purchase_Cost)
                       print('=========================================================================================')


            print('Basket Cost : ',str(Basket_Cost))




    def add_Product_to_Basket(self,USID):
        print('What is the id of the product you want to add : ')
        id=input()
        print('How many items do you need to add in your basket ?')
        numOfItems=input()
        numOfItems=int(numOfItems)
        for user in self.users_list:
            if user.User_id==USID:
                newList=user.Basket.copy()

                user.Basket[int (id)] = str(numOfItems)






    def update_basket(self,USID):
        print('Choice one of the updating options :')
        print('1. Clear  : (Remove all products from the basket ) ')
        print('2. Remove : (Remove a specific product from the basket)')
        print('3. Update : (Change the number of items of a particular product in the basket)')
        choice =input()
        if choice == '1':
            for user in self.users_list:
                if user.User_id==USID:
                    user.Basket.clear()
                    print('Your basket now is empty')

        elif choice == '2':

            print('Enter the id of the product you want to remove : ')
            id=input()
            id = int(id)
            for user in self.users_list:
                if user.User_id== USID:
                    newList=user.Basket.copy()
                    for key in newList:
                        if key == id:
                          del user.Basket[key]


        elif choice == '3':
          print('Enter the id of the product that want to be updated')
          id=input()
          id=int(id)
          for user in self.users_list:
              if user.User_id==USID:
                  newList=user.Basket.copy()
                  for key in newList:
                      if key ==id:
                          newAmount=input('Enter the new number of items')
                          user.Basket[key]=newAmount


    def place_order(self,USID):

            for user in self.users_list:
                if user.User_id== USID :
                    if user.Order==0:
                      user.Order = 1
                      print("Order placed successfully for user ",str( USID))
                    elif user.Order==1:
                        print('You have already but an order')


    def execute_order_for_shopper(self):
        # Find the shopper
        shopper_id = int(input("Enter the ID of the shopper whose order you want to execute: "))
        found_shopper = None
        for user in self.users_list:
            if user.User_id == shopper_id:
                found_shopper = user
                break

        if found_shopper:
            if found_shopper.Order == 1 :
                for product_id in found_shopper.Basket.copy():
                    for product in self.product_list:
                        if product.Product_id == product_id:
                            if int(product.Inventory) >= int(found_shopper.Basket[product_id]):
                                print('The Inventory of product : ',product.Product_name)
                                print('Before Execute the order :',product.Inventory)
                                product.Inventory = str(int(product.Inventory) - int(found_shopper.Basket[product_id]))
                                print('after execute the order:', product.Inventory)
                                print('-----------------------------------------------------------------------')
                            else:
                                print("Order not executed.")

                # Clear the items from the shopper's basket
                found_shopper.Basket.clear()
                found_shopper.Order = 0
                print(f"Order executed for shopper ID {found_shopper.User_id}. Basket cleared.")
            else:
                print("you cant execute order because shopper order equal zero")
        else:
            print("Shopper not found ")

    def save_products_to_file(self):
        file_name = input("Enter the name of the file to save the product information: ")
        try:
            with open(file_name, 'w') as file:
                for product in self.product_list:
                    file.write(f"{product.Product_id};{product.Product_name};{product.Product_category};"
                               f"{product.Price};{product.Inventory};{product.Supplier};"
                               f"{product.Has_an_offer};{product.Offer_Price};{product.valid_Until}\n")

            print("Product information saved to the file successfully ")
        except Exception as e:
            print(f"An error occurred : {str(e)}")

    def save_users_to_file(self):
        file_name = input("Enter the name of the text file to s" "ave the information: ")
        try:
            with open(file_name, 'w') as file:
                for user in self.users_list:
                    basket_str = str(user.Basket).replace("'", "\"")
                    file.write(f"{user.User_id};{user.User_name};{user.User_DoB};"
                               f"{user.Role};{user.Active};{basket_str};{user.Order}\n")

            print("User information saved to the file successfully ")
        except Exception as e:
            print(f"An error occurred : {str(e)}")