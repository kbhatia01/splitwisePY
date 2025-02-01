from splitwise.models import User, UserExpense, Expense, ExpenseType, UserExpenseType


class SplitwiseService:

    def settle_up_user(self, user_id):
        u =None
        try:
            u = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            print("User Doesnot exist")
            return None

        expesne_for_user = UserExpense.objects.filter(user=u)
        how_much_to_pay = self.calculate_txns()


        # add transaction in reverse to Expense and UserExpense
            # with type      SETTLE_UP_EXPENSE

        for exp in how_much_to_pay:
            e = Expense.objects.create(amount=exp.amount, group=exp.group,
                                   created_by=u, expense_type=ExpenseType.SETTLE_UP_EXPENSE)

            UserExpense.objects.create(
                user=u,
                amount=exp.amount,
                expense=e,
                created_by=u,
                ExpenseType=UserExpenseType.OWES_EXPENSE,
            )

            UserExpense.objects.create(
                user=u,
                amount=exp.amount,
                expense=e,
                created_by=exp.user,
                ExpenseType=UserExpenseType.PAID_EXPENSE,
            )




    def calculate_txns(self, Userexpense):
        # group by data... based on groups..
        # Simplify data..
            # find total using dict..

        pass





