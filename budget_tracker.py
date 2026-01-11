import json
import os
from datetime import datetime
from collections import defaultdict

class BudgetTracker:
    def __init__(self, filename='budget_data.json'):
        self.filename = filename
        self.transactions = []
        self.categories = ['Food', 'Transportation', 'Entertainment', 'Utilities', 
                          'Shopping', 'Healthcare', 'Education', 'Other']
        self.load_data()
    
    def load_data(self):
        """Load existing budget data from file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.transactions = json.load(f)
                print(f"Loaded {len(self.transactions)} transactions.")
            except:
                print("Error loading data. Starting fresh.")
                self.transactions = []
        else:
            print("No existing data found. Starting fresh.")
    
    def save_data(self):
        """Save budget data to file"""
        with open(self.filename, 'w') as f:
            json.dump(self.transactions, f, indent=2)
        print("Data saved successfully!")
    
    def add_transaction(self):
        """Add a new income or expense transaction"""
        print("\n--- Add Transaction ---")
        
        # Get transaction type
        while True:
            trans_type = input("Type (income/expense): ").lower()
            if trans_type in ['income', 'expense']:
                break
            print("Please enter 'income' or 'expense'")
        
        # Get amount
        while True:
            try:
                amount = float(input("Amount: "))
                if amount > 0:
                    break
                print("Amount must be positive!")
            except ValueError:
                print("Please enter a valid number!")
        
        # Get category (only for expenses)
        category = None
        if trans_type == 'expense':
            print("\nCategories:")
            for i, cat in enumerate(self.categories, 1):
                print(f"{i}. {cat}")
            
            while True:
                try:
                    choice = int(input("Select category (1-8): "))
                    if 1 <= choice <= len(self.categories):
                        category = self.categories[choice - 1]
                        break
                    print(f"Please enter a number between 1 and {len(self.categories)}")
                except ValueError:
                    print("Please enter a valid number!")
        else:
            category = "Income"
        
        # Get description
        description = input("Description: ").strip()
        if not description:
            description = category
        
        # Create transaction
        transaction = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'type': trans_type,
            'amount': amount,
            'category': category,
            'description': description
        }
        
        self.transactions.append(transaction)
        print(f"\n✓ {trans_type.capitalize()} of ${amount:.2f} added successfully!")
    
    def view_transactions(self):
        """Display all transactions"""
        if not self.transactions:
            print("\nNo transactions found!")
            return
        
        print("\n" + "="*80)
        print(f"{'Date':<20} {'Type':<10} {'Category':<15} {'Description':<20} {'Amount':>10}")
        print("="*80)
        
        for trans in self.transactions:
            amount_str = f"${trans['amount']:,.2f}"
            if trans['type'] == 'expense':
                amount_str = f"-{amount_str}"
            else:
                amount_str = f"+{amount_str}"
            
            print(f"{trans['date']:<20} {trans['type']:<10} {trans['category']:<15} "
                  f"{trans['description'][:20]:<20} {amount_str:>10}")
        print("="*80)
    
    def view_summary(self):
        """Display budget summary"""
        if not self.transactions:
            print("\nNo transactions to summarize!")
            return
        
        total_income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        total_expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        balance = total_income - total_expenses
        
        # Category breakdown
        category_totals = defaultdict(float)
        for trans in self.transactions:
            if trans['type'] == 'expense':
                category_totals[trans['category']] += trans['amount']
        
        print("\n" + "="*50)
        print("BUDGET SUMMARY")
        print("="*50)
        print(f"Total Income:     ${total_income:>12,.2f}")
        print(f"Total Expenses:   ${total_expenses:>12,.2f}")
        print("-" * 50)
        print(f"Balance:          ${balance:>12,.2f}")
        print("="*50)
        
        if category_totals:
            print("\nExpenses by Category:")
            print("-" * 50)
            for category, amount in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
                percentage = (amount / total_expenses * 100) if total_expenses > 0 else 0
                print(f"{category:<20} ${amount:>10,.2f}  ({percentage:>5.1f}%)")
            print("="*50)
    
    def delete_transaction(self):
        """Delete a transaction"""
        if not self.transactions:
            print("\nNo transactions to delete!")
            return
        
        self.view_transactions()
        
        print(f"\nEnter transaction number to delete (1-{len(self.transactions)}), or 0 to cancel:")
        try:
            choice = int(input("Choice: "))
            if choice == 0:
                print("Deletion cancelled.")
                return
            if 1 <= choice <= len(self.transactions):
                deleted = self.transactions.pop(choice - 1)
                print(f"\n✓ Deleted: {deleted['description']} - ${deleted['amount']:.2f}")
            else:
                print("Invalid transaction number!")
        except ValueError:
            print("Please enter a valid number!")
    
    def run(self):
        """Main application loop"""
        print("\n" + "="*50)
        print("  PERSONAL BUDGET TRACKER")
        print("="*50)
        
        while True:
            print("\n--- Main Menu ---")
            print("1. Add Transaction")
            print("2. View All Transactions")
            print("3. View Summary")
            print("4. Delete Transaction")
            print("5. Save & Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                self.add_transaction()
            elif choice == '2':
                self.view_transactions()
            elif choice == '3':
                self.view_summary()
            elif choice == '4':
                self.delete_transaction()
            elif choice == '5':
                self.save_data()
                print("\nThank you for using Budget Tracker. Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    tracker = BudgetTracker()
    tracker.run()