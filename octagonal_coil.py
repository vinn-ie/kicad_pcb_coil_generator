import os

def generate_octagonal_spiral_coil_footprint(filename, num_turns, layer, total_width, line_width, gap):
    with open(filename, 'w') as f:
        # Header for KiCad version 5 footprint
        f.write(f"(module OctagonalSpiralCoil (layer {layer}) (tedit 5A8B0D07)\n")
        f.write(f"  (descr \"Octagonal spiral coil with {num_turns} turns\")\n")
        
        # Calculate the starting length of the side of the octagon
        length = total_width / (1 + 2**0.5)
        ref_len = length
        x, y = length / (2**0.5), 0
        
        direction = 0

        for i in range(8 * num_turns):
            if direction == 7:
                length = ref_len - (line_width + gap / (2**0.5))
                ref_len = length
            elif direction == 3:
                length = ref_len - (line_width + gap / 2**0.5) / (2)
                
            delta = length / 2**0.5 if direction % 2 else length

            print(length)

            if direction == 0: # Right
                x_end, y_end = x + length, y
            elif direction == 1: # Diagonal Right-Down
                x_end, y_end = x + delta, y + delta
            elif direction == 2: # Down
                x_end, y_end = x, y + length
            elif direction == 3: # Diagonal Left-Down
                x_end, y_end = x - delta, y + delta
            elif direction == 4: # Left
                x_end, y_end = x - length, y
            elif direction == 5: # Diagonal Left-Up
                x_end, y_end = x - delta, y - delta
            elif direction == 6: # Up
                x_end, y_end = x, y - length
            elif direction == 7: # Diagonal Right-Up
                x_end, y_end = x + delta, y - delta

            f.write(f"  (fp_line (start {x:.6f} {y:.6f}) (end {x_end:.6f} {y_end:.6f}) (layer {layer}) (width {line_width:.6f}))\n")
            
            # Update starting point for next segment
            x, y = x_end, y_end

            direction = (direction + 1) % 8

        # Closing the module
        f.write(")\n")

    print(f"{filename} generated successfully!")

# Example usage:
generate_octagonal_spiral_coil_footprint("octagonal_spiral_coil.kicad_mod", num_turns=4, layer="F.Cu", total_width=2.5, line_width=0.1, gap=0.1)
