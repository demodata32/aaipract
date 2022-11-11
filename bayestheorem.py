def are_drug_users(n, users_of_drug):
    m = 1-n
    non_users_of_drug = 1 - users_of_drug
    return (n * users_of_drug)/(n * users_of_drug + m * non_users_of_drug)

print(are_drug_users(0.99,0.005))
