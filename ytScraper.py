from googleapiclient.discovery import build

def search_first_video(query, ytKey):
    youtube = build('youtube', 'v3', developerKey=ytKey)

    request = youtube.search().list(
        part='snippet',
        q=query,
        type='video',
        maxResults=1
    )

    response = request.execute()

    if 'items' in response:
        first_video = response['items'][0]
        video_id = first_video['id']['videoId']
        video_link = f'https://www.youtube.com/watch?v={video_id}'
        return video_link
    else:
        print("No videos found.")
        return("x56")

