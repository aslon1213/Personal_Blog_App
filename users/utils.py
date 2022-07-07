

def check_password_req(pass_1, pass_2):
    if pass_1 == pass_2:
        if len(pass_1) >= 8:
            return 1
        else:
            return 'Password length is less than 8'
    else:
        return 'Passwords are not identical'