# py self_assessment.py {nama_file csv} {list NIM orang}
import csv
import sys
from constant import *

def getSelfAssessment(nim):
  with open(sys.argv[1]) as csv_file:
    for row in csv.reader(csv_file):
      if(row[NIM] == nim):
        print(f"Self assessment nim {nim} adalah {row[NILAI_SENDIRI]}")
        break

if __name__ == "__main__":
  listNIM = sys.argv[2].split(",")
  for nim in listNIM:
    getSelfAssessment(nim)