from rest_framework import exceptions

def user_auth_rule(user):
    if user is not None:
        if not user.username:
            raise exceptions.AuthenticationFailed(
                "username is not verified for this account",
                "username_not_verified",
            )
        if not user.is_active:
            raise exceptions.AuthenticationFailed(
                "No active account found with the given credentials",
                "no_active_account",
            )
        return True
    return False