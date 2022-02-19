import fractions as f


class Solution:
    def fractionAddition(self, expression: str) -> str:
        output = eval(str(expression))  # evaluate the expression
        output_frac = str(f.Fraction(output).limit_denominator()) # get the fraction
        if len(output_frac) < 3:
            return output_frac+"/1"
        return output_frac
