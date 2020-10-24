def format_float(v):
    s = str(v)
    if 'e' in s:
        i = s.index('e')
        exponent = int(s[i + 1:])
        mantissa = s[:i]
        if '.' not in mantissa:
            frac_len = 0
        else:
            frac_len = len(mantissa) - mantissa.index('.') - 1
        frac_len -= exponent
        if frac_len <= 0:
            s = str(int(v))
        else:
            s = f'%.{int(frac_len)}f' % v
    if '.' not in s:
        s += '.0'
    return s

def main():
    N = int(input())
    ans = 1/pow(5, N)
    print(format_float(ans))

if __name__ == "__main__":
    main()