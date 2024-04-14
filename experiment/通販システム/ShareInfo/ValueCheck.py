from ShareInfo.ShareInfo import Message,InputLimit

def memIDCheck(mem_id) :
    ValueCheck(mem_id,InputLimit.ID_MIN_DIGIT,InputLimit.ID_MAX_DIGIT)
def passwordCheck(password) :
    ValueCheck(password,InputLimit.PW_MIN_DIGIT,InputLimit.PW_MAX_DIGIT)

def ValueCheck(check_value,min_digit,max_digit) :
    if not check_value :
        return Message.NOT_ENTERED
    elif min_digit <= len(check_value) <= max_digit :
        return Message.CHECK_FAILURE
    elif not check_value.isalnum() :
        return Message.CHECK_FAILURE
    return ""