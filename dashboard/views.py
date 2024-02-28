from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from expense.models import Expense

from income.models import Income

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def dashboard_api(request):
    total_income = 0
    total_expenses = 0
    try:
        incomes = Income.objects.all()
        total_income = sum(income.amount for income in incomes)
    except:
        pass
    
    try:
        expenses = Expense.objects.all()
        total_expenses = sum(expense.amount for expense in expenses)
    except:
        pass

    income_minus_expenses = total_income - total_expenses

    return Response({
        'total_income': total_income,
        'total_expenses': total_expenses,
        'income_minus_expenses': income_minus_expenses
    })
