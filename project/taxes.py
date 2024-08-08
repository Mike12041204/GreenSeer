import common
from decimal import Decimal

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
    __STATE_BRACKET_1 = Decimal('0')
    __STATE_BRACKET_2 = Decimal('20_000')
    __STATE_BRACKET_3 = Decimal('35_000')
    __STATE_BRACKET_4 = Decimal('40_000')
    __STATE_BRACKET_5 = Decimal('75_000')
    __STATE_BRACKET_6 = Decimal('500_000')
    __STATE_BRACKET_7 = Decimal('1_000_000')
    # using Decimal class for state tax calculation for increased precision
    __STATE_RATE_1 = Decimal('1.4')
    __STATE_RATE_2 = Decimal('1.75')
    __STATE_RATE_3 = Decimal('3.5')
    __STATE_RATE_4 = Decimal('5.525')
    __STATE_RATE_5 = Decimal('6.37')
    __STATE_RATE_6 = Decimal('8.97')
    __STATE_RATE_7 = Decimal('10.75')

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

    # New Jersey allows an exemption of 1000 in income from taxes, the federal governemnt used to 
    # allow this but has since gotten rid of it
    __FEDERAL_EXEMPTION = 0
    __STATE_EXEMPTION = Decimal('1_000')

    # the federal government has a standard deduction if the indivdual does not opt for an itemized
    # deduction, New Jersey has no standard deduction one must itemize if any
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
    # New Jersey tax capital gains as normal income so they have no brackets

    # if you make over 200,000 a year you have to pay 3.8 on all investment gains above that
    __NIIT_THRESHOLD = 200_000
    __NIIT_RATE = 3.8

    @staticmethod
    def __federal_earned_income_tax(earned_income, deduction, exemption, investment_income) -> float:
        tax = 0
        income = earned_income + investment_income - exemption - deduction

        # bracket 7
        if income > Taxes.__FEDERAL_BRACKET_7:
            tax += (income - Taxes.__FEDERAL_BRACKET_7) * (Taxes.__FEDERAL_RATE_7 / 100)
            income = Taxes.__FEDERAL_BRACKET_7
        # bracket 6
        if income > Taxes.__FEDERAL_BRACKET_6:
            tax += (income - Taxes.__FEDERAL_BRACKET_6) * (Taxes.__FEDERAL_RATE_6 / 100)
            income = Taxes.__FEDERAL_BRACKET_6
        # bracket 5
        if income > Taxes.__FEDERAL_BRACKET_5:
            tax += (income - Taxes.__FEDERAL_BRACKET_5) * (Taxes.__FEDERAL_RATE_5 / 100)
            income = Taxes.__FEDERAL_BRACKET_5
        # bracket 4
        if income > Taxes.__FEDERAL_BRACKET_4:
            tax += (income - Taxes.__FEDERAL_BRACKET_4) * (Taxes.__FEDERAL_RATE_4 / 100)
            income = Taxes.__FEDERAL_BRACKET_4
        # bracket 3
        if income > Taxes.__FEDERAL_BRACKET_3:
            tax += (income - Taxes.__FEDERAL_BRACKET_3) * (Taxes.__FEDERAL_RATE_3 / 100)
            income = Taxes.__FEDERAL_BRACKET_3
        # bracket 2
        if income > Taxes.__FEDERAL_BRACKET_2:
            tax += (income - Taxes.__FEDERAL_BRACKET_2) * (Taxes.__FEDERAL_RATE_2 / 100)
            income = Taxes.__FEDERAL_BRACKET_2
        # bracket 1
        if income > Taxes.__FEDERAL_BRACKET_1:
            tax += (income - Taxes.__FEDERAL_BRACKET_1) * (Taxes.__FEDERAL_RATE_1 / 100)
            income = Taxes.__FEDERAL_BRACKET_1

        return tax
    
    @staticmethod
    def __state_tax(earned_income, ltcg, deduction, investment_income) -> float:
        tax = Decimal('0')
        income = (Decimal(earned_income) + Decimal(ltcg) + Decimal(investment_income) - 
                  Taxes.__STATE_EXEMPTION - Decimal(deduction))

        # bracket 7
        if income > Taxes.__STATE_BRACKET_7:
            tax += (income - Taxes.__STATE_BRACKET_7) * (Taxes.__STATE_RATE_7 / Decimal('100'))
            income = Taxes.__STATE_BRACKET_7
        # bracket 6
        if income > Taxes.__STATE_BRACKET_6:
            tax += (income - Taxes.__STATE_BRACKET_6) * (Taxes.__STATE_RATE_6 / Decimal('100'))
            income = Taxes.__STATE_BRACKET_6
        # bracket 5
        if income > Taxes.__STATE_BRACKET_5:
            tax += (income - Taxes.__STATE_BRACKET_5) * (Taxes.__STATE_RATE_5 / Decimal('100'))
            income = Taxes.__STATE_BRACKET_5
        # bracket 4
        if income > Taxes.__STATE_BRACKET_4:
            tax += (income - Taxes.__STATE_BRACKET_4) * (Taxes.__STATE_RATE_4 / Decimal('100'))
            income = Taxes.__STATE_BRACKET_4
        # bracket 3
        if income > Taxes.__STATE_BRACKET_3:
            tax += (income - Taxes.__STATE_BRACKET_3) * (Taxes.__STATE_RATE_3 / Decimal('100'))
            income = Taxes.__STATE_BRACKET_3
        # bracket 2
        if income > Taxes.__STATE_BRACKET_2:
            tax += (income - Taxes.__STATE_BRACKET_2) * (Taxes.__STATE_RATE_2 / Decimal('100'))
            income = Taxes.__STATE_BRACKET_2
        # bracket 1
        if income > Taxes.__STATE_BRACKET_1:
            tax += (income - Taxes.__STATE_BRACKET_1) * (Taxes.__STATE_RATE_1 / Decimal('100'))
            income = Taxes.__STATE_BRACKET_1

        return float(tax)
    
    @staticmethod
    def __fica_tax(earned_income) -> float:
        tax = 0
        income = earned_income

        # apply social tax
        temp_income = income
        # bracket 2
        if temp_income > Taxes.__SOCIAL_BRACKET_2:
            tax += (temp_income - Taxes.__SOCIAL_BRACKET_2) * (Taxes.__SOCIAL_RATE_2 / 100)
            temp_income = Taxes.__SOCIAL_BRACKET_2
        # bracket 1
        if temp_income > Taxes.__SOCIAL_BRACKET_1:
            tax += (temp_income - Taxes.__SOCIAL_BRACKET_1) * (Taxes.__SOCIAL_RATE_1 / 100)
            temp_income = Taxes.__SOCIAL_BRACKET_1

        # apply medicare tax
        temp_income = income
        # bracket 2
        if temp_income > Taxes.__MEDICARE_BRACKET_2:
            tax += (temp_income - Taxes.__MEDICARE_BRACKET_2) * (Taxes.__MEDICARE_RATE_2 / 100)
            temp_income = Taxes.__MEDICARE_BRACKET_2
        # bracket 1
        if temp_income > Taxes.__MEDICARE_BRACKET_1:
            tax += (temp_income - Taxes.__MEDICARE_BRACKET_1) * (Taxes.__MEDICARE_RATE_1 / 100)
            temp_income = Taxes.__MEDICARE_BRACKET_1

        return tax
    
    @staticmethod
    def __federal_ltcg_tax(earned_income, ltcg, deduction, exemption, investment_income) -> float:
        tax = 0
        income = earned_income + ltcg + investment_income -exemption - deduction

        # bracket 3
        if income > Taxes.__FEDERAL_LTCG_BRACKET_3:
            ltcg_above = min(ltcg, income - Taxes.__FEDERAL_LTCG_BRACKET_3)
            tax += ltcg_above * (Taxes.__FEDERAL_LTCG_RATE_3 / 100)
            ltcg -= ltcg_above
            income -= ltcg_above
        # bracket 2
        if income > Taxes.__FEDERAL_LTCG_BRACKET_2:
            ltcg_above = min(ltcg, income - Taxes.__FEDERAL_LTCG_BRACKET_2)
            tax += ltcg_above * (Taxes.__FEDERAL_LTCG_RATE_2 / 100)
            ltcg -= ltcg_above
            income -= ltcg_above
        # bracket 1
        if income > Taxes.__FEDERAL_LTCG_BRACKET_1:
            ltcg_above = min(ltcg, income - Taxes.__FEDERAL_LTCG_BRACKET_1)
            tax += ltcg_above * (Taxes.__FEDERAL_LTCG_RATE_1 / 100)
            ltcg -= ltcg_above
            income -= ltcg_above

        return tax

    @staticmethod
    def __niit_tax(earned_income, ltcg, investment_income) -> float:
        """TODO
        """

        tax = 0
        net_investment_income = ltcg + investment_income
        income = earned_income + net_investment_income

        niit_applicable = min(net_investment_income, max(0, income - Taxes.__NIIT_THRESHOLD))
        tax += niit_applicable * (Taxes.__NIIT_RATE / 100)

        return tax
    
    @staticmethod
    def calculate_tax(earned_income, itemized_deduction, ltcg, current_salt_deduction, 
                      investment_income) -> float:
        # to determine whether a standard or itemized deduction would be better we run both and 
        # choose the lesser

        # ITEMIZED DEDUCTION
        itemized_tax = 0
        itemized_exemption = Taxes.__FEDERAL_EXEMPTION

        # fica tax on income earned from a job
        itemized_fica = Taxes.__fica_tax(earned_income)
        itemized_tax += itemized_fica

        # DEBUG - save original information
        d_i_d_s = itemized_deduction

        # state tax, which are deductable up to salt cap, and apply to capital gains as well
        itemized_state = Taxes.__state_tax(earned_income, ltcg, itemized_deduction, 
                                           investment_income)
        itemized_deduction += min(itemized_state, Taxes.__SALT_DEDUCTION_CAP - 
                                  current_salt_deduction)
        itemized_tax += itemized_state

        # DEBUG - save original information
        d_i_d_f = itemized_deduction
        d_i_e_f = itemized_exemption

        # federal earned income tax
        itemized_federal = Taxes.__federal_earned_income_tax(earned_income, itemized_deduction, 
                                                             itemized_exemption, investment_income)
        itemized_deduction = max(0, itemized_deduction - earned_income)
        itemized_exemption = max(0, itemized_exemption - earned_income)
        itemized_tax += itemized_federal

        # DEBUG - save original information
        d_i_d_l = itemized_deduction
        d_i_e_l = itemized_exemption

        # federal capital gains tax on top of earned income
        itemized_ltcg = Taxes.__federal_ltcg_tax(earned_income, ltcg, itemized_deduction, 
                                                 itemized_exemption, investment_income)
        itemized_tax += itemized_ltcg
        
        # niit tax apply seperately to investment income
        itemized_niit = Taxes.__niit_tax(earned_income, ltcg, investment_income)
        itemized_tax += itemized_niit

        # STANDARD DEDUCTION
        standard_tax = 0
        standard_deduction = Taxes.__FEDERAL_DEDUCTION
        standard_exemption = Taxes.__FEDERAL_EXEMPTION

        # fica tax on income earned from a job
        standard_fica = Taxes.__fica_tax(earned_income)
        standard_tax += standard_fica

        # state tax, which are deductable up to salt cap, and apply to capital gains as well
        standard_state = Taxes.__state_tax(earned_income, ltcg, Taxes.__STATE_DEDUCTION, 
                                           investment_income)
        standard_tax += standard_state

        # federal earned income tax
        standard_federal = Taxes.__federal_earned_income_tax(earned_income, standard_deduction, 
                                                             standard_exemption, investment_income)
        standard_deduction = max(0, standard_deduction - earned_income)
        standard_exemption = max(0, standard_exemption - earned_income)
        standard_tax += standard_federal

        # DEBUG - save original information
        d_s_d_l = standard_deduction
        d_s_e_l = standard_exemption

        # federal capital gains tax on top of earned income
        standard_ltcg = Taxes.__federal_ltcg_tax(earned_income, ltcg, standard_deduction, 
                                                 standard_exemption, investment_income)
        standard_tax += standard_ltcg

        # niit tax apply seperately to investment income
        standard_niit = Taxes.__niit_tax(earned_income, ltcg, investment_income)
        standard_tax += standard_niit

        # DEBUG - print tax breakdown
        if common.DEBUG_TOGGLE == 1:

            # case itemized
            if itemized_tax < standard_tax:
                deduction = 'Itemized'
                federal_tax = itemized_federal
                state_tax = itemized_state
                fica_tax = itemized_fica
                ltcg_tax = itemized_ltcg
                niit_tax = itemized_niit

                state_e_i = Taxes.__state_tax(earned_income, 0, d_i_d_s, investment_income)
                state_earned = Taxes.__state_tax(earned_income, 0, d_i_d_s, 0)
                state_investment = state_e_i - state_earned
                state_ltcg = state_tax - state_e_i

                federal_earned = Taxes.__federal_earned_income_tax(earned_income, d_i_d_f, 
                                                                   d_i_e_f, 0)
                federal_investment = federal_tax - federal_earned

                niit_investment = Taxes.__niit_tax(earned_income, 0, investment_income)
                niit_ltcg = niit_tax - niit_investment
            # case standard
            else:
                deduction = 'Standard'
                federal_tax = standard_federal
                state_tax = standard_state
                fica_tax = standard_fica
                ltcg_tax = standard_ltcg
                niit_tax = standard_niit

                state_e_i = Taxes.__state_tax(earned_income, 0, Taxes.__STATE_DEDUCTION, 
                                              investment_income)
                state_earned = Taxes.__state_tax(earned_income, 0, Taxes.__STATE_DEDUCTION, 0)
                state_investment = state_e_i - state_earned
                state_ltcg = state_tax - state_e_i

                federal_earned = Taxes.__federal_earned_income_tax(earned_income, 
                                                                   Taxes.__FEDERAL_DEDUCTION, 
                                                                   Taxes.__FEDERAL_EXEMPTION, 0)
                federal_investment = federal_tax - federal_earned

                niit_investment = Taxes.__niit_tax(earned_income, 0, investment_income)
                niit_ltcg = niit_tax - niit_investment

            print(f"Deduction: {deduction}")
            print("Earned Income:")
            print(f"   Federal - {common.fa(federal_earned)}")
            print(f"   State   - {common.fa(state_earned)}")
            print(f"   FICA    - {common.fa(fica_tax)}")
            print(f"   Total   - {common.fa(federal_earned + state_earned + fica_tax)}")
            print("Investment Income:")
            print(f"   Federal - {common.fa(federal_investment)}")
            print(f"   State   - {common.fa(state_investment)}")
            print(f"   NIIT    - {common.fa(niit_investment)}")
            print(f"   Total   - " +
                  f"{common.fa(federal_investment + state_investment + niit_investment)}")
            print("Long Term Capital Gains:")
            print(f"   LTCG    - {common.fa(ltcg_tax)}")
            print(f"   State   - {common.fa(state_ltcg)}")
            print(f"   NIIT    - {common.fa(niit_ltcg)}")
            print(f"   Total   - {common.fa(ltcg_tax + state_ltcg + niit_ltcg)}")
            print("Summary:")
            print(f"   Federal - {common.fa(federal_tax)}")
            print(f"   State   - {common.fa(state_tax)}")
            print(f"   LTCG    - {common.fa(ltcg_tax)}")
            print(f"   FICA    - {common.fa(fica_tax)}")
            print(f"   NIIT    - {common.fa(niit_tax)}")
            print(f"   Total   - " + 
                  f"{common.fa(federal_tax + state_tax + ltcg_tax + fica_tax + niit_tax)}")
            
        return min(itemized_tax, standard_tax)