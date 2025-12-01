def contain(class1, class2):
    if class1.get_outer_rect()[0] > class2.get_outer_rect()[0] and class1.get_outer_rect()[1] > class2.get_outer_rect()[1]:
        return f"{type(class1).__name__} может содержать {type(class2).__name__}"
    else:
        return f"{type(class1).__name__} не может содержать {type(class2).__name__}"