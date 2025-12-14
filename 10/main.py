import re
from typing import List
import numpy as np
from scipy.optimize import LinearConstraint, milp, Bounds


class Wiring:
    def __parse_expected(self,expected: str) -> int:
        n = len(expected) - 2
        to_binary_mapper = lambda x: '0' if x == '.' else '1'
        bits = ''.join(map(to_binary_mapper, expected[1:-1]))
        return int(bits, 2)

    def __init__(self, expected: str, buttons: List[int], joltages: str) -> None:
        self.expected = self.__parse_expected(expected)
        self.__digits = len(expected) - 2
        self.buttons = buttons
        self.joltages = list(map(int, joltages[1:-1].split(',')))

    def __str__(self) -> str:
        buttons_binary = [format(x,f'0{self.__digits}b') for x in self.buttons]
        return f"{format(self.expected, f'0{self.__digits}b')} {buttons_binary} {self.joltages}"
    def __repr__(self) -> str:
        return self.__str__()

    def minimum_presses(self) -> int:
        states_old, states_new = [0], []
        times = 0
        while self.expected not in states_old:
            states_new = []
            for button in self.buttons:
                for old_state in states_old:
                    states_new.append(old_state ^ button)
            states_old = states_new
            times += 1
        return times

    def minimum_presses_joltage(self) -> int:
        string_repr = [ format(button, f'0{self.__digits}b') for button in self.buttons ]
        rep_mask = []
        for i in range(self.__digits):
            tmp = []
            for rep in string_repr:
                tmp.append(int(rep[i]))
            rep_mask.append(tmp)
        A = np.array(rep_mask)
        b = np.array(self.joltages)
        c = np.ones(A.shape[1])
        linear_constraint = LinearConstraint(A, b, b)
        bounds = Bounds(lb=[0] * A.shape[1], ub=[1000] * A.shape[1])
        res = milp(c=c, constraints=[linear_constraint], bounds=bounds, integrality=np.ones(A.shape[1]))
        return sum(res.x)

def read_file(fname: str) -> List[Wiring]:
    ret = []
    with open(fname, 'r') as f:
        for line in f:
            splitted = line.split()
            bitcount = len(splitted[0]) - 2
            button_groups = re.findall(r"\((.*?)\)", line)
            button_bins = []
            for group in button_groups:
                indices = []
                if group.strip() != "":
                    indices = list(map(int, group.split(',')))
                bits = ['1' if i in indices else '0' for i in range(bitcount)]
                button_bins.append(int(''.join(bits),base=2))
            ret.append(Wiring(splitted[0], button_bins, splitted[-1]))
    return ret


def main() -> None:
    wirings = read_file('input.txt')
    summa = 0
    # part 1
    for wiring in wirings:
       summa += wiring.minimum_presses()
    print(summa)
    # part 2
    summa = 0
    for wiring in wirings:
       summa += wiring.minimum_presses_joltage()
    print(int(summa))


if __name__ == '__main__':
    main()
