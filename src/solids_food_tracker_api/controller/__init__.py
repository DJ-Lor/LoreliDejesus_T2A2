from controller.home_controller import home 
from controller.parents_controller import parent 
from controller.children_controller import child
from controller.foods_controller import food
from controller.auth_controller import auth
from controller.stats_controller import stats

registerable_controllers = [
    home,
    parent,
    child,
    food,
    auth,
    stats
]