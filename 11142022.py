from earsketch import *

init()
setTempo(120)

MyIntro = HOUSE_SFX_WHOOSH_001
MyBeat = HOUSE_MAIN_BEAT_008
MyBass = HOUSE_DEEP_BASS_001
MyLead_1 = HOUSE_DEEP_ARPLEAD_001
MyLead_2 = HOUSE_DEEP_CRYSTALCHORD_001

MySound1 = DANGERMSE_CODER_DOJO_01
beat = "0++00-00-0+++0+0++++++"

# using iteration instead of repeating similar lines of code
for measure in range(11, 16, 2):
    makeBeat(MySound1, 3, measure, beat)

fitMedia(MyIntro, 1, 1, 3)
fitMedia(MyBass, 1, 2.5, 25)
fitMedia(MyLead_1, 2, 3, 10)
fitMedia(MyLead_2, 2, 10, 17)
fitMedia(MyLead_1, 2, 17, 25)

finish()