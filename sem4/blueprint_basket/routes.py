from flask import Blueprint
from utils import login_required, check_user

blueprint_basket = Blueprint('blueprint_basket', __name__, template_folder = 'templates')


@blueprint_basket.route('/basket/<mpoint>',methods = ['GET', 'POST'])
@check_user
def basket(mpoint):
#    print('I am in basket and point =',mpoint)
    return 'Basket done'
