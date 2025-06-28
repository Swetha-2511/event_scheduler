
# 📅 Event Scheduler System (Python Flask REST API)

A simple backend system for managing events (creating, listing, updating, deleting, and searching) using Python 3.x, Flask, and REST API principles.

## ✅ Features

- Create new events
- View all scheduled events (sorted by start time)
- Update event details
- Delete events
- Search for events by title or description
- Data Persistence using a local JSON file (`events.json`)
- Postman Collection provided for easy testing

## ✅ Technologies Used

- Python 3.x
- Flask (Python web framework)
- JSON for data persistence
- Postman (for API testing)

## ✅ Setup Instructions

### 1. Prerequisites

- Python 3.x installed
- Pip (Python package installer)
- (Optional) Postman app for API testing

### 2. Installing Dependencies

First, navigate to your project folder.

```bash
cd path/to/event_scheduler_project
```

If you want, create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate          # On Linux/Mac
venv\Scripts\activate             # On Windows
```

Now, install Flask:

```bash
pip install Flask
```

### 3. Running the Flask Server

```bash
python app.py
```

✅ If successful, you’ll see:

```
* Running on http://127.0.0.1:5000
```

## ✅ API Endpoints

| Function | Method | URL | Body Format |
|---|---|---|---|
| Create Event | POST | `/events` | JSON |
| Get All Events | GET | `/events` | None |
| Update Event | PUT | `/events/<id>` | JSON |
| Delete Event | DELETE | `/events/<id>` | None |
| Search Events | GET | `/events/search?q=<keyword>` | None |

## ✅ Example Commands and Outputs

### ✔️ Example: Create Event (POST `/events`)

**POST Body (JSON):**

```json
{
    "title": "Team Meeting",
    "description": "Discuss project status",
    "start_time": "2025-06-28 19:00",
    "end_time": "2025-06-28 20:00"
}
```

**Example Response:**

```json
{
    "id": 1,
    "title": "Team Meeting",
    "description": "Discuss project status",
    "start_time": "2025-06-28 19:00",
    "end_time": "2025-06-28 20:00"
}
```

### ✔️ Example: Get All Events (GET `/events`)

```json
[
    {
        "id": 1,
        "title": "Team Meeting",
        "description": "Discuss project status",
        "start_time": "2025-06-28 19:00",
        "end_time": "2025-06-28 20:00"
    }
]
```

### ✔️ Example: Update Event (PUT `/events/1`)

**PUT Body:**

```json
{
    "description": "Updated: Status discussion with full team"
}
```

### ✔️ Example: Delete Event (DELETE `/events/1`)

```json
{
    "message": "Deleted"
}
```

### ✔️ Example: Search Event (GET `/events/search?q=team`)

```json
[
    {
        "id": 1,
        "title": "Team Meeting",
        "description": "Discuss project status",
        "start_time": "2025-06-28 19:00",
        "end_time": "2025-06-28 20:00"
    }
]
```

## ✅ Data Persistence (events.json)

All events are automatically saved in a file called:

```
events.json
```

Even after stopping and restarting the server, your data will remain.

## ✅ Postman Collection

A ready-made Postman Collection is included:

File:

```
Event_Scheduler_API_Collection.json
```

You can import this file directly into Postman and test all the APIs.

## ✅ Optional Improvements (For future):

- Event Reminders
- Recurring Events (Daily, Weekly, Monthly)
- Email Notifications
- User Authentication
- Frontend UI for easier access

## ✅ Author

Swetha
