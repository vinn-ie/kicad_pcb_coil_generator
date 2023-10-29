import os
import math

def generate_archimedean_spiral_coil_footprint(filename, num_turns, layer, OD, track_width, gap):
    with open(filename, 'w') as f:
        # Header for KiCad version 5 footprint
        f.write(f"(module ArchimedeanSpiralCoil (layer {layer}) (tedit 5A8B0D07)\n")
        f.write(f"  (descr \"Archimedean spiral coil with {num_turns} turns\")\n")
        
        # Constants for the spiral
        b = (track_width + gap) / (2 * math.pi)
        theta_start = 3 * math.pi / 2
        theta_max = 2 * math.pi * num_turns + theta_start
        theta_step = 0.1
    
        theta_relative = 0
        theta = 0
        while theta < theta_max:
            r = (OD / 2) - b * theta_relative
            theta = theta_relative + theta_start
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            
            theta_next = theta + theta_step
            r_next = (OD / 2) - b * (theta_next - theta_start)
            x_next = r_next * math.cos(theta_next)
            y_next = r_next * math.sin(theta_next)
            
            f.write(f"  (fp_line (start {x:.6f} {y:.6f}) (end {x_next:.6f} {y_next:.6f}) (layer {layer}) (width {track_width:.6f}))\n")
            
            theta_relative = theta_next - theta_start
        
        # Closing the module
        f.write(")\n")

    print(f"{filename} generated successfully!")

# Example usage:
generate_archimedean_spiral_coil_footprint("archimedean_spiral_coil.kicad_mod", num_turns=5, layer="F.Cu", OD=2.5, track_width=0.1, gap=0.1)
