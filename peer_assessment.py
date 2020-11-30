# py peer_assessment {namafile.csv} {list NIM orang dipisahkan koma}
import csv
import sys
from dataclasses import dataclass
from constant import *
import re

class NilaiOrang:
  def __init__(self, nim):
    self.nim = nim
    self.arrNilai = []
  
  def addNilai(self, nilai):
    self.arrNilai.append(int(nilai))

  def getAvg(self):
    try:
      return sum(self.arrNilai) / len(self.arrNilai)
    except ZeroDivisionError:
      return 0
  
  def printAverage(self):
    print(f"Rata rata nilai dari peer NIM {self.nim} adalah {self.getAvg()}")

class CsvRow:
  def __init__(self, data):
    self.timestamp = data[TIMESTAMP]
    self.email = data[EMAIL]
    self.nim = data[NIM]
    self.nilai_sendiri = data[NILAI_SENDIRI]
    self.mulai_nilai_temen = data[MULAI_NIM_TEMEN:]

def generateOrangs(nimList):
  orangs = [NilaiOrang(nim) for nim in nimList]
  return orangs

def checkIfNim(nim):
  span = re.match("^[0-9]*", nim).span()
  NIMLength = 8

  # check if number
  if(span == (0, 0)):
    return False
  # check length
  if(span[1] - span[0] != NIMLength):
    return False
  return True

def getAvgOfNIM(nim):
  with open(sys.argv[1]) as csv_file:
      NIMOrang = nim
      nilaiOrang = NilaiOrang(NIMOrang)
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
          if line_count == 0:
            line_count += 1
          else:
            csvRow = CsvRow(row)
            isNilai = False
            for csvData in csvRow.mulai_nilai_temen:
              if(isNilai == True):
                isNilai = False
                nilaiOrang.addNilai(csvData)
              elif(checkIfNim(csvData)):
                if(csvData == nilaiOrang.nim):
                  isNilai = True
          line_count += 1
      nilaiOrang.printAverage()

if __name__ == "__main__":
  listOfNim = sys.argv[2].split(",")
  for nim in listOfNim:
    getAvgOfNIM(nim)