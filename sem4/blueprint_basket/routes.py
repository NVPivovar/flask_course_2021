from flask import Blueprint
from utils import check_user

blueprint_basket = Blueprint('blueprint_basket', __name__)


@blueprint_basket.route('/<point>', methods=['GET', 'POST'])
@check_user('typical')
def basket(point):
    return f'Basket point: {point}'
