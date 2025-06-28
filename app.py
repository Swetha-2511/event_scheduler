from flask import Flask, jsonify, request
import json
from datetime import datetime, timedelta
import threading
import time
import os

app = Flask(__name__)

DATA_FILE = 'events.json'

# Load Events
def load_events():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Save Events
def save_events(events):
    with open(DATA_FILE, 'w') as f:
        json.dump(events, f, indent=4)

events = load_events()

# Reminder Background Thread
def reminder_checker():
    while True:
        now = datetime.now()
        upcoming_events = []
        for event in events:
            start_time = datetime.strptime(event['start_time'], '%Y-%m-%d %H:%M')
            if 0 <= (start_time - now).total_seconds() <= 3600:
                upcoming_events.append(event)
        if upcoming_events:
            print("\n=== Upcoming Events Within 1 Hour ===")
            for ev in upcoming_events:
                print(f"Reminder: {ev['title']} at {ev['start_time']}")
        time.sleep(60)

threading.Thread(target=reminder_checker, daemon=True).start()

# Create Event
@app.route('/events', methods=['POST'])
def create_event():
    data = request.json
    required_fields = ['title', 'description', 'start_time', 'end_time']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    event = {
        'id': len(events) + 1,
        'title': data['title'],
        'description': data['description'],
        'start_time': data['start_time'],
        'end_time': data['end_time']
    }
    events.append(event)
    save_events(events)
    return jsonify(event), 201

# Get All Events (Sorted by Start Time)
@app.route('/events', methods=['GET'])
def get_events():
    sorted_events = sorted(events, key=lambda x: datetime.strptime(x['start_time'], '%Y-%m-%d %H:%M'))
    return jsonify(sorted_events), 200

# Update Event
@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.json
    for event in events:
        if event['id'] == event_id:
            event.update({k: data[k] for k in data if k in event})
            save_events(events)
            return jsonify(event), 200
    return jsonify({'error': 'Event not found'}), 404

# Delete Event
@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    global events
    events = [event for event in events if event['id'] != event_id]
    save_events(events)
    return jsonify({'message': 'Event deleted'}), 200

# Search Events
@app.route('/events/search', methods=['GET'])
def search_events():
    keyword = request.args.get('q', '')
    filtered = [e for e in events if keyword.lower() in e['title'].lower() or keyword.lower() in e['description'].lower()]
    return jsonify(filtered), 200

if __name__ == '__main__':
    app.run(debug=True)
