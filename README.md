# Budget App

###### Technologies:
<p align="center">
<img src="https://img.icons8.com/color/75/000000/python.png" width="75" height="75" alt="Python" style="margin: 10px 15px 0 15px;" />
</p>

### Try it!

To run the Budget App application, follow the instructions in the Setup section below.

## Project Structure

- `budget.py`: Contains the implementation of the `Category` class and the `create_spend_chart` function.

## Setup

### Prerequisites

- Python 3 installed

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/creinis/budget-app-fcc-scicomp-py-cert.git
   cd budget-app-fcc-scicomp-py-cert
   ```

2. Run the Budget App script:
   ```bash
   python3 budget.py
   ```

## Budget App

### Functionality

The Budget App allows you to manage different budget categories, such as food, clothing, and entertainment. You can deposit, withdraw, transfer funds between categories, and get the current balance of each category. The app also generates a bar chart representing the percentage spent in each category.

### Category Class

#### Methods

- `__init__(self, name)`: Initializes a new category with a name and an empty ledger.
- `__str__(self)`: Returns a string representation of the category, including all ledger entries and the total balance.
- `deposit(self, amount, description='')`: Adds a deposit entry to the ledger.
- `withdraw(self, amount, description='')`: Adds a withdrawal entry to the ledger if there are enough funds. Returns `True` if successful, `False` otherwise.
- `get_balance(self)`: Returns the current balance of the category.
- `transfer(self, amount, category)`: Transfers funds to another category if there are enough funds. Returns `True` if successful, `False` otherwise.
- `check_funds(self, amount)`: Checks if there are enough funds in the category. Returns `True` if there are enough funds, `False` otherwise.

### create_spend_chart Function

The `create_spend_chart` function generates a bar chart showing the percentage spent in each category. The chart includes a title, percentage labels, and the names of the categories.

### Practical Use Case

The Budget App helps users manage their finances by categorizing their spending and visualizing it in a bar chart. It is useful for tracking expenses, budgeting, and identifying spending patterns.

### Benefits

- **Organization:** Categorizes expenses and income for better financial management.
- **Visualization:** Provides a visual representation of spending percentages.
- **Python Standard Library:** Utilizes Python’s built-in data structures for implementation.

## How to Use

1. Create instances of the `Category` class for different budget categories.
2. Use the methods `deposit`, `withdraw`, and `transfer` to manage funds within and between categories.
3. Call the `create_spend_chart` function to generate a bar chart of spending percentages.

### Example Usage

```python
from budget import Category, create_spend_chart

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))
```

### Example Output

```plaintext
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96

***********Clothing***********
Transfer from Food        50.00
                        -25.55
                        -100.00
Total: -75.55

************Auto*************
initial deposit        1000.00
                        -15.00
Total: 985.00

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

### Function Parameters

- `categories`: A list of `Category` objects to be included in the spend chart.

### Constraints

- The `Category` class methods ensure that funds are managed correctly, preventing withdrawals and transfers if there are insufficient funds.

### Additional Information

- **Category Management:** Enables adding, withdrawing, and transferring funds with detailed descriptions.
- **Visualization:** Generates a clear and concise bar chart representing spending percentages.

---
#### This is a FreeCodeCamp Challenge for Scientific Computing with Python Projects Certification.
<p align="center">
<img src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg" width="250" height="75" alt="freeCodeCamp" style="margin: 0 15px; opacity: 0.6" />
</p>
