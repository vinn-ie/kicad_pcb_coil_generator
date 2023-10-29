import os

def generate_hexagonal_spiral_coil_footprint(filename, num_turns, layer, total_width, line_width, gap):
    with open(filename, 'w') as f:
        # Header for KiCad version 5 footprint
        f.write(f"(module HexagonalSpiralCoil (layer {layer}) (tedit 5A8B0D07)\n")
        f.write(f"  (descr \"Hexagonal spiral coil with {num_turns} turns\")\n")
        
        # Determine the starting length of the hexagon from the outermost edge.
        # Using the flat-to-flat distance.
        length = total_width / 2
        decrement = (line_width + gap) / (3**0.5)
        
        x, y = 0, 0
        direction = 0  # 0 = right, 1 = up-right, 2 = up-left, 3 = left, 4 = down-left, 5 = down-right
        
        for i in range(6*num_turns):
            # Update length decrement after every third edge
            if i % 3 == 0 and i > 0:
                length -= decrement

            delta_y = length * (3**0.5 / 2)
            delta_x = length / 2

            if direction == 0: # Left
                x_end, y_end = x + length, y
            elif direction == 1: # Down-Left
                x_end, y_end = x + delta_x, y + delta_y
            elif direction == 2: # Down-Right
                x_end, y_end = x - delta_x, y + delta_y
            elif direction == 3: # Right
                x_end, y_end = x - length, y
            elif direction == 4: # Up-Right
                x_end, y_end = x - delta_x, y - delta_y
            elif direction == 5: # Up-Left
                x_end, y_end = x + delta_x, y - delta_y

            f.write(f"  (fp_line (start {x:.6f} {y:.6f}) (end {x_end:.6f} {y_end:.6f}) (layer {layer}) (width {line_width:.6f}))\n")
            
            # Update x and y for next segment
            x, y = x_end, y_end

            direction = (direction + 1) % 6
            
        # Closing the module
        f.write(")\n")
    print(f"{filename} generated successfully!")

# Example usage:
generate_hexagonal_spiral_coil_footprint("hexagonal_spiral_coil.kicad_mod", num_turns=4, layer="F.Cu", total_width=2.5, line_width=0.1, gap=0.1)
