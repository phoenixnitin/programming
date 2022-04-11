## Vending Machine Operator
`Use python 3.10 to execute as match case is used`


Update test file at ./test/input1 or create new test file at ./test by providing correct file path at line 72 of operate_vending_machine.py

Execute as below:

`python operate_vending_machine.py`

### Assumptions:
- User can only be added by admin user
- `getitem` can be accessed without login
- Available user_type are `['admin', 'employee']`
- Available item_type are `['drink', 'snack']`

### Commands:

- `maxquantity, <max_quantity>` is used for initializing max quantity of each product type
- `costofeachitem, <cost_of_each_item>` is used for initializing cost of each product
- `login, <username>` used for login
- `logout` is used for logout
- `addcash` is used to add cash for user
- `getavailablecash` is used to fetch current cash balance of logged in user
- `getitem` to get list of all items, with ID
- `additem, <item_type> <item_quantity> <item_name>` is used to add item
- `increaseitem, <item_type> <item_id> <item_quantity>` is used to increase quantity of item
- `decreaseitem, <item_type> <item_id> <item_quantity>` is used to decrease quantity of item
- `deleteitem, <item_type> <item_id>` is used to delete item
- `buy, <item_type> <item_id> <item_quantity>` to purchase an available item
- `adduser, <user_type> <username>` is used to create user
- `getalluser` is used to get list of all user
- `deleteuser, <user_id>` is used to delete user


