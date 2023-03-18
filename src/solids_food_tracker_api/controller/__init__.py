from controller.children_controller import child
from controller.foods_controller import food
from controller.auth_controller import auth
from controller.stats_controller import stats

registerable_controllers = [
    child,
    food,
    auth,
    stats
]