from midiutil.MidiFile import MIDIFile
import numpy as np

# You can adjust the below parameters to adjust the number of notes generated, the tonic note, and major or minor.
# You can play the generated midi file using musescore or another program.

MIDDLE_C = 60
N = 150 # number of notes
major = True # false would be minor
tonic_pitch = MIDDLE_C + 3  # Eb

def catalan(n,k):
    ''' Returns a numpy array of catalan numbers mod k '''
    # Table to store results of subproblems
    catalan = np.zeros(n+1, dtype=int)

    # Initialize first two values in table
    catalan[0] = 1
    catalan[1] = 1

    # Fill entries in catalan[] using recursive formula
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]
            catalan[i] %= k

    # return array
    return catalan

catalan_arr_mod_7 = catalan(N,7)
catalan_arr_mod_5 = catalan(N,5)

W = 2 # whole step
H = 1 # half step
major_jumps_arr = np.array([0,W,W,H,W,W,W], dtype=int)
minor_jumps_arr = np.array([0,W,H,W,W,H,W], dtype=int)

np.cumsum(major_jumps_arr, out=major_jumps_arr)
np.cumsum(minor_jumps_arr, out=minor_jumps_arr)

duration_arr = np.array([1/4,1/2,1,2,4])

# Create midi file
mf = MIDIFile(1)     # only 1 track
track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 120)

channel = 0
volume = 100

for jj in range(0,N):
    jump_index = catalan_arr_mod_7[jj]
    if major: pitch = tonic_pitch + major_jumps_arr[jump_index]
    else: pitch = tonic_pitch + minor_jumps_arr[jump_index]

    duration_index = catalan_arr_mod_5[jj]
    duration = duration_arr[duration_index]

    mf.addNote(track, channel, pitch, time, duration, volume)
    time+=duration

# write it to disk
with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)
