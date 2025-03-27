import pandas as pd

# Sample data
data = {
    "content_id": [1, 2, 3, 4],
    "content_text": [
        "hello world of SQL",
        "the QUICK-brown fox",
        "modern-day DATA science",
        "web-based FRONT-end development"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)
def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    user_content.rename(columns={'content_text': 'original_text'}, inplace=True)
    user_content['converted_text'] = user_content['original_text'].str.title()

    return user_content

# Display the updated DataFrame
print(capitalize_content(df))