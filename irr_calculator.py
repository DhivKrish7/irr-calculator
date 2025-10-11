def npv(i, cashflows):
    return sum(cf / ((1 + i) ** t) for t, cf in enumerate(cashflows))


def irr_bisection(cashflows, lower=0.0, upper=1.0, tolerance=0.000001, max_iter=1000):
    npv_lower = npv(lower, cashflows)
    npv_upper = npv(upper, cashflows)

    if npv_lower * npv_upper > 0:
        raise ValueError("Your cashflows may not have an valid IRR")

    for p in range(max_iter):
        mid = (lower + upper) / 2
        npv_mid = npv(mid, cashflows)

        if abs(npv_mid) < tolerance:
            return mid

        if npv_lower * npv_mid < 0:
            upper = mid
            npv_upper = npv_mid
        else:
            lower = mid
            npv_lower = npv_mid

    raise RuntimeError("IRR did not converge within maximum iterations.")

if __name__ == "__main__":
    print("IRR Calculator using Bisection Method\n")
    print("--------------------------------------")

    print("Enter the series of cashflows separated by spaces (eg: -10000 3500 4252.56 3693.69)")
    user = input("Cashflows: ")

    try:
        cashflows = [float(x) for x in user.split()]
    except ValueError:
        print("Invalid input. Please enter only numbers separeted by spaces")
        exit(1)

    print(f"\nYour Cashflows: {cashflows}")

    try:
        irr = irr_bisection(cashflows)
        print(f'\nCalculated IRR: {irr * 100:.2f}%')
    except Exception as e:
        print(f"Error: {e}")