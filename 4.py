def calculation_monthly_payment(principal,annual_interest_rate,duration) :
    #monthly_interest_rate
    r = annual_interest_rate/1200
    #monthly payment for total duration of the loan
    n = duration*12
    if r==0 :
        monthly_payment = principal/n
    else :
        monthly_payment =(principal*(r*((1+r)**n)))/(((1+r)**n)-1)
    print(monthly_payment)

total_loan = float(input("meghdare kole vam ra vared namayid : "))
interest_rate = float(input("nerkhe bahre dar sal ra vared namayid : "))
total_years = float(input("tedade sal baraye pardakhte vam ra vared namayid : "))

calculation_monthly_payment(total_loan,interest_rate,total_years)
