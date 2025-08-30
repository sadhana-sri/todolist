checklist=[]
num_tasks=int(input("How many tasks do you want to add today?"))

for i in range(num_tasks):
    task=input(f"Enter task {i+1}:")
    checklist.append(task)

completed_tasks=[]
incomplete_tasks=[]

print("\n Now mark the completed tasks(yes/no):")
for task in checklist:
    status=input(f"Did you complete this task -{task}? (yes/no)")
    if status=='yes':
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)

print("\n Completed tasks:")
for task in completed_tasks:
    print("#"+task)

print("\n Incomplete tasks:")
for task in incomplete_tasks:
    print("#"+task)