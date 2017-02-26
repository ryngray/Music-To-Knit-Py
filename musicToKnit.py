from music21 import *

weight=raw_input("Enter the weight of yarn").lower()
knitThing = raw_input("Enter what you would like to make").lower()
size=raw_input("Enter the size").lower()
music = raw_input("Enter the music to be based on")

#Circumference of head in inches
SCirc = 18
MCirc = 20
LCirc = 22
XLCirc = 23.5
XXLCirc = 24.5

#stitches per inch by yarn weight
Lace=40/4
Fingering=28/4
Sport = 24/4
DK=20/4
Worsted=16/4
Bulky = 12/4
SuperBulky=8/4

def createThing(listy):
    noteslist=[0,0,0,0,0,0,0,0,0,0,0,0]
    for n in listy:
        if n.name=="C" or n.name=="B+":
            noteslist[0]+=1
        elif n.name=="D-" or n.name=="C+":
            noteslist[1]+=1
        elif  n.name=="D":
            noteslist[2]+=1
        elif n.name=="D+" or n.name=="E-":
            noteslist[3]+=1
        elif n.name=="E" or n.name=="F-":
            noteslist[4]+=1
        elif n.name=="F" or n.name=="E+":
            noteslist[5]+=1
        elif n.name=="G-" or n.name=="F+":
            noteslist[6]+=1
        elif n.name=="G":
            noteslist[7]+=1
        elif n.name=="G+" or n.name=="A-":
            noteslist[8]+=1
        elif n.name=="A":
            noteslist[9]+=1
        elif n.name=="A+" or n.name=="B-":
            noteslist[10]+=1
        elif n.name=="B" or n.name=="C-":
            noteslist[11]+=1
    pstitch=0
    kstitch=0
    pklist=[]
    for item in noteslist:
        if item > 10:
            pklist.append(pstitch)
            kstitch+=1
            pstitch=0
        else:
            pklist.append(kstitch)
            pstitch+=1
            kstitch=0
    pklist.append(kstitch)
    pklist.append(pstitch)
    purl=False
    for stitchvalue in pklist:
        if stitchvalue!=0:
            if not purl:
                if stitchvalue==1:
                    print "Knit", stitchvalue, "stitch,",
                else:
                    print "Knit",stitchvalue,"stiches,",
                purl=True
            else:
                if stitchvalue==1:
                    print "Purl", stitchvalue, "stitch,",
                else:
                    print "Purl", stitchvalue, "stitches,",
                purl=False
    print "\nRepeat till end of row"

Circ=0
if size=="s" or size=="small":
    Circ = SCirc
elif size=='m' or size=='medium':
    Circ=MCirc
elif size=='l' or size=='large':
    Circ=LCirc
elif size=="xl" or size =="xlarge" or size == "x large" or size == "extra large" or size =="extralarge":
    Circ=XLCirc
else:
    size == XXLCirc

spi=0
if weight=="lace":
    spi=Lace
elif weight=="fingering":
    spi=Fingering
elif weight=="sport":
    spi=Sport
elif weight=="dk":
    spi=DK
elif weight=="worsted":
    spi=Worsted
elif weight=="bulky":
    spi=Bulky
else:
    spi=SuperBulky


numstitches=spi*Circ

rib=2
otherRib=2
if numstitches%4==0:
    rib=2
    otherRib=2
elif numstitches%3==0:
    rib = 1
    otherRib=2
else:
    rib=3
    otherRib=2
print "Cast on",numstitches,"stitches"
print "Work two inches in rib of your choice.  We suggest", rib, "by", otherRib

print("Stitch pattern")
print("This is what is based on the music")

lace=False
cables=False
s=corpus.parse(music)
sopr= s.parts['Soprano']
alto=s.parts['Alto']
tenor=s.parts['Tenor']
bass=s.parts['Bass']
#print s.analyze('key')
array=[]
allNotes=s.flattenParts()
if allNotes.recurse().getElementsByClass(meter.TimeSignature)[0]==meter.TimeSignature('6/8'):
    lace=True
octave=[0,0,0,0,0]
for note in allNotes.pitches:
    if note.octave==1:
        octave[0]+=1
    elif note.octave==2:
        octave[1]+=1
    elif note.octave==3:
        octave[2]+=1
    elif note.octave==4:
        octave[3]+=1
    elif note.octave==5:
        octave[4]+=1

if (octave[4]>octave[0] and octave[4]>octave[1] and octave[4]>octave[2]) or (octave[3]>octave[0] and octave[3]>octave[1] and octave[3]>octave[2]):
    cables=False
if (octave[0]>octave[4]and octave[0]>octave[3] and octave[0]>octave2) or (octave[1]>octave[2] and octave[1]>octave[3] and octave[1]>octave[4]):
    lace=False

if cables==False and lace==False:
    if numstitches%12!=0:
        print "Over the next row, increase", numstitches%12, "stitches"
    createThing(alto.flat.notes)
    createThing(sopr.flat.notes)
    createThing(bass.flat.notes)
    createThing(tenor.flat.notes)
    print "Repeat these four rows until desired length"
    print "Decrease Rows"
    print "Continue in pattern as well as you're able, or switch to knit one row, purl one row
    print "knit 10, k2tog* around or continue in pattern, decreasing one every twelve stitches"
    print "purl or continue in pattern"
    print "continue previous two rows, knitting one less before the decrease, until 8 stitches remain between each decrease set"
    print "knit 6, k2tog*"
    print "repeat last row, knitting one less before the decrease until you reach the row where there are no stitches before the decrease"
    print "cut yarn and pull through remaining stitches"


#print pklist
#print noteslist
#print octave
#print "soprano"
#for n in sopr.flat.notes:
    #print (n, n.beatStr)
#print "Alto"
#for n in alto.flat.notes:
    #print (n, n.beatStr)
#print "tenor"
#for n in tenor.flat.notes:
    #print (n, n.beatStr)
#print "bass"
#for n in bass.flat.notes:
    #print (n, n.beatStr)
#for oc in octave:
    #print oc
