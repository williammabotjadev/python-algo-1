# The decimal.Decimal module
from decimal import Decimal

print(sum(0.1 for i in range(10)) == 1.0)

print(sum(Decimal("0.1") for i in range(10)) == Decimal("1.0"))