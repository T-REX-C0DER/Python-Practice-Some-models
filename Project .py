import csv
import os
from datetime import datetime
from statistics import mean

DATA_FILE = "daily_logs.csv"


def init_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                "date", "study_hours", "focus", "sleep_hours",
                "practice_done", "distraction_minutes"
            ])


def log_daily_data():
    print("\n📥 Enter Today's Academic Data")
    study = float(input("Study hours: "))
    focus = int(input("Focus level (1-5): "))
    sleep = float(input("Sleep hours: "))
    practice = input("Practice done (yes/no): ").lower()
    distraction = int(input("Distraction time (minutes): "))

    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().date(), study, focus, sleep,
            1 if practice == 'yes' else 0, distraction
        ])

    print("✅ Data saved successfully")



def load_last_14_days():
    with open(DATA_FILE, mode='r') as file:
        rows = list(csv.DictReader(file))
        return rows[-14:]



def calculate_averages(data):
    return {
        "study": mean(float(d["study_hours"]) for d in data),
        "focus": mean(int(d["focus"]) for d in data),
        "sleep": mean(float(d["sleep_hours"]) for d in data),
        "practice": mean(int(d["practice_done"]) for d in data),
        "distraction": mean(int(d["distraction_minutes"]) for d in data)
    }


def analyze_trends():
    data = load_last_14_days()

    if len(data) < 14:
        print("⚠️ Need at least 14 days of data for drift analysis")
        return

    prev_week = data[:7]
    recent_week = data[7:]

    prev_avg = calculate_averages(prev_week)
    recent_avg = calculate_averages(recent_week)

    focus_down = recent_avg["focus"] < prev_avg["focus"]
    practice_down = recent_avg["practice"] < prev_avg["practice"]
    distraction_up = recent_avg["distraction"] > prev_avg["distraction"]

    print("\n📊 Weekly Trend Report")
    print(f"Study Hours: {prev_avg['study']:.1f} → {recent_avg['study']:.1f}")
    print(f"Focus Level: {prev_avg['focus']:.1f} → {recent_avg['focus']:.1f}")
    print(f"Sleep Hours: {prev_avg['sleep']:.1f} → {recent_avg['sleep']:.1f}")
    print(f"Practice Consistency: {prev_avg['practice']:.1f} → {recent_avg['practice']:.1f}")
    print(f"Distraction Minutes: {prev_avg['distraction']:.1f} → {recent_avg['distraction']:.1f}")

    drift_score = sum([focus_down, practice_down, distraction_up])

    print("\n🧠 Drift Analysis")

    if drift_score >= 2:
        print("⚠️ Academic Drift Detected")
        if focus_down:
            print("• Focus is declining — try shorter, deeper sessions")
        if practice_down:
            print("• Practice consistency reduced — revise fundamentals")
        if distraction_up:
            print("• Distractions increased — limit screen time")
    else:
        print("✅ No major drift detected. Keep going!")



def main():
    init_file()

    while True:
        print("\n🎓 Academic Drift Detector")
        print("1. Log today's data")
        print("2. Analyze academic drift")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            log_daily_data()
        elif choice == '2':
            analyze_trends()
        elif choice == '3':
            print("👋 Goodbye. Stay consistent!")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()