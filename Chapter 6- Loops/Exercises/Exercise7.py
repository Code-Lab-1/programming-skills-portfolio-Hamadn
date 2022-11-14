# Creating a list and assigning it a variable(nums)
nums = [12, 75, 150, 180, 145, 525, 50]

# Loop for every item in nums
for i in nums:
# Checking if a value in nums is less than 500
    if i > 500:
# Break the  loop
        break
# Checking if a value is greater than 150(if the first condition is not fulfilled)
    elif i > 150:
# Continue the loop
        continue
# Checking if a value in the list is divisible by 5
    elif i % 5 == 0:
# Print the value
        print(i)