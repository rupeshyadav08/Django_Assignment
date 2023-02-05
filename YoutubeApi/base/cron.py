import requests
from YoutubeApi import settings
from isodate import parse_duration
from .models import  ListOfVideos
from datetime import datetime, timedelta

import logging
logger = logging.getLogger(__name__)


def GetAndUpdateData():
    print('started')
    logger.info('Function called')
    logger.info('---------------')
    video_data=[]
    logger.info('Api Call iniated')
    details_url = settings.details_url
    video_url = settings.video_url
    current_time = datetime.now()
    lastcall = current_time - timedelta(minutes=100)
    details_params = {
        'part' : 'snippet',
        'q' : 'game',
        'key' : settings.YoutubeKey,
        'maxResults' : 50,
        'order' : 'date',
        'publishedAfter' : (lastcall.strftime('%Y-%m-%dT%H:%M:%SZ'))
    }
    
    details_request = requests.get(details_url, params=details_params)
    results= details_request.json()['items']
    videoIdList = []
    for res in results:
        videoId = res['id']['videoId']
        videoIdList.append(videoId)
    
    video_params = {
        'part' : 'snippet,contentDetails',
        'key' : settings.YoutubeKey,
        'id' : ','.join(videoIdList)
    }

    video_request = requests.get(video_url, params=video_params)
    results = video_request.json()['items']
    for result in results:
        data = {
            'title' : result['snippet']['title'],
            'description' : result['snippet']['description'],
            'id' : result['id'],
            'publishtime' : result['snippet']['publishedAt'],
            'view' : f'https://www.youtube.com/watch?v={ result["id"] }',
            'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
            'thumbnail' : result['snippet']['thumbnails']['high']['url'],
            'channelid' : result['snippet']['channelId'],
            'channelname' : result['snippet']['channelTitle']
        }
        video_data.append(data)

    for item in video_data:
        Title = item['title']
        VideoId = item['id']
        Description = item['description']
        UploadDateTime = item['publishtime']
        ThumbnailUrl = item['thumbnail']
        Duration = item['duration']
        ChannelId = item['channelid']
        ChannelName = item['channelname']
        VideoUrl = item['view']
        ListOfVideos.objects.create(
            Title=Title,
            VideoId=VideoId,
            Description=Description,
            UploadDateTime=UploadDateTime,
            ThumbnailUrl=ThumbnailUrl,
            Duration=Duration,
            ChannelId=ChannelId,
            ChannelName=ChannelName,
            VideoUrl=VideoUrl,
        )
    logger.info('Execution caompleted')
    
