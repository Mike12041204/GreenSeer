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

    # federal long term capital gains tax
    __FEDERAL_LTCG_BRACKET_1 = 0
    __FEDERAL_LTCG_BRACKET_2 = 44_625
    __FEDERAL_LTCG_BRACKET_3 = 429_300
    __FEDERAL_LTCG_RATE_1 = 0
    __FEDERAL_LTCG_RATE_2 = 15
    __FEDERAL_LTCG_RATE_3 = 20
    # New Jersey taxes capital gains as normal income so they have no brackets

    # if you make over 200,000 a year you have to pay 3.8 on all investment gains above that
    __NIIT_THRESHOLD = 200_000
    __NIIT_RATE = 3.8

    @staticmethod
    def __federal_earned_income_tax(earned_income, deduction):
        taxes = 0
        income = earned_income

        # determine and apply deduction and exemption
        income -= Taxes.__FEDERAL_EXEMPTION
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
    def __state_tax(earned_income, long_term_capital_gains, deduction):
        taxes = 0
        income = earned_income + long_term_capital_gains

        # apply deductions and state exemption
        income -= Taxes.__STATE_EXEMPTION
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
    def __fica_tax(earned_income):
        taxes = 0
        income = earned_income

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
    
    # CURSOR - doesnt work, refactor Taxes to use min and max methods
    @staticmethod
    def __federal_long_term_capital_gains_tax(earned_income, long_term_capital_gains, deduction):
        taxes = 0
        income = earned_income + long_term_capital_gains

        income -= Taxes.__FEDERAL_EXEMPTION
        income -= deduction

        # bracket 3
        if income > Taxes.__FEDERAL_LTCG_BRACKET_3:
            ltcg_above = income - Taxes.__FEDERAL_LTCG_BRACKET_3 if long_term_capital_gains >= income - Taxes.__FEDERAL_LTCG_BRACKET_3 else long_term_capital_gains
            taxes += ltcg_above * (Taxes.__FEDERAL_LTCG_RATE_3 / 100)
            long_term_capital_gains -= ltcg_above
            income -= ltcg_above
        # bracket 2
        if income > Taxes.__FEDERAL_LTCG_BRACKET_2:
            ltcg_above = income - Taxes.__FEDERAL_LTCG_BRACKET_2 if long_term_capital_gains >= income - Taxes.__FEDERAL_LTCG_BRACKET_2 else long_term_capital_gains
            taxes += ltcg_above * (Taxes.__FEDERAL_LTCG_RATE_2 / 100)
            long_term_capital_gains -= ltcg_above
            income -= ltcg_above
        # bracket 1
        if income > Taxes.__FEDERAL_LTCG_BRACKET_1:
            ltcg_above = income - Taxes.__FEDERAL_LTCG_BRACKET_1 if long_term_capital_gains >= income - Taxes.__FEDERAL_LTCG_BRACKET_1 else long_term_capital_gains
            taxes += ltcg_above * (Taxes.__FEDERAL_LTCG_RATE_1 / 100)
            long_term_capital_gains -= ltcg_above
            income -= ltcg_above

        return taxes

    @staticmethod
    def __niit_tax(earned_income, long_term_capital_gains):
        """TODO
        """

        taxes = 0
        income = earned_income + long_term_capital_gains

        niit_applicable = long_term_capital_gains if earned_income >= Taxes.__NIIT_THRESHOLD else income - Taxes.__NIIT_THRESHOLD
        taxes += niit_applicable * (Taxes.__NIIT_RATE / 100)

        return taxes
    
    @staticmethod
    def calculate_tax(earned_income, long_term_capital_gains, itemized_deduction, current_salt_deduction):
        """TODO
        """

        # to determine whether a standard or itemized deduction would be better we run both and choose the lesser

        itemized_taxes = 0

        # fica taxes on income earned from a job
        itemized_taxes += Taxes.__fica_tax(earned_income)

        # state taxes, which are deductable up to salt cap, and apply to capital gains as well
        state_taxes = Taxes.__state_tax(earned_income, long_term_capital_gains, itemized_deduction)
        itemized_deduction += state_taxes if current_salt_deduction + itemized_deduction <= Taxes.__SALT_DEDUCTION_CAP else Taxes.__SALT_DEDUCTION_CAP - current_salt_deduction
        itemized_taxes += state_taxes

        # federal earned income tax
        itemized_taxes += Taxes.__federal_earned_income_tax(earned_income, itemized_deduction)
        itemized_deduction = 0 if itemized_deduction <= earned_income else itemized_deduction - earned_income

        # federal capital gains tax on top of earned income
        itemized_taxes += Taxes.__federal_long_term_capital_gains_tax(earned_income, long_term_capital_gains, itemized_deduction)
        itemized_taxes += Taxes.__niit_tax(earned_income, long_term_capital_gains)

        standard_taxes = 0
        standard_deduction = Taxes.__FEDERAL_DEDUCTION

        # fica taxes on income earned from a job
        standard_taxes += Taxes.__fica_tax(earned_income)

        # state taxes, which are deductable up to salt cap, and apply to capital gains as well
        state_taxes = Taxes.__state_tax(earned_income, long_term_capital_gains, standard_deduction)
        standard_taxes += state_taxes

        # federal earned income tax
        standard_taxes += Taxes.__federal_earned_income_tax(earned_income, standard_deduction)
        standard_deduction = 0 if standard_deduction <= earned_income else standard_deduction - earned_income

        # federal capital gains tax on top of earned income
        standard_taxes += Taxes.__federal_long_term_capital_gains_tax(earned_income, long_term_capital_gains, standard_deduction)
        standard_taxes += Taxes.__niit_tax(earned_income, long_term_capital_gains)

        return itemized_taxes if itemized_taxes < standard_taxes else standard_taxes