class AddLists:
    @staticmethod
    def sumList(augend, addend=None):
        if isinstance(augend, list):
            return AddLists.sumList(augend)
        return augend + addend

    @staticmethod
    def sumLists(valueList):
        result = 0
        for value in valueList:
            result = AddLists.sumList(result, value)

        return result