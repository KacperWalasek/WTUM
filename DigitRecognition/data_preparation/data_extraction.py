from data_preparation.find_min_position import find_min_position
from data_preparation.find_max_position import find_max_position
from data_preparation.find_median import find_median
from data_preparation.find_average import find_average
from data_preparation.projection_vertical import projection_vertical
from data_preparation.projection_horizontal import projection_horizontal
from data_preparation.transition_horizontal import transition_horizontal
from data_preparation.transition_vertical import transition_vertical
import mahotas

def extract_data(entity):
    projections = [projection_horizontal, projection_vertical, transition_horizontal, transition_vertical]
    values = []
    for his_fun in projections:
        histogram = his_fun(entity)
        values.extend([find_average(histogram), find_median(histogram)]
                      + list(find_max_position(histogram))
                      + list(find_min_position(histogram)))

    values.append(mahotas.features.eccentricity(entity.pixels))
    values.extend(list(mahotas.features.ellipse_axes(entity.pixels)))
    values.append(mahotas.features.roundness(entity.pixels))
    return values
