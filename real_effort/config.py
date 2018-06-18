import random

# Dictionary Format: endowment, multiplier, tax, transcription
# Each dictionary entry represents the data values for 1 round
data = [
    [ 
        {"end": 100, "multiplier": 2, "tax": 0.2, "transcription": False, "mode": 2},
        {"end": 100, "multiplier": 2, "tax": 0.2, "transcription": False, "mode": 2},
        {"end": 100, "multiplier": 2, "tax": 0.2, "transcription": False, "mode": 2},
        {"end": 100, "multiplier": 1.5, "tax": 0.2, "transcription": False, "mode": 2},
        {"end": 100, "multiplier": 1.5, "tax": 0.2, "transcription": False, "mode": 2},
        {"end": 100, "multiplier": 1.5, "tax": 0.2, "transcription": False, "mode": 2}
    ]
]

def shuffle(data):
    # random.sample does not shuffle data in place. random.shuffle would work in this case but
    # could lead to bugs if we are say trying to write the data to csv after having used
    # it in the experiment.
    return [random.sample(data[0], k=len(data[0]))]

def export_data():
    return shuffle(data)