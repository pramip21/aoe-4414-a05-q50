# ray_ellipsoid_intersection.py
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Pramil Patel
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
# e.g., R_E_KM = 6378.137
# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
# arg1 = '' # description of argument 1
# arg2 = '' # description of argument 2

# parse script arguments
# if len(sys.argv)==3:
#   arg1 = sys.argv[1]
#   arg2 = sys.argv[2]
#   ...
# else:
#   print(\
#    'Usage: '\
#    'python3 arg1 arg2 ...'\
#   )
#   exit()

# write script below this line
w=7.292115*10**-5
R_E_KM = 6378.1363
E_E    = 0.081819221456


if len(sys.argv) == 7:
    d_l_x = float(sys.argv[1])
    d_l_y = float(sys.argv[2])
    d_l_z = float(sys.argv[3])
    c_l_x = float(sys.argv[4])
    c_l_y = float(sys.argv[5])
    c_l_z = float(sys.argv[6])
else:
    print('python3 conv_ops.py d_l_x, d_l_y, d_l_z, c_l_x, c_l_y, c_l_z')
    

a = d_l_x*d_l_x + d_l_y*d_l_y + ((d_l_z*d_l_z)/(1-E_E*E_E))
b = 2*(d_l_x*c_l_x + d_l_y*c_l_y + ((d_l_z*c_l_z)/(1-E_E**2)))
c = c_l_x**2+c_l_y**2+(c_l_z**2)/(1-E_E**2)-R_E_KM**2
discr = b*b-4.0*a*c


if discr >= 0:
    d = (-b - math.sqrt(discr))/(2*a)

if d < 0:
     d = (-b + math.sqrt(discr))/(2*a)
   
if d > 0:
    l_d = [d*d_l_x+c_l_x, d*d_l_y+c_l_y, d*d_l_z+c_l_z]
     
print(l_d[0]) # x-component of intersection point
print(l_d[1]) # y-component of intersection point
print(l_d[2]) # z-component of intersection point