def convert_path(path):
    return path.replace("\\", "/")

# Example usage
original_path = r"C:\Users\CISSSXS4\OneDrive - New Jersey Transit\Desktop\Scraper"
converted_path = convert_path(original_path)

print("Converted Path:", converted_path)
