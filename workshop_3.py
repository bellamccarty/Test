def bond_val_formula(cr, N, ytm, fv, freq):  # function to find a bond's pv using a formula
    # cr = annual coupon rate
    # N = number of years
    # ytm = yield to maturity or yield
    # fv = future value or par value
    # freq = frequency of coupon payments
    coupon = (cr / freq) * fv  # finds coupon payment value
    n_payments = N * freq  # finds number of times payment will be made
    pv_of_fv = fv / (1 + ytm) ** n_payments  # finds present value of the face value
    pv_of_coupons = (coupon) * (1 / ytm) * (1 - (1 / (1 + ytm) ** n_payments))
    present_value = pv_of_coupons + pv_of_fv  # adds coupons pv to fv pv
    return (present_value)  # returns the pv to the computer's memory


print(bond_val_formula(0.10, 10, 0.04, 1000, 2))  # calls the above function and prints its returned variable


def bond_val_pv(cr, N, ytm, fv, freq):  # function to find a bond's pv using iteration of a present value
    # cr = annual coupon rate
    # N = number of years
    # ytm = yield to maturity or yield
    # fv = future value or par value
    # freq = frequency of coupon payments
    coupon = (cr / freq) * fv  # finds coupon payment value
    n_payments = N * freq  # finds number of times payment will be made
    pv_of_fv = fv / (1 + ytm) ** n_payments  # finds present value of the face value
    pv_of_coupons = 0  # starts present value of coupons
    while n_payments > 0:  # iterates over each coupon payment to find pv and add to present value of all coupons
        temp = (coupon) / (1 + ytm) ** (n_payments)  # temporary coupon variable
        pv_of_coupons += temp  # adds temporary coupon to total of present value of all coupons
        n_payments -= 1  # decrements the payment number EX: if bond is 10y with payments every 6 months, will go from 20 to 19 to 18... to 0
    present_value = pv_of_coupons + pv_of_fv  # adds coupons pv to fv pv
    return present_value  # returns the pv to the computer's memory


print(bond_val_pv(0.10, 10, 0.04, 1000, 2))  # calls the above function and prints its returned variable


def bond_dur_pv(cr, N, ytm, fv, freq):  # function to find a bond's pv using iteration of a present value
    # cr = annual coupon rate
    # N = number of years
    # ytm = yield to maturity or yield
    # fv = future value or par value
    # freq = frequency of coupon payments
    coupon = (cr / freq) * fv  # finds coupon payment value
    n_payments = N * freq  # finds number of times payment will be made
    pv_of_fv = (fv + coupon) / ((1 + ytm) ** (n_payments))  # finds present value of the face value
    t_x_pv_of_fv = pv_of_fv * n_payments  # finds present value of the face value * t
    pv_of_coupons = 0  # starts present value of coupons
    t_x_pv_of_coupons = 0  # starts t * pv of coupons
    n_payments -= 1
    while n_payments > 0:  # iterates over each coupon payment to find pv and add to prresent value of all coupons
        temp = (coupon) / (1 + ytm) ** (n_payments)  # temporary coupon variable
        t_temp = temp * n_payments  # temporary coupon * t variable
        pv_of_coupons += temp  # adds temporary coupon to total of present value of all coupons
        t_x_pv_of_coupons += t_temp  # adds temporary coupon * t to total of present value of all coupons * t
        n_payments -= 1  # decrements the payment number EX: if bond is 10y with payments every 6 months,
        # will go from 20 to 19 to 18... to 0
    present_value = pv_of_coupons + pv_of_fv  # adds coupons pv to fv pv
    t_x_presesnt_value = t_x_pv_of_coupons + (t_x_pv_of_fv)  # adds coupons * t to pv to fv pv * t
    Dmac_Semi = t_x_presesnt_value / present_value  # calculates Dmac Semi
    Dmac_Ann = Dmac_Semi / 2  # Calculates Dmac Ann
    Dmod_Ann = Dmac_Ann / (1 + ytm)  # Calculates Dmod Ann
    return Dmod_Ann  # returns the pv to the computer's memory and pv*t


print(bond_dur_pv(0.025, 5, 0.010125, 100, 2))  # calls the above function and prints its
