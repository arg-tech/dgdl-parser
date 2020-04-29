from .requirement import Requirement

class InRoleRequirement(Requirement):

    def __init__(self, playerID, role, negative=False):
        self.type = "inrole"
        self.playerID = playerID
        self.role = role
        self.negative = negative