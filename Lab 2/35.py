def main():
    x_i = 50

    for i in range(15):
        f_x_i = x_i * x_i * x_i - x_i - 1
        d_f_x_i = 3 * x_i * x_i - 1
        x_i1 = x_i - f_x_i / d_f_x_i
        err = x_i1 - x_i
        re = err / x_i1

        print(f"i = {i}")
        print(f"xi = {x_i:.3f}")
        print(f"f(xi) = {f_x_i:.3f}")
        print(f"f'(xi) = {d_f_x_i:.3f}")
        print(f"xi+1 = {x_i1:.3f}")
        print(f"approx. error = {err:.3f}")
        print(f"rel. approx. error = {re:.3f}\n")

        x_i = x_i1


if __name__ == "__main__":
    main()
