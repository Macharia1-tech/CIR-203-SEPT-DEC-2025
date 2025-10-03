
import numpy as np
transactions = np.array([
    [140, 235, 100, 180, 165, 200],  # Branch 1
    [290, 110, 260, 120, 120, 130],  # Branch 2
    [135, 260, 235, 105, 250, 260],  # Branch 3
    [200, 195, 170, 210, 160, 260]   # Branch 4
])

print("Transaction Volumes (4x6):\n", transactions)
total_per_branch = transactions.sum(axis=1)
print("\nTotal Transactions per Branch:\n", total_per_branch)
highest_branch = np.argmax(total_per_branch) + 1  
print("\nBranch with Highest Transactions: Branch", highest_branch)
average_monthly = transactions.mean(axis=0)
print("\nAverage Monthly Transaction Volume Across All Branches:\n", average_monthly)
reshaped = transactions.reshape(3, 8)
print("\nReshaped Array (3x8):\n", reshaped)
explanation = """
Reshaping does not change the total number of elements (4x6 = 24 elements).
It only changes how the data is structured. In this case, moving from 4 branches x 6 months 
to 3 rows x 8 columns breaks the original meaning:
- Rows no longer directly represent branches.
- Columns no longer directly represent months.
Reshaping is useful for mathematical operations, but in financial analysis, it can make 
data interpretation harder unless clearly defined.
"""
print(explanation)
