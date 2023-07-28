import sys

if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")

    pre_apprx = float(input())

    for _ in range(4):
        cur_apprx = float(input())

        apprx_error = cur_apprx - pre_apprx

        pre_apprx = cur_apprx

        rel_apprx_error = (apprx_error / pre_apprx) * 100

        print("Approximate Error =", round(apprx_error, 3))
        print("Relative Approximate Error =", round(rel_apprx_error, 3), "\n")
