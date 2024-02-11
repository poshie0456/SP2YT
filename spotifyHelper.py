import requests



def getPlaylistTracks(playlistID,client_id,client_secret):
        # Make sure to include the access token in the Authorization header
    token = getToken(client_id,client_secret)
    headers = {
        "Authorization": f"{token[1]} {token[0]}"
    }

    url = f"https://api.spotify.com/v1/playlists/{playlistID}/tracks"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        track_tuple = []
        
        # Get items in the response
        for item in data.get('items', []):
            track = item.get('track')
            try:
                track_name = track.get('name')
                artists = track.get('artists')
                artist_names = ', '.join([artist.get('name') for artist in artists]) #Joined in case multiple artists
                track_tuple.append((track_name, artist_names))
                
            except Exception as e:
                print(e)
        return track_tuple
    else:
        print("Error: Code ", response.status_code)



def getToken(id,secret):
    url = "https://accounts.spotify.com/api/token"
    body = {
        "grant_type": "client_credentials",
        "client_id": f"{id}",
        "client_secret": f"{secret}"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=body, headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        access_token = response_json.get('access_token')
        token_type = response_json.get('token_type')
        
        #print("Access Token:", access_token)
        #print("Token Type:", token_type)
        return (access_token,token_type)
