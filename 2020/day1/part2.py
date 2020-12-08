target = 2020

with open("day1.txt") as f:
    expenses = list(filter(None, f.read().split("\n")))

    for index, expense in enumerate(expenses):
        for second_index, second_expense in enumerate(expenses[index:]):
            for third_expense in expenses[second_index:]:
                if int(expense) + int(second_expense) + int(third_expense) == target:
                    print(
                        f"{expense} + {second_expense} + {third_expense} = {int(expense) + int(second_expense) + int(third_expense)}"
                    )
                    print(
                        f"{expense} * {second_expense} * {third_expense} = {int(expense)*int(second_expense)*int(third_expense)}"
                    )
                    break
