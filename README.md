
# Instagram Bot for Engagement



## Features

- **Automated Login**: Logs in using session data or username/password.
- **Commenting**: Chooses random comments from a predefined list and posts them on target media.
- **Liking**: Likes posts based on specified hashtags.
- **Following**: Follows users who have interacted with posts of specific hashtags.
- **Unfollowing**: Unfollows users that were previously followed by the bot.

## Requirements

- Python 3.7+
- [instagrapi](https://github.com/adw0rd/instagrapi)

Install `instagrapi` via pip:
```bash
pip install instagrapi
```

## Setup

1. Clone this repository or copy the script into a Python file.
2. Install the dependencies.
3. Update the `username` and `password` variables with your Instagram account credentials.

## Usage

### Main Functions

- **`login_user(username, password)`**: Logs into Instagram, using session data if available to avoid re-login.
- **`follow(pk)`**: Follows users based on a target profile's followers.
- **`unfollow()`**: Unfollows users that the bot followed.
- **`comment(media_id)`**: Posts a random comment on the specified media.
- **`like(media_id)`**: Likes the specified media.
- **`interactions()`**: The main function that performs interactions—like, comment, and follow—on posts with specific hashtags.

### Running the Script

The script runs an infinite loop in the `main()` function, repeating the `interactions()` process every hour and then unfollowing previously followed users to avoid excessive following.

```python
python bot.py
```

## Configuration

Edit the hashtag list in the `interactions()` function to target specific hashtags for engagement:
```python
hashtag = ["entrepreneur", "success", "onlinebusiness", "sidehustle"]
```

