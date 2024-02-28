'''
-----------------------------------------------------------------------
File: pairwise_by_gpt4.py
Creation Time: Feb 27th 2024, 5:30 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''

# from itertools import combinations
# from more_itertools import roundrobin

# # Define the parameters and their possible values
# parameters = {
#     "Type of Phone": ["iPhone 14", "iPhone 13", "Galaxy Z", "Huawei Mate", "Google Pixel 7"],
#     "Authentication": ["Fingerprint", "Face recognition", "Text Password"],
#     "Connectivity": ["Wireless", "3G", "4G LTE", "5G Edge"],
#     "Memory": ["128 GB", "256 GB", "512 GB", "1 TB"],
#     "Battery Level": ["< 20 %", "20-39%", "40-59%", "60-79%", "80-100%"]
# }

# # Generate all possible pairs of parameters
# parameter_pairs = list(combinations(parameters.keys(), 2))

# # Function to generate pairwise combinations for each pair of parameters
# def generate_pairwise_combinations(param1, values1, param2, values2):
#     combinations = []
#     # Create a list of tuples for each combination of values from the two parameters
#     for value1 in values1:
#         for value2 in values2:
#             combinations.append({param1: value1, param2: value2})
#     return combinations

# # Generate pairwise combinations for all parameter pairs
# pairwise_combinations = []
# for pair in parameter_pairs:
#     param1, param2 = pair
#     combinations = generate_pairwise_combinations(param1, parameters[param1], param2, parameters[param2])
#     pairwise_combinations.append(combinations)

# # Merge the pairwise combinations into a minimal set of test cases
# # This involves selecting a combination for each pair such that all pairs are covered with minimal redundancy

# # Initialize a list to hold the final merged test cases
# test_cases = []

# # Function to merge combinations into test cases
# def merge_combinations(combinations_list):
#     # Start by adding the first combination of the first pair to the test cases
#     for combination in roundrobin(*combinations_list):
#         # For each combination, check if it can be merged into an existing test case
#         merged = False
#         for test_case in test_cases:
#             # Check if the combination can be merged into the current test case
#             if all(test_case.get(key) in [None, value] for key, value in combination.items()):
#                 # Merge the combination into the test case
#                 test_case.update(combination)
#                 merged = True
#                 break
#         # If the combination was not merged into any existing test case, add it as a new test case
#         if not merged:
#             test_cases.append(combination)

# # Merge the pairwise combinations into test cases
# merge_combinations(pairwise_combinations)

# # Convert the test cases into the desired JSON format
# test_cases_json = {"testCases": test_cases}

# with open("test_cases.json", "w") as file:
#     file.write(str(test_cases_json))


from itertools import product

# Define the parameters and their values
parameters = {
    "Type of Phone": ["iPhone 14", "iPhone 13", "Galaxy Z", "Huawei Mate", "Google Pixel 7"],
    "Authentication": ["Fingerprint", "Face recognition", "Text Password"],
    "Connectivity": ["Wireless", "3G", "4G LTE", "5G Edge"],
    "Memory": ["128 GB", "256 GB", "512 GB", "1 TB"],
    "Battery Level": ["< 20 %", "20-39%", "40-59%", "60-79%", "80-100%"]
}

# Generate all combinations of test cases
test_cases = list(product(*parameters.values()))

# Convert tuples to list format for easy reading
test_cases_formatted = [list(test_case) for test_case in test_cases]

with open("test_cases.txt", "w") as file:
    for test_case in test_cases_formatted:
        file.write(str(test_case) + "\n")
