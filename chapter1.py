from __future__ import division
from collections import Counter
from collections import defaultdict

# Data dump of users
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
    ]

# ID pairs (tuples)
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

########################## FINDING KEY CONNECTORS ##########################


# Add a list of friends to each other
for user in users:

    user["friends"] = []

# Populate the list
for i, j in friendships:

    users[i]["friends"].append(users[j]) # Add i as a friend of j
    users[j]["friends"].append(users[i])  # Add j as a friend of i

def number_of_friends(user):

    # How many friends does _user_ have?
    return len(user["friends"])     # Length of friend_ids list

total_connections = sum(number_of_friends(user) for user in users)      # 24

num_users = len(users)      # Length of the users list
avg_connections = total_connections / num_users     # 2.4

# Create a list
num_friends_by_id = [(user["id"], number_of_friends(user)) for users in users]

# Sort the list by num_friends, largest to smallest
#num_friends_by_id = sorted(num_friends_by_id, key = lambda (user_id, num_friends): num_friends, reverse = True)


################################ DATA SCIENTISTS YOU MAY KNOW ################################
def friends_of_friend_ids_bad(user):

    # For each of user's friends get _their_ friends
    return [foaf["id"] for friend in user["friends"] for foaf in friend["friends"]]

def not_the_same(user, other_user):

    # Two users are not the same if they have different ids
    return user["id"] != other_user["id"]

def not_friends(user, other_user):

    # Other_user is not a friend if he's not in user["friends"]; that is if he's not_the_same as all the people in user
    return all(not_the_same(friend, other_user) for friend in user["friends"])

def friend_of_friend_ids(user):
    # FOr each of my friends count their friends who aren't me and aren't my friends.
    return Counter(foaf["id"] for friend in user["friends"] for foaf in friend["friends"] if not_the_same(user, foaf) and not_friends(user, foaf))

def data_scientists_who_like(target_interest):

    return [user_id for user_id, user_interest in interests if user_interest == target_interest]

# Keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:

    user_ids_by_interest[interest].append(user_id)

# Keys are user_ids, values are lists of interest for that user_id
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:

    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):

    return Counter(interested_user_id for interest in interests_by_user_id[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest] if interests_by_user_id != user["id"])

################################ Salaries and Experience ################################

# Keys are years, values are lists of the salaries for each tenure
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:

    salary_by_tenure[tenure].append(salary)

# Keys are years, each value is average salary for that tenure
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

def tenure_bucket(tenure):

    if tenure < 2:

        return "Less than two"
    elif tenure < 5:

        return "Between two and five"
    else:

        return "More than five"

# Keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:

    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# Keys are years, each value is average salary for that tenure
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.iteritems()
}



# Test chapter one statements and functions
if __name__=="__main__":

    print("\n")
    print([friend["id"] for friend in users[0]["friends"]])        # [1,2]
    print([friend["id"] for friend in users[1]["friends"]])        # [0,2,3]
    print([friend["id"] for friend in users[2]["friends"]], "\n")        # [0,1,3]

    print(friend_of_friend_ids(users[3]))    # Counter({0:2, 5:1})