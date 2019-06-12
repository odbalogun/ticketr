from django.contrib.auth.decorators import user_passes_test


def user_not_authenticated(user):
    """
    Function to restrict views (eg login) to only unauthenticated users
    :param user: user object
    :return: Boolean
    """
    # actual_decorator = user_passes_test(
    #     lambda u: not user.is_authenticated,
    #     login_url=login_url,
    #     redirect_field_name=redirect_field_name
    # )
    if not user.is_authenticated():
        return True
    return False
