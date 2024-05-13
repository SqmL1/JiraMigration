import random
from datetime import datetime, timedelta

# Define some helper functions
def random_date(start_date=datetime(2023, 1, 1), end_date=datetime.today()):
  """Returns a random date between the specified start and end dates."""
  time_between_dates = end_date - start_date
  days_until_random_date = random.randrange(time_between_dates.days)
  return start_date + timedelta(days=days_until_random_date)

def random_status():
  """Returns a random Jira issue status."""
  statuses = ["To Do", "In Progress", "Done", "In Review", "Blocked"]
  return random.choice(statuses)

def random_priority():
  """Returns a random Jira issue priority."""
  priorities = ["Highest", "High", "Medium", "Low", "Lowest"]
  return random.choice(priorities)

# Define some common Jira issue types
issue_types = ["Task", "Bug", "Story", "Sub-task"]

# Generate user data
users = [f"User {i+1}" for i in range(10)]

# Generate sample Jira data
data = []
for user in users:
  # Generate a random number of tickets between 1 and 5 for each user
  num_tickets = random.randint(1, 5)
  for i in range(num_tickets):
    # Create a new row of data
    data.append({
      "User": user,
      "Issue Key": f"JIRA-{random.randint(1000, 9999)}",
      "Summary": f"Sample summary for ticket {i+1} by {user}",
      "Issue Type": random.choice(issue_types),
      "Status": random_status(),
      "Priority": random_priority(),
      "Reporter": random.choice(users),
      "Created": random_date().strftime('%Y-%m-%d'),
      "Updated": random_date(start_date=random_date()).strftime('%Y-%m-%d')
    })

# Print the data
for row in data:
  print(row)