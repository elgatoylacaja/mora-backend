import os
from bson.json_util import dumps
from . import users


@users.route('/users', methods=['GET'])
def users_list():
    return dumps({'juan': 'jejeje'})

