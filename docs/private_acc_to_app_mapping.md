# Fields used in OTP statement
## In Ukrainian language

- Номер рахунку/картки (B1)
- Тип операції (B2)
- Дата здійснення операції (B3)
- Дата обробки операції в банку (B4)
- Опис операції (B5)
- Сума операції (B6)
- Валюта операції (B7)
- Сума операції в валюті рахунку (B8)
- Валюта рахунку (B9)
- Код категорії підприємства (B10)

## In Russian

**Won't be supported**

## In English

- Account/card number (B1)
- Transaction type (B2)
- Transaction date (B3)
- Date of transaction processing in the bank (B4)
- Transaction description (B5)
- Transaction amount (B6)
- Transaction currency (B7)
- Transaction amount in account currency (B8)
- Account currency (B9)
- Code of enterprise type (B10)

## Internal represenation

OTPSmart supports three languages. To determine the correct value, we have to 
check which one language is used inside the statement. Opposite way, we can
ignore the locale and map by indexes, but this is not the safe way if the
fields will change or get extended.

Each field from the bank's statement is marked with the index BX.


# Fields used in Gnucash

- Source Account (G1)
- Date (G2)
- Number (G3)
- Description (G4)
- Destination Account (G5)
- Value (G6)

# Notes

GNUCash supports double-way transactions: expenses are withdrawn from one
account and increase balance on another account. This feature is implemented 
within the script to map different activities to the corresponding accounts.

# Mapping

B1 -> G1
B3 -> G2 (excluding hours)
B3 -> G3 (including hours)
B5 -> G4
<internal mapping> -> G5 (an extra logic is here to determine different account usage)
B8, and consider B6 -> G6

