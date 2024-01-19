# This code is part of Qiskit.
#
# (C) Copyright IBM 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

""" Test data potentials """

import numpy as np

from qiskit.chemistry.constants import HARTREE_TO_J_PER_MOL

X_DATA = np.array([0.45, 0.75, 1.05, 1.35, 1.65, 1.95, 2.25, 2.55, 2.85, 3.15,
                   3.45, 3.75, 4.05, 4.35, 4.65, 4.95, 5.25, 0.45, 0.75, 1.05,
                   1.35, 1.65, 1.95, 2.25, 2.55, 2.85, 3.15, 3.45, 3.75, 4.05,
                   4.35, 4.65, 4.95, 5.25, 0.45, 0.75, 1.05, 1.35, 1.65, 1.95,
                   2.25, 2.55, 2.85, 3.15, 3.45, 3.75, 4.05, 4.35, 4.65, 4.95,
                   5.25])

Y_DATA = np.array([-2254757.5348101, -2746067.46608231, -2664406.49829366,
                   -2611323.75276296, -2502198.92978322, -2417457.48952287,
                   -2390778.71123391, -2379482.70907613, -2373850.72354504,
                   -2361426.93801724, -2369992.6305902, -2363833.07716161,
                   -2360577.93019891, -2356002.65576262, -2355574.41051646,
                   -2357254.94032554, -2351656.71871981, -2308055.75509618,
                   -2797576.98597419, -2715367.76135088, -2616523.58105343,
                   -2498053.2658529, -2424288.88205414, -2393385.83237565,
                   -2371800.12956182, -2353202.82294735, -2346873.32092711,
                   -2343485.8487826, -2342937.74947792, -2350276.02096954,
                   -2347674.75469199, -2346912.78218669, -2339886.28877723,
                   -2353456.10489755, -2359599.85281831, -2811321.68662548,
                   -2763866.98837641, -2613385.92519959, -2506804.00364042,
                   -2419329.49702063, -2393428.68052976, -2374166.67617163,
                   -2352961.35574553, -2344972.64297329, -2356294.5588125,
                   -2341396.63369969, -2337344.83138146, -2339793.71365995,
                   -2335667.95101689, -2327347.45385524, -2341367.28061372])

YDATA_HARTEE = Y_DATA / HARTREE_TO_J_PER_MOL
YDATA_J_PEL_MOL = Y_DATA

XDATA_ANGSTROM = X_DATA
