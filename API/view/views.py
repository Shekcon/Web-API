from django.shortcuts import render, reverse, HttpResponse
from apiclient.discovery import build
from apiclient.errors import HttpError


def result(request, *args, **kargs):
    if request.method == "POST":
        options = {
            "key": request.POST['key'],
            "max_results": 25
        }
        return render(request, 'view/result.html', contents)
    return render(request, 'view/result.html', {})


def search_videos(options):
    DEVELOPER_KEY = "AIzaSyCXMDV4kLIWAQxsv4oM_2p1ZlrVerIKbVM"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options["key"],
        part="id,snippet",
        maxResults=options["max_results"]
    ).execute()

    contexts = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            # videos.append("%s (%s)" % (search_result["snippet"]["title"],
            #                            search_result["id"]["videoId"]))
            contexts.append({
                'title': search_result["snippet"]["title"],
                'video_id': search_result["id"]["videoId"],
                'thumbnail': search_result["snippet"]["thumbnails"]["high"]["url"]
            })
    print(contexts)
    return contexts

def watching(request, id):
    return HttpResponse("Greeting Shekcon %s" % (id))


def index(request, *args, **kargs):
    contents = {
            "result_videos": search_videos(options)
    }
    return render(request, 'view/result.html', contents)