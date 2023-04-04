import math

# Define the polar phasor
magnitude = 100
phase_angle_degrees = 145

# Convert phase angle from degrees to radians
phase_angle_radians = math.radians(phase_angle_degrees)

# Calculate the rectangular form using the formula:
# real_part = magnitude * cos(phase_angle)
# imaginary_part = magnitude * sin(phase_angle)
real_part = magnitude * math.cos(phase_angle_radians)
imaginary_part = magnitude * math.sin(phase_angle_radians)

# Print the rectangular form
print("Rectangular form: {:.2f} + {:.2f}j".format(real_part, imaginary_part))

