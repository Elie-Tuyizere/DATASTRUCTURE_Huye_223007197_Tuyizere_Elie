from collections import deque

scheduled_interviews = deque()
undo_stack = []
candidates = [["1","Ange","Interviewer A","10:00 AM"],
              ["2","Aime","Interviewer C","11:00 AM"],
              ["3","Jack","Interviewer C","10:00 AM"],["4","Cyus","Interviewer C","10:00 AM"]]
def schedule(no,candidate, interviewer, time):
    scheduled_interviews.append((no,candidate, interviewer, time))
    undo_stack.append(('schedule', no,candidate, interviewer, time))

def undo():
    if undo_stack:
        action, no, candidate, interviewer, time = undo_stack.pop()
        if action == 'schedule':
            scheduled_interviews.remove((no, candidate, interviewer, time))
            print(f"Undo scheduling: Interview for {candidate} has been removed.")

def display():
    print("Scheduled interviews:")
    for no, candidate, interviewer, time in scheduled_interviews:
        print(f"- {no}. {candidate} with {interviewer} at {time}")

    
schedule("1","ALICE", "Interviewer A", "10:00 AM")
schedule("2","MUGENGA", "Interviewer B", "11:00 AM")
schedule("3","KAMANA", "Interviewer C", "11:00 AM")
schedule("4","KAMALI", "Interviewer D", "11:00 AM")
import queue

# Create a queue to store schedules
schedule_queue = deque()

# Enqueue operations
schedule_queue.append(("1", "ALICE", "Interviewer A", "10:00 AM"))
schedule_queue.append(("2", "MUGENGA", "Interviewer B", "11:00 AM"))
schedule_queue.append(("3", "KAMANA", "Interviewer C", "11:00 AM"))
schedule_queue.append(("4", "KAMALI", "Interviewer D", "11:00 AM"))

print("\n Candidates Enqueue  \n")

    
print("\n Candidates after deque \n")
schedule_queue.popleft()
for schedule_queue in schedule_queue:
    print("  ".join(schedule_queue))

print("-------------------------------------------")
print("\n Display a list of candidates \n")
for candidate in candidates:
    print("  ".join(candidate))
candidates.pop()
print("\n Display a list of candidates After remove \n")
for candidate in candidates:
    print("  ".join(candidate))
print("---------------------------------------------")
print("\n Candidates Pushed in stack \n")
display()
undo()
print("\n Candidates after Pop in stack \n")
display()
