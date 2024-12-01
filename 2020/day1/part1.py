target = 2020

with open("input.txt") as f:
    expenses = list(filter(None, f.read().split("\n")))

    for index, expense in enumerate(expenses):
        for other_expense in expenses[index:]:
            if int(expense) + int(other_expense) == 2020:
                print(
                    f"{expense} + {other_expense} = {int(expense)+int(other_expense)}"
                )
                print(
                    f"{expense} * {other_expense} = {int(expense)*int(other_expense)}"
                )
                break
