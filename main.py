from line import Line
from vector import Vector


ell = Line(normal_vector=Vector(['4.046', '2.836']), constant_term = '1.21')
ell2 = Line(normal_vector=Vector(['10.115', '7.09']), constant_term = '3.025')
print('Intersection 1: ', ell.intersection_with(ell2))

ell = Line(normal_vector=Vector(['7.204', '3.182']), constant_term = '8.68')
ell2 = Line(normal_vector=Vector(['8.172', '4.114']), constant_term = '9.883')
print('Intersection 2: ', ell.intersection_with(ell2))

ell = Line(normal_vector=Vector(['1.182', '5.562']), constant_term = '6.744')
ell2 = Line(normal_vector=Vector(['1.773', '8.343']), constant_term = '9.525')
print('Intersection 3: ', ell.intersection_with(ell2))


# v = Vector(['8.462', '7.893', '-8.187'])
# w = Vector(['6.984', '-5.975', '4.778'])
# print('#1', v.cross(w))
#
# v = Vector(['-8.987', '-9.838', '5.031'])
# w = Vector(['-4.268', '-1.861', '-8.866'])
# print('#2', v.area_of_parallelogram_with(w))
#
# v = Vector(['1.5', '9.547', '3.691'])
# w = Vector(['-6.007', '0.124', '5.772'])
# print('#3', v.area_of_triangle_with(w))


#
# if __name__ == "__main__":
#     # execute only if run as a script
#     main()