#from GreenSeer import DEBUG_TOGGLE
DEBUG_TOGGLE = 1

class Taxes:
    """The Taxes class is responcible for handling all tax settings and methods.

    !!! All tax data used is from 2023, should be updated with time. !!!
    """

    # starting value for all brackets
    __FEDERAL_BRACKET_1 = 0
    __FEDERAL_BRACKET_2 = 11_000
    __FEDERAL_BRACKET_3 = 44_725
    __FEDERAL_BRACKET_4 = 95_375
    __FEDERAL_BRACKET_5 = 182_100
    __FEDERAL_BRACKET_6 = 231_250
    __FEDERAL_BRACKET_7 = 578_125
    # tax rate for all brackets
    __FEDERAL_RATE_1 = 10
    __FEDERAL_RATE_2 = 12
    __FEDERAL_RATE_3 = 22
    __FEDERAL_RATE_4 = 24
    __FEDERAL_RATE_5 = 32
    __FEDERAL_RATE_6 = 35
    __FEDERAL_RATE_7 = 37

    # using New Jersey tax brackets
    __STATE_BRACKET_1 = 0
    __STATE_BRACKET_2 = 20_000
    __STATE_BRACKET_3 = 35_000
    __STATE_BRACKET_4 = 40_000
    __STATE_BRACKET_5 = 75_000
    __STATE_BRACKET_6 = 500_000
    __STATE_BRACKET_7 = 1_000_000
    __STATE_RATE_1 = 1.4
    __STATE_RATE_2 = 1.75
    __STATE_RATE_3 = 3.5
    __STATE_RATE_4 = 5.525
    __STATE_RATE_5 = 6.37
    __STATE_RATE_6 = 8.97
    __STATE_RATE_7 = 10.75

    # social security is taxed at 6.2% up to 160,200 then no more
    __SOCIAL_BRACKET_1 = 0
    __SOCIAL_BRACKET_2 = 160_200
    __SOCIAL_RATE_1 = 6.2
    __SOCIAL_RATE_2 = 0

    # medicare is taxed at 1.45 until 200,000 then 2.35 after
    __MEDICARE_BRACKET_1 = 0
    __MEDICARE_BRACKET_2 = 200_000
    __MEDICARE_RATE_1 = 1.45
    __MEDICARE_RATE_2 = 2.35

    # New Jersey allows an exemption of 1000 in income from taxes, the federal governemnt used to allow this but has since gotten rid of it
    __FEDERAL_EXEMPTION = 0
    __STATE_EXEMPTION = 1_000

    # the federal government has a standard deduction if the indivdual does not opt for an itemized deduction, New Jersey has no standard deduction one must itemize if any
    __FEDERAL_DEDUCTION = 13_850
    __STATE_DEDUCTION = 0

    # state and local government SALT taxes are deductable up to 10,000 on federal taxes
    __SALT_DEDUCTION_CAP = 10_000

    @staticmethod
    def calculate_federal_tax(income, itemized_deduction):
        taxes = 0

        # determine and apply deduction and exemption
        income -= Taxes.__FEDERAL_EXEMPTION
        deduction = Taxes.__FEDERAL_DEDUCTION if Taxes.__FEDERAL_DEDUCTION > itemized_deduction else itemized_deduction
        income -= deduction

        # bracket 7
        if income > Taxes.__FEDERAL_BRACKET_7:
            taxes += (income - Taxes.__FEDERAL_BRACKET_7) * (Taxes.__FEDERAL_RATE_7 / 100)
            income = Taxes.__FEDERAL_BRACKET_7
        # bracket 6
        if income > Taxes.__FEDERAL_BRACKET_6:
            taxes += (income - Taxes.__FEDERAL_BRACKET_6) * (Taxes.__FEDERAL_RATE_6 / 100)
            income = Taxes.__FEDERAL_BRACKET_6
        # bracket 5
        if income > Taxes.__FEDERAL_BRACKET_5:
            taxes += (income - Taxes.__FEDERAL_BRACKET_5) * (Taxes.__FEDERAL_RATE_5 / 100)
            income = Taxes.__FEDERAL_BRACKET_5
        # bracket 4
        if income > Taxes.__FEDERAL_BRACKET_4:
            taxes += (income - Taxes.__FEDERAL_BRACKET_4) * (Taxes.__FEDERAL_RATE_4 / 100)
            income = Taxes.__FEDERAL_BRACKET_4
        # bracket 3
        if income > Taxes.__FEDERAL_BRACKET_3:
            taxes += (income - Taxes.__FEDERAL_BRACKET_3) * (Taxes.__FEDERAL_RATE_3 / 100)
            income = Taxes.__FEDERAL_BRACKET_3
        # bracket 2
        if income > Taxes.__FEDERAL_BRACKET_2:
            taxes += (income - Taxes.__FEDERAL_BRACKET_2) * (Taxes.__FEDERAL_RATE_2 / 100)
            income = Taxes.__FEDERAL_BRACKET_2
        # bracket 1
        if income > Taxes.__FEDERAL_BRACKET_1:
            taxes += (income - Taxes.__FEDERAL_BRACKET_1) * (Taxes.__FEDERAL_RATE_1 / 100)
            income = Taxes.__FEDERAL_BRACKET_1

        return taxes
    
    @staticmethod
    def calculate_state_tax(income, itemized_deduction):
        taxes = 0

        # apply 
        income -= Taxes.__STATE_EXEMPTION
        deduction = Taxes.__STATE_DEDUCTION if Taxes.__STATE_DEDUCTION > itemized_deduction else itemized_deduction
        income -= deduction

        # bracket 7
        if income > Taxes.__STATE_BRACKET_7:
            taxes += (income - Taxes.__STATE_BRACKET_7) * (Taxes.__STATE_RATE_7 / 100)
            income = Taxes.__STATE_BRACKET_7
        # bracket 6
        if income > Taxes.__STATE_BRACKET_6:
            taxes += (income - Taxes.__STATE_BRACKET_6) * (Taxes.__STATE_RATE_6 / 100)
            income = Taxes.__STATE_BRACKET_6
        # bracket 5
        if income > Taxes.__STATE_BRACKET_5:
            taxes += (income - Taxes.__STATE_BRACKET_5) * (Taxes.__STATE_RATE_5 / 100)
            income = Taxes.__STATE_BRACKET_5
        # bracket 4
        if income > Taxes.__STATE_BRACKET_4:
            taxes += (income - Taxes.__STATE_BRACKET_4) * (Taxes.__STATE_RATE_4 / 100)
            income = Taxes.__STATE_BRACKET_4
        # bracket 3
        if income > Taxes.__STATE_BRACKET_3:
            taxes += (income - Taxes.__STATE_BRACKET_3) * (Taxes.__STATE_RATE_3 / 100)
            income = Taxes.__STATE_BRACKET_3
        # bracket 2
        if income > Taxes.__STATE_BRACKET_2:
            taxes += (income - Taxes.__STATE_BRACKET_2) * (Taxes.__STATE_RATE_2 / 100)
            income = Taxes.__STATE_BRACKET_2
        # bracket 1
        if income > Taxes.__STATE_BRACKET_1:
            taxes += (income - Taxes.__STATE_BRACKET_1) * (Taxes.__STATE_RATE_1 / 100)
            income = Taxes.__STATE_BRACKET_1

        return taxes
    
    @staticmethod
    def calculate_fica_tax(income):
        taxes = 0

        # apply social taxes
        temp_income = income
        # bracket 2
        if temp_income > Taxes.__SOCIAL_BRACKET_2:
            taxes += (temp_income - Taxes.__SOCIAL_BRACKET_2) * (Taxes.__SOCIAL_RATE_2 / 100)
            temp_income = Taxes.__SOCIAL_BRACKET_2
        # bracket 2
        if temp_income > Taxes.__SOCIAL_BRACKET_1:
            taxes += (temp_income - Taxes.__SOCIAL_BRACKET_1) * (Taxes.__SOCIAL_RATE_1 / 100)
            temp_income = Taxes.__SOCIAL_BRACKET_1

        # apply medicare taxes
        temp_income = income
        # bracket 2
        if temp_income > Taxes.__MEDICARE_BRACKET_2:
            taxes += (temp_income - Taxes.__MEDICARE_BRACKET_2) * (Taxes.__MEDICARE_RATE_2 / 100)
            temp_income = Taxes.__MEDICARE_BRACKET_2
        # bracket 2
        if temp_income > Taxes.__MEDICARE_BRACKET_1:
            taxes += (temp_income - Taxes.__MEDICARE_BRACKET_1) * (Taxes.__MEDICARE_RATE_1 / 100)
            temp_income = Taxes.__MEDICARE_BRACKET_1

        return taxes
    
    @staticmethod
    def calculate_earned_income_tax(income, itemized_deduction, current_salt_deduction):
        """Calculates the taxes owed on income earned from a job.
        
        Taxes from a job have to pay FICA tax as well as the usual State and Federal.
        Maintains the current itemized deduction accounting for standard deductions and salt caps.
        
        @param income - The gross income made through a conventional job by the investor for the year.
        @param itemized_deduction - The investors itemized deduction before state tax for the year.
        @param current_salt_deduction - The current amount of state taxes through property etc. that are included in the itemized deduction.

        @return - The total amount of tax owed on the investors gross job income.
        """

        fica_taxes = Taxes.calculate_fica_tax(income)
        state_taxes = Taxes.calculate_state_tax(income, itemized_deduction)

        # add state tax to deduction keeping in mind salt cap
        itemized_deduction += state_taxes if current_salt_deduction + state_taxes <= Taxes.__SALT_DEDUCTION_CAP else Taxes.__SALT_DEDUCTION_CAP - current_salt_deduction

        federal_taxes = Taxes.calculate_federal_tax(income, itemized_deduction)

        if DEBUG_TOGGLE == 1:
            print(f"Federal: {federal_taxes}")
            print(f"FICA: {fica_taxes}")
            print(f"State: {state_taxes}")

        return fica_taxes + state_taxes + federal_taxes