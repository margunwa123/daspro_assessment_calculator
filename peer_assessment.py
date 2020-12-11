# py peer_assessment {namafile.csv} {list NIM orang dipisahkan koma}
import csv
import sys
from dataclasses import dataclass
from constant import *
import re

class ListOfNilai:
  def __init__(self):
    self.arrNilai = []
  
  def addNilai(self, nilai):
    self.arrNilai.append(int(nilai))

  def getAvg(self):
    try:
      return sum(self.arrNilai) / len(self.arrNilai)
    except ZeroDivisionError:
      return 0
  
  def printAverage(self):
    print(f"Rata rata peer adalah {self.getAvg()}")

class CsvRow:
  def __init__(self, data):
    self.timestamp = data[TIMESTAMP]
    self.email = data[EMAIL]
    self.nim = data[NIM]
    self.nilai_sendiri = data[NILAI_SENDIRI]
    self.mulai_nilai_temen = data[MULAI_NIM_TEMEN:]

class CsvPeerAssessor:
  def __init__(self, filename):
    with open(filename) as csv_file:
      self.data = []
      for row in csv.reader(csv_file, delimiter=','):
        self.data.append(row)

  def initiateNIMList(self):
    self.nimList = []
    i = 1
    while(True):
      nim = input(f"Masukan NIM ke - {i} (ketik 'stop' untuk berhenti):")
      if(nim == "stop"):
        break
      elif(not self.checkIfNim(nim)):
        print("Wrong NIM format")
      else:
        self.nimList.append(nim)
      i += 1

  def checkIfNim(self, nim):
    span = re.match("^[0-9]*", nim).span()
    NIMLength = 8

    # check if number
    if(span == (0, 0)):
      return False
    # check length
    if(span[1] - span[0] != NIMLength):
      return False
    return True

  def printAvgFromNIMList(self):
    for nim in self.nimList:
      listOfNilai = ListOfNilai()
      line_count = 0
      for row in self.data:
          if line_count == 0:
            line_count += 1
          else:
            csvRow = CsvRow(row)
            isNilai = False
            for csvData in csvRow.mulai_nilai_temen:
              if(isNilai == True):
                isNilai = False
                listOfNilai.addNilai(csvData)
              elif(csvData == nim):
                  isNilai = True
          line_count += 1
      print()
      print(f"Nilai rata rata dari NIM {nim} adalah {listOfNilai.getAvg()}")

if __name__ == "__main__":
  peerAssessor = CsvPeerAssessor(sys.argv[1])
  peerAssessor.initiateNIMList()
  peerAssessor.printAvgFromNIMList()