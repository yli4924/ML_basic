def generateSessionData(input):
    window = 600000
    if 'events' not in input:
        return
    visitor_records = defaultdict(list)
    session_by_user = {}
    for event in input['events']:
        visitor_id = event['visitorId']
        visitor_records[visitor_id].append((event['timestamp'], event['url']))

    for visitor_id, records in visitor_records.items():
        sessions = []
        records.sort()
        session_start_time, session_end_time, pages = records[0][0], records[0][0], [records[0][1]]
        for timestamp, url in records[1:]:
            if timestamp <= session_end_time+window:
                pages.append(url)
                session_end_time = timestamp
            else:
                sessions.append({
                    "duration": session_end_time-session_start_time,
                    "pages": pages,
                    "startTime":session_start_time
                })
                session_start_time, session_end_time,pages = timestamp,timestamp,[url]
        if len(pages) > 0:
            sessions.append({
                "duration": session_end_time - session_start_time,
                "pages": pages,
                "startTime": session_start_time
            })
        session_by_user[visitor_id] = sessions
    return {'sessionByUser': session_by_user}
  #input = {'events': {
    #    {"url": "/battle-itchy-slave", "visitorId": "65bed0ca-8d6b-38f6-853b-16b649966ad8", "timestamp": 1515042135343},
    #    {"url": "/breed-heavy-vacation/start-ceaseless-oven", "visitorId": "3d3fe222-5eb6-3920-8aa6-6bee9b7037a0",
    #     "timestamp": 1515042145370}}}
    #generateSessionData(input)
