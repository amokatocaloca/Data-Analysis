import json
import pandas as pd

# Load JSON data from file
with open("tumblr_data.json", "r", encoding="utf-8") as file:
    tumblr_data = json.load(file)

# Function to extract post content text and assign unique IDs
def extract_tumblr_posts(tumblr_data):
    extracted_data = []
    
    for i, post in enumerate(tumblr_data, start=1):
        post_id = i  # Unique ID
        post_url = post.get("postUrl", "")
        date = post.get("date", "")
        
        # Extract all text content from "content" list
        content_list = post.get("content", [])
        content_text = " ".join([item["text"] for item in content_list if item["type"] == "text"]).strip()

        # If no text content, fallback to summary
        if not content_text:
            content_text = post.get("summary", "")

        extracted_data.append({
            "ID": post_id,
            "Post URL": post_url,
            "Date": date,
            "Content": content_text
        })
    
    return pd.DataFrame(extracted_data)

# Convert extracted data into a DataFrame
df = extract_tumblr_posts(tumblr_data)

# Save extracted data to CSV
df.to_csv("tumblr_data.csv", index=False)