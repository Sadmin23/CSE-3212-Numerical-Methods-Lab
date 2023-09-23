import matplotlib.pyplot as plt
from prettytable import PrettyTable

apprxf = []
apprxb = []
apprxc = []
h_val = []
real = []
true_errorf = []
true_errorb = []
true_errorc = []
rel_truef = []
rel_trueb = []
rel_truec = []
apprx_errf = []
apprx_errb = []
apprx_errc = []
rel_apprxf = []
rel_apprxb = []
rel_apprxc = []


def fx(x):
    return x * x * x + 3 * x


def dfx(x):
    return 3 * x * x + 3


def central(x, h):
    f0 = fx(x)
    real_val = dfx(x)

    while h >= 0.01:
        fi1p = fx(x + h)
        fi1n = fx(x - h)
        ans = (fi1p - fi1n) / (2 * h)

        if h != 10:
            ae = abs(ans - ans0)
            rae = ae / ans

            apprx_errc.append(ae)
            rel_apprxc.append(rae)

        te = abs(real_val - ans)
        rete = te / real_val

        apprxc.append(ans)
        true_errorc.append(te)
        rel_truec.append(rete)

        # print(f"h={h} {ans}\n")
        h -= 0.01
        ans0 = ans


def backward(x, h):
    f0 = fx(x)
    real_val = dfx(x)

    while h >= 0.01:
        fi1 = fx(x - h)
        ans = (f0 - fi1) / h

        if h != 10:
            ae = abs(ans - ans0)
            rae = ae / ans

            apprx_errb.append(ae)
            rel_apprxb.append(rae)

        te = abs(real_val - ans)
        rete = te / real_val

        apprxb.append(ans)
        true_errorb.append(te)
        rel_trueb.append(rete)

        # print(f"h={h} {ans}\n")
        h -= 0.01
        ans0 = ans


def forward(x, h):
    f0 = fx(x)
    real_val = dfx(x)

    while h >= 0.01:
        fi1 = fx(x + h)
        ans = (fi1 - f0) / h

        if h != 10:
            ae = abs(ans - ans0)
            rae = ae / ans

            apprx_errf.append(ae)
            rel_apprxf.append(rae)

        te = abs(real_val - ans)
        rete = te / real_val

        apprxf.append(ans)
        h_val.append(h)
        real.append(real_val)
        true_errorf.append(te)
        rel_truef.append(rete)

        # print(f"h={h} {ans}\n")
        h -= 0.01
        ans0 = ans


if __name__ == "__main__":
    #    x = int(input("Enter the value of x: "))
    x = 3

    print(f"real value={dfx(x)}\n")

    forward(x, 10)
    backward(x, 10)
    central(x, 10)

    x = PrettyTable()

    x.add_column("h", h_val)
    x.add_column("d(f(x))", real)
    x.add_column("Forward Approx.", apprxf)
    x.add_column("Backward Approx.", apprxb)
    x.add_column("Central Approx.", apprxc)

    print(x)

    plt.plot(h_val, apprxf, label="Forward")
    plt.plot(h_val, apprxb, label="Backward")
    plt.plot(h_val, apprxc, label="Central")
    plt.plot(h_val, real, label="True Value")
    plt.xlabel("Value of h")
    plt.ylabel("Approx. Value")
    plt.title("Approximate values of all methods")
    plt.legend()
    plt.show()

    plt.plot(h_val, true_errorf, label="Forward")
    plt.plot(h_val, true_errorb, label="Backward")
    plt.plot(h_val, true_errorc, label="Central")
    plt.xlabel("Value of h")
    plt.ylabel("True Error")
    plt.title("True error values of all methods")
    plt.legend()
    plt.show()

    plt.plot(h_val, rel_truef, label="Forward")
    plt.plot(h_val, rel_trueb, label="Backward")
    plt.plot(h_val, rel_truec, label="Central")
    plt.xlabel("Value of h")
    plt.ylabel("Rel. True Error")
    plt.title("Relative True error values of all methods")
    plt.legend()
    plt.show()

    h_val.pop(10)

    plt.plot(h_val, apprx_errf, label="Forward")
    plt.plot(h_val, apprx_errb, label="Backward")
    plt.plot(h_val, apprx_errc, label="Central")
    plt.xlabel("Value of h")
    plt.ylabel("Approx. Error")
    plt.title("Approx. error values of all methods")
    plt.legend()
    plt.show()

    plt.plot(h_val, rel_apprxf, label="Forward")
    plt.plot(h_val, rel_apprxb, label="Backward")
    plt.plot(h_val, rel_apprxc, label="Central")
    plt.xlabel("Value of h")
    plt.ylabel("Rel. Approx. Error")
    plt.title("Rel. Approx. error values of all methods")
    plt.legend()
    plt.show()
