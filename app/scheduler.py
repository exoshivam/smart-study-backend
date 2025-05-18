from datetime import datetime, timedelta

def generate_schedule(data):
    subjects = data["subjects"]       # List of {"name": "Math", "syllabus": 10, "difficulty": 3}
    exam_dates = data["examDates"]    # Dict {"Math": "2025-06-01"}
    hours_per_day = data["hoursPerDay"]

    today = datetime.today()
    schedule = []

    # Sort by exam dates
    subjects.sort(key=lambda x: exam_dates[x["name"]])

    for subject in subjects:
        name = subject["name"]
        syllabus = subject["syllabus"]
        difficulty = subject["difficulty"]
        exam_date = datetime.strptime(exam_dates[name], "%Y-%m-%d")

        days_left = (exam_date - today).days
        total_slots = days_left * hours_per_day
        time_per_unit = max(1, int(total_slots / (syllabus * difficulty)))

        for i in range(syllabus):
            study_date = today + timedelta(days=i % days_left)
            schedule.append({
                "date": study_date.strftime("%Y-%m-%d"),
                "subject": name,
                "topic": f"Part {i + 1}",
                "duration": time_per_unit
            })

    return schedule
