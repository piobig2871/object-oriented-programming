#!/usr/bin/python3

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from collections import namedtuple

MyExpance = namedtuple('F', ['type_', 'amount'])


def summarize_expances(min_amount, alist):
    expenses = {}
    for expense in alist:
        if expense.amount >= min_amount:
            if expense.type_ not in expenses:
                expenses[expense.type_] = 0
            expenses[expense.type_] = expenses[expense.type_] + expense.amount

    for (type_, amount) in sorted(expenses.items(), key=lambda e: e[1]):
        print(type_, amount)
