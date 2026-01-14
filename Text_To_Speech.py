import pyttsx3
import os

engine = pyttsx3.init()

# BASIC CONFIG 
def set_rate(rate=170):
    engine.setProperty('rate', rate)

def set_volume(volume=1.0):
    engine.setProperty('volume', volume)

def show_voices():
    voices = engine.getProperty('voices')
    for i, v in enumerate(voices):
        print(f"{i}. {v.name} ({v.languages})")

def set_voice(index=0):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[index].id)

# CORE FUNCTIONS 
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def save_to_file(text, filename="output.mp3"):
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print(f"✅ Audio saved as: {filename}")

def read_from_file(filepath):
    if not os.path.exists(filepath):
        print("❌ File not found!")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    speak_text(text)

# MENU SYSTEM
def menu():
    print("\n" + "="*50)
    print("🎙️ TEXT TO SPEECH CONVERTER (pyttsx3)")
    print("="*50)
    print("1. Speak text")
    print("2. Change voice")
    print("3. Change speed")
    print("4. Change volume")
    print("5. Save speech to audio file")
    print("6. Read text from file and speak")
    print("7. Exit")

while True:
    menu()
    choice = input("\nEnter your choice: ")

    if choice == "1":
        text = input("Enter text to speak:\n> ")
        speak_text(text)

    elif choice == "2":
        show_voices()
        idx = int(input("Select voice number: "))
        set_voice(idx)
        print("✅ Voice changed")

    elif choice == "3":
        rate = int(input("Enter speed (100–250 recommended): "))
        set_rate(rate)
        print("✅ Speed updated")

    elif choice == "4":
        vol = float(input("Enter volume (0.0 to 1.0): "))
        set_volume(vol)
        print("✅ Volume updated")

    elif choice == "5":
        text = input("Enter text:\n> ")
        name = input("Enter file name (example: voice.mp3): ")
        save_to_file(text, name)

    elif choice == "6":
        path = input("Enter text file path: ")
        read_from_file(path)

    elif choice == "7":
        print("👋 Exiting... Thank you!")
        break

    else:
        print("❌ Invalid choice. Try again.")
