from csp import Constraint, CSP
from typing import Dict, List, Optional


class australiamapcoloring():
    def __init__(self):
        variables: List[str] = ["Western Australia", "Northern Territory", "South Australia", "Queensland",
                                "New South Wales", "Victoria", "Tasmania"]
        domains: Dict[str, List[str]] = {}

        for variable in variables:
            domains[variable] = ["red", "green", "blue"]

        self.csp: CSP[str, str] = CSP(variables, domains)

        self.csp.addconstraint(self.mapcoloringconstraint("Western Australia", "Northern Territory"))
        self.csp.addconstraint(self.mapcoloringconstraint("Western Australia", "South Australia"))
        self.csp.addconstraint(self.mapcoloringconstraint("South Australia", "Northern Territory"))
        self.csp.addconstraint(self.mapcoloringconstraint("Queensland", "Northern Territory"))
        self.csp.addconstraint(self.mapcoloringconstraint("Queensland", "South Australia"))
        self.csp.addconstraint(self.mapcoloringconstraint("Queensland", "New South Wales"))
        self.csp.addconstraint(self.mapcoloringconstraint("New South Wales", "South Australia"))
        self.csp.addconstraint(self.mapcoloringconstraint("Victoria", "South Australia"))
        self.csp.addconstraint(self.mapcoloringconstraint("Victoria", "New South Wales"))
        self.csp.addconstraint(self.mapcoloringconstraint("Victoria", "Tasmania"))
        print(self.csp)

    def solve(self):
        solution: Optional[Dict[str, str]] = self.csp.solution()
        if not solution:
            print("No solution found!")
        else:
            print(solution)

    class mapcoloringconstraint(Constraint[str, str]):
        def __init__(self, place1: str, place2: str):
            super().__init__([place1, place2])
            self.place1 = place1
            self.place2 = place2

        def satisfied(self, assignment: Dict[str, str]) -> bool:
            if self.place1 not in assignment or self.place2 not in assignment:
                return True
            return assignment[self.place1] != assignment[self.place2]


a: australiamapcoloring = australiamapcoloring()
a.solve()
