from typing import Generic, TypeVar, List, Optional, Dict
from abc import ABC, abstractmethod

V = TypeVar('V')
D = TypeVar('D')


class Constraint(Generic[V, D], ABC):
    def __init__(self, variables: List[V]) -> None:
        self.variables: List[V] = variables

    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...


class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables
        self.domains: Dict[V, List[D]] = domains
        self.constraints: Dict[V:List[Constraint[V, D]]] = []

        for variable in self.variables:
            self.constraints[V] = []
            if variable not in self.domains:
                raise LookupError("Domain not available for variable {v}".format(v=variable))

    def addconstraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable in self.variables:
                self.constraints[variable].append(constraint)
            else:
                raise LookupError("Invalid variable {v}".format(v=variable))

    def isconsistent(self, variable: V, vassignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(vassignment):
                return False
        return True

    def solution(self, vassignment: Dict[V, D]) -> Optional[Dict[V, D]]:
        if len(vassignment) == len(self.variables):
            return vassignment
        unassignedvars: List[V] = [v for v in self.variables if v not in vassignment]
        firstunassignedvar = unassignedvars[0]
        for domain in self.domains[firstunassignedvar]:
            local_vsassigment = vassignment.copy()
            local_vsassigment[firstunassignedvar] = domain
            if self.isconsistent(firstunassignedvar, local_vsassigment):
                result: Optional[Dict[D, V]] = self.solution(local_vsassigment)
                if result is not None:
                    return result
        return None
