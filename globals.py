# Getters and setters to set the lambda that determines the prioritization function
# for both the PQ and the PancakeStack Class
COMPARE_FN = None

def set_compare(fn):
    global COMPARE_FN
    COMPARE_FN = fn
def get_compare():
    return COMPARE_FN