from flask import Blueprint
from utils import check_user

blueprint_query = Blueprint('blueprint_query', __name__)


@blueprint_query.route('/<point>', methods=['GET', 'POST'])
@check_user('typical')
def simple_query(point):
    return f'Query point: {point}'
