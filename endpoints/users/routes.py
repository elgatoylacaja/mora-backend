from bson.json_util import dumps

from database import mongo
from . import users


@users.route('/users', methods=['GET'])
def users_list():
    test_data = mongo.db.testData.find_one()
    print(test_data)
    return dumps({'juan': test_data['Test']})

