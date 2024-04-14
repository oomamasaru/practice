from Screen.BeforeLogin.BeforeLoginScreen import BeforeLoginScreen
from Screen.AfterLogin.AfterLoginScreen import AfterLoginScreen

def execute() :
    before_login_root = BeforeLoginScreen()
    member_info_dict = before_login_root.bootScreen()

    if not member_info_dict :
        return 
    
    after_login_root = AfterLoginScreen(member_info_dict)
    after_login_root.bootScreen()

if __name__ == "__main__":
    execute()