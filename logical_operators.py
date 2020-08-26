has_high_income = False
has_good_credit = True
#logical 'and' operator: both conditions should be True
#logical 'or' operator: At least one condition should be true
if has_high_income or has_good_credit:
    print("Eligibled for Loan")

has_nice_credit = True
has_criminal_record = True

if has_nice_credit and not has_criminal_record:
    print("Eligible for loan")