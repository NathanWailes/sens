"""
Code based on https://developers.google.com/youtube/v3/docs/search/list#examples

Note from Nathan Wailes: I have an untracked "client_secrets.json" file and an untracked
"youtube-api-snippets-oauth2.json" file in the same folder as this file, which are used to make this program work.
I don't remember how I got those two json files. I think it may have been through the Google App Developer Console
(or something like that). I'm going to commit this code now so I don't lose it, but later I need to figure out how to
get those json files and add the instructions to this file so it's easy for others to use this code.
"""

# Sample Python code for user authorization

import httplib2

from googleapiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secrets.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
YOUTUBE_READ_WRITE_SSL_SCOPE = "https://www.googleapis.com/auth/youtube.force-ssl"
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = "WARNING: Please configure OAuth 2.0"


def get_list_of_all_videos_with_string(search_string):
    videos = []

    results = search_list_by_keyword(service,
                                    part='snippet',
                                    maxResults=50,
                                    q=search_string,
                                    type='video')

    for item in results['items']:
        new_video = {'id': item['id']['videoId'],
                     'title': item['snippet']['title'],
                     'published': {'year': item['snippet']['publishedAt'][:4],
                                   'month': item['snippet']['publishedAt'][5:7],
                                   'day': item['snippet']['publishedAt'][8:10]}}
        videos.append(new_video)

    videos = sorted(videos, key=lambda x: (x['published']['year'], x['published']['month'], x['published']['day']))

    with open('output.md', 'w', encoding="utf8") as outfile:
        for video in videos:
            video_date_string = video['published']['year'] + "." + video['published']['month'] + "." + video['published']['day']
            line_of_output = "[" + video_date_string + " - " + video['title'] + "](" + \
                             "https://www.youtube.com/watch?v=" + video['id'] + ")\n"
            outfile.write(line_of_output)

    return


def search_list_by_keyword(service, **kwargs):
    kwargs = remove_empty_kwargs(**kwargs) # See full sample for function
    results = service.search().list(
        **kwargs
    ).execute()

    return results


def remove_empty_kwargs(**kwargs):
    # Remove keyword arguments that are not set
    good_kwargs = {}
    if kwargs is not None:
        for key, value in kwargs.items():
            if value:
                good_kwargs[key] = value
    return good_kwargs


def get_authenticated_service(args):
    # Authorize the request and store authorization credentials.
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=YOUTUBE_READ_WRITE_SSL_SCOPE,
        message=MISSING_CLIENT_SECRETS_MESSAGE)

    storage = Storage("youtube-api-snippets-oauth2.json")
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage, args)

    # Trusted testers can download this discovery document from the developers page
    # and it should be in the same directory with the code.
    return build(API_SERVICE_NAME, API_VERSION,
            http=credentials.authorize(httplib2.Http()))


args = argparser.parse_args()
service = get_authenticated_service(args)


if __name__ == '__main__':
    get_list_of_all_videos_with_string('aubrey de grey')
