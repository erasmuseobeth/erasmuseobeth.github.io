# Generating HTML content based on parsed colors and requirements

# List of text colors for each div box text
text_colors = [
    "#FFFFFF",  # White
    "#000000",  # Black
    "#FFD700",  # Gold
    "#FFDF00",  # Yellow Gold
    "#00FFFF",  # Aqua
    "#000080",  # Navy
    "#4169E1",  # Royal Blue
    "#0047AB",  # Cobalt
    "#00008B",  # Dark Blue
    "#0000FF"   # Blue
]

# Sample parsed data of color codes for demonstration
color_codes = [
    "#00167A", "#000080", "#060b91", "#002bf5", "#00FFFF", "#0047AB",
    "#0000FF", "#0C1D4E", "#1944f1", "#002bd8"
]

# Generating the HTML structure
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Color Preview</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-wrap: wrap;
        }
        .color-box {
            width: 200px;
            margin: 10px;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .text-sample {
            font-size: 2.5rem;
            margin: 5px 0;
        }
    </style>
</head>
<body>
"""

# Creating divs for each color code with the required text in different colors
for color_code in color_codes:
    html_content += f'<div class="color-box" style="background-color: {color_code}; color: #FFFFFF;">\n'
    for text_color in text_colors:
        html_content += f'    <p class="text-sample" style="color: {text_color};">This is how I look</p>\n'
    html_content += '</div>\n'

# Closing HTML tags
html_content += """
</body>
</html>
"""

# Saving the HTML file to the provided path
output_html_path = "../colors_preview.html"
with open(output_html_path, "w") as html_file:
    html_file.write(html_content)

output_html_path
