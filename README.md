# 🛍️ Python Console-Based Online Shopping System


This project is a text-based online store implemented in Python, supporting features for both **Admins** and **Shoppers**. The system allows product management, user handling, basket operations, placing/executing orders, and persisting data to text files.

---

## 🚀 Features


### 👤 Admin Functionality

- Add new products
- Update existing products
- Place items on sale with expiration dates
- Add new users (Admins or Shoppers)
- Update user data
- Display all users
- Execute shopper orders
- Save/load product and user data to/from files

### 🛒 Shopper Functionality

- Add products to basket
- View and update basket contents
- Place orders
- View discounted products
- List products by category or name

---

## 📦 Classes Overview


### `Product`
Represents each product with attributes:
- `Product_id`, `Product_name`, `Product_category`
- `Price`, `Inventory`, `Supplier`
- `Has_an_offer`, `Offer_Price`, `valid_Until`

### `User`
Represents each user with attributes:
- `User_id`, `User_name`, `User_DoB`, `Role`, `Active`
- `Basket` (dictionary of product ID to quantity)
- `Order` (1 if order placed, 0 otherwise)

### `Online_store`
Manages product/user lists and all store functionalities, including:
- `load_users_from_file()` / `load_products_from_file()`
- `add_user()`, `update_user()`, `display_all_users()`
- `Add_product()`, `Update_Product()`, `place_an_item_on_sale()`
- `add_Product_to_Basket()`, `display_Basket()`, `update_basket()`
- `place_order()`, `execute_order_for_shopper()`
- `save_users_to_file()` / `save_products_to_file()`

---

## 🗃️ File Format (Text Files)


### Products (`products.txt`)
Product_id;Product_name;Category;Price;Inventory;Supplier;Has_an_offer;Offer_Price;Valid_Until

shell
Copy
Edit

### Users (`users.txt`)
User_id;User_name;Date_of_Birth;Role;Active;Basket;Order

css
Copy
Edit

Example basket format:
```json
{100101: "2", 100202: "1"}
🧪 Sample Run
plaintext
Copy
Edit
1. Add product (Admin Only)
2. Place an item on sale (Admin Only)
...
9. Add product to the basket (Shopper Only)
...
Enter your choice: 1

Enter the product id (6 digits number): 100123
Product name: Leather Bag
Category: Hand
Price: 250
Inventory: 30
Supplier: LuxBrand
...
💾 How to Run

bash
Copy
Edit
python main.py
Make sure the following are available in the same directory:

Product.py

User.py

users.txt

products.txt

📌 Project Structure

bash
Copy
Edit

online_store/
├── main.py                  # Contains the logic using Online_store
├── Product.py               # Product class
├── User.py                  # User class
├── users.txt                # Stored user data
├── products.txt             # Stored product data
└── README.md


🔐 Future Improvements
Add GUI using Tkinter or PyQt

Integrate database (e.g., MySQL or SQLite) instead of text files

Add login authentication and session handling

Extend to support product reviews, ratings, and search

