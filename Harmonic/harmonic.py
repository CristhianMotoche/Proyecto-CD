class Harmonic(object):
    def __init__(self):
        """Constructor """
        super(Harmonic, self).__init__()

    def sum(self, d, n, m):
        digits = [0]*(d+11)

        for i in range(m,n + 1):
            remainder = 1
            for digit in range(d + 11):
                if remainder == 0:
                    break
                div = int(remainder / i)
                mod = remainder % i
                digits[digit] += div
                remainder = mod*10

        for i in range(1, d + 11):
            digits[-(i + 1)] += int(digits[-i] / 10)
            digits[-i] %= 10

        if digits[d + 1] >= 5:
            digits[d] += 1

        for i in range(d + 1):
            digits[d - i - 1] += int(digits[d - i] / 10)
            digits[d - i] %= 10

        return digits[:-11]
