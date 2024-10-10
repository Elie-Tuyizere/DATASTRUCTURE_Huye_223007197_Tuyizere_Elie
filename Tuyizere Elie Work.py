from collections import deque

scheduled_interviews = deque()
undo_stack = []
candidates = []
def schedule(candidate, interviewer, time):
    scheduled_interviews.append((candidate, interviewer, time))
    undo_stack.append(('schedule', candidate, interviewer, time))
    #print(f"Interview scheduled for {candidate} with {interviewer} at {time}.")

def undo():
    if undo_stack:
        action, candidate, interviewer, time = undo_stack.pop()
        if action == 'schedule':
            scheduled_interviews.remove((candidate, interviewer, time))
            print(f"Undo scheduling: Interview for {candidate} has been removed.")

def add_candidate(info):
    candidates.append(info)
    print(f"{info['name']} added to the candidate pool.")

def display():
    print("Scheduled interviews:")
    for candidate, interviewer, time in scheduled_interviews:
        print(f"- {candidate} with {interviewer} at {time}")

schedule("ALICE", "Interviewer A", "10:00 AM")
schedule("MUGENGA", "Interviewer B", "11:00 AM")
schedule("KAMANA", "Interviewer C", "11:00 AM")
schedule("KAMALI", "Interviewer D", "11:00 AM")
schedule("JAMES", "Interviewer E", "11:00 AM")
undo()
undo()

display()