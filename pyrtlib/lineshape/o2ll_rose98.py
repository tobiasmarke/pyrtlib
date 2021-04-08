import numpy as np

# Nico F[GHz]
f = np.array(
    [118.7503, 56.2648, 62.4863, 58.4466, 60.3061, 59.591, 59.1642, 60.4348, 58.3239, 61.1506, 57.6125, 61.8002,
     56.9682, 62.4112, 56.3634, 62.998, 55.7838, 63.5685, 55.2214, 64.1278, 54.6712, 64.6789, 54.13, 65.2241, 53.5957,
     65.7648, 53.0669, 66.3021, 52.5424, 66.8368, 52.0214, 67.3696, 51.5034, 67.9009, 368.4984, 424.7632, 487.2494,
     715.3931, 773.8397, 834.1458])
# Nico S(T_0)[Hz*cm2]
s300 = np.array(
    [2.936e-15, 8.079e-16, 2.48e-15, 2.228e-15, 3.351e-15, 3.292e-15, 3.721e-15, 3.891e-15, 3.64e-15, 4.005e-15,
     3.227e-15, 3.715e-15, 2.627e-15, 3.156e-15, 1.982e-15, 2.477e-15, 1.391e-15, 1.808e-15, 9.124e-16, 1.23e-15,
     5.603e-16, 7.842e-16, 3.228e-16, 4.689e-16, 1.748e-16, 2.632e-16, 8.898e-17, 1.389e-16, 4.264e-17, 6.899e-17,
     1.924e-17, 3.229e-17, 8.191e-18, 1.423e-17, 6.494e-16, 7.083e-15, 3.025e-15, 1.835e-15, 1.158e-14, 3.993e-15])
# Nico (Elow+hf)/kT_0 [unitless]
be = np.array(
    [0.009, 0.015, 0.083, 0.084, 0.212, 0.212, 0.391, 0.391, 0.626, 0.626, 0.915, 0.915, 1.26, 1.26, 1.66, 1.665, 2.119,
     2.115, 2.624, 2.625, 3.194, 3.194, 3.814, 3.814, 4.484, 4.484, 5.224, 5.224, 6.004, 6.004, 6.844, 6.844, 7.744,
     7.744, 0.048, 0.044, 0.049, 0.145, 0.141, 0.145])
# Nico gamma(T_0) [MHZ/mb == GHz/bar]
wb300 = 0.56
x = 0.8
w300 = np.array(
    [1.63, 1.646, 1.468, 1.449, 1.382, 1.36, 1.319, 1.297, 1.266, 1.248, 1.221, 1.207, 1.181, 1.171, 1.144, 1.139, 1.11,
     1.108, 1.079, 1.078, 1.05, 1.05, 1.02, 1.02, 1.0, 1.0, 0.97, 0.97, 0.94, 0.94, 0.92, 0.92, 0.89, 0.89, 1.92, 1.92,
     1.92, 1.81, 1.81, 1.81])
y300 = np.append(
    [-0.0233, 0.2408, -0.3486, 0.5227, -0.543, 0.5877, -0.397, 0.3237, -0.1348, 0.0311, 0.0725, -0.1663, 0.2832,
     -0.3629, 0.397, -0.4599, 0.4695, -0.5199, 0.5187, -0.5597, 0.5903, -0.6246, 0.6656, -0.6942, 0.7086,
     -0.7325, 0.7348, -0.7546, 0.7702, -0.7864, 0.8083, -0.821, 0.8439, -0.8529], np.tile(0.0, (1, 6)))
v = np.append(
    [0.0079, -0.0978, 0.0844, -0.1273, 0.0699, -0.0776, 0.2309, -0.2825, 0.0436, -0.0584, 0.6056, -0.6619, 0.6451,
     -0.6759, 0.6547, -0.6675, 0.6135, -0.6139, 0.2952, -0.2895, 0.2654, -0.259, 0.375, -0.368, 0.5085, -0.5002,
     0.6206, -0.6091, 0.6526, -0.6393, 0.664, -0.6475, 0.6729, -0.6545], np.tile(0.0, (1, 6)))
