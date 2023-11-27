from ics import Calendar
import requests
from datetime import date, timedelta


def get_events_by_weekday(isen_url):
    ICS_URL = isen_url
    response = requests.get(ICS_URL)
    calendar = Calendar(response.text)
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    # Filter events that occur within the current week
    events_this_week = [event for event in calendar.events if start_of_week <= event.begin.date() <= end_of_week]
    # Create a list for each weekday
    weekdays = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
    events_by_weekday = {day: [] for day in weekdays}
    # Group events by weekday
    for event in events_this_week:
        start = event.begin.strftime("%H:%M")
        event_name = event.name.encode('latin-1').decode('utf-8')
        intervenant = event.description.split("\n")[3].split(" : ")[1].encode('latin-1').decode('utf-8')
        description = event.description.split("\n")[4].split(" : ")[1].encode('latin-1').decode('utf-8')
        salle = event.location
        end = event.end.strftime("%H:%M")
        weekday = weekdays[event.begin.date().weekday()]
        events_by_weekday[weekday].append({
            "modified": False, # "true" or "false
            "start": start,
            "event_name": event_name,
            "intervenant": intervenant,
            "description": description,
            "salle": salle,
            "end": end
        })
    return events_by_weekday


# function to save to json the dictionary of events
def save_events_to_json(events_by_weekday):
    import json
    with open('static/events.json', 'w') as fp:
        json.dump(events_by_weekday, fp, indent=4)


def compare_dicts(dict1, dict2):
    for weekday, events in dict2.items():
        for event in events:
            if weekday not in dict1 or event not in dict1[weekday]:
                event["modified"] = True
    return dict2