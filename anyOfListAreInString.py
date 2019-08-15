def anyOfListAreInString(case: str, of: list):
    result = False
    for checks in of:
        if checks in case:
            result = True
    return result
