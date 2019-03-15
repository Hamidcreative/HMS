import requests, json

def checkUserGroup(request, group):
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    print(request.user.groups)

    if 'user_group' not in request.session:
        print('innnnnnnnnnnnnnnnnnnnnnnnnnnnnnn')
        request.session['user_group'] = request.user.groups.values_list('name', flat=True).first()

    if request.session['user_group'] == group:
        print('session true')
        return True
    else:
        return False