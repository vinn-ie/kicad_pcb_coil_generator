import os

def generate_square_spiral_coil_footprint(filename, num_turns, layer, total_width, line_width, gap):
    with open(filename, 'w') as f:
        # Header for KiCad version 5 footprint
        f.write(f"(module SquareSpiralCoil (layer {layer}) (tedit 5A8B0D07)\n")
        f.write(f"  (descr \"Square spiral coil with {num_turns} turns\")\n")
        
        width = total_width - line_width
        x, y = 0, 0
        direction = 0 # 0 = right, 1 = down, 2 = left, 3 = up
        
        for i in range(4*num_turns):
            if direction == 0: # Right
                x_end, y_end = x + width, y
            elif direction == 1: # Down
                x_end, y_end = x, y + width
                width -= (line_width + gap)
            elif direction == 2: # Left
                x_end, y_end = x - width, y
            elif direction == 3: # Up
                x_end, y_end = x, y - width
                width -= (line_width + gap)

            f.write(f"  (fp_line (start {x:.6f} {y:.6f}) (end {x_end:.6f} {y_end:.6f}) (layer {layer}) (width {line_width:.6f}))\n")
            
            # Update x and y for next segment
            x, y = x_end, y_end

            direction = (direction + 1) % 4
        
        # Closing the module
        f.write(")\n")
    print(f"{filename} generated successfully!")

# Example usage:
generate_square_spiral_coil_footprint("square_spiral_coil2.kicad_mod", num_turns=6, layer="F.Cu", total_width=2.5, line_width=0.1, gap=0.1)
