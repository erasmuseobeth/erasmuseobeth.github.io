import json

# Sample structure to hold parsed color data
colors_data = []

# Adding black and white manually to the data
colors_data.extend([
    {"name": "Black", "category": "Neutral", "hex": "#000000", "rgb": "(0, 0, 0)"},
    {"name": "White", "category": "Neutral", "hex": "#FFFFFF", "rgb": "(255, 255, 255)"}
])

# Raw text data from the user's file, simulating parsed data from the provided .txt file
raw_data = """
#00167A Navy Blue Shade
#000080 Dark Navy Blue Original
#060b91 Royal Blue Shade
#002bf5 Electric Blue Tint
#00FFFF Cyan Tones
#0047AB Cobalt Tints
#0000FF Blue Shades
"""

# Simulating parsing of color information
for line in raw_data.strip().split("\n"):
    if not line.strip():  # Skip empty lines
        continue
    parts = line.split()
    
    # Extract hex code, name, and category (last item on the line for this case)
    hex_code = parts[0]
    name = " ".join(parts[1:-1])
    category = parts[-1]
    
    # Infer RGB if possible by hex to RGB conversion
    rgb_tuple = tuple(int(hex_code[i:i+2], 16) for i in (1, 3, 5))
    rgb = f"({rgb_tuple[0]}, {rgb_tuple[1]}, {rgb_tuple[2]})"
    
    # Append structured color data
    colors_data.append({
        "name": name,
        "category": category,
        "hex": hex_code,
        "rgb": rgb
    })

# Saving the parsed data into a JSON file format as requested
output_filepath = "/mnt/data/colors_i_like.json"
with open(output_filepath, "w") as json_file:
    json.dump(colors_data, json_file, indent=4)

output_filepath
