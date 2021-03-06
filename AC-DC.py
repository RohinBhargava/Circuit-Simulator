!/usr/bin/env python

import operator
class circuitBoard:
  def __init__(self):
    self.resistors = list()
    self.voltage = 1.0
    self.current = 1.0
    self.voltageDrops = list()
    self.currents = list()
    self.powers = list()
  def addResistor(self, resistance):
    self.resistors.append(resistance)
  def setVoltage(self, voltage):
    self.voltage = voltage
  def setCurrent(self, current):
    self.current = current
  def calculateVoltage(self):
    voltage = self.voltage
    current = self.current
    voltageDrops = list()
    currents = list()
    sr = self.resistors
    i = 0
    while i < len(sr):
      if sr[i][0] == 's':
        voltage = voltage/(sr[i][1] * current)
        voltageDrops.append(voltage)
        currents.append(current)
      elif sr[i][0] == 'ps':
        return None
      else:
        resistance = list()
        counter = list()
        j = -1
        while i < len(sr) and (sr[i][0] == 'p' or sr[i][0] == 'ps'):
          if sr[i][0] == 'p':
            resistance.append(sr[i][1])
            j += 1
          else:
            resistance[j] += sr[i][1]
          i += 1
        for l in resistance:
          cur = current - float(l)/sum(resistance)
          voltageDrops.append(voltage - cur * l)
          currents.append(cur)
        voltage = voltageDrops[len(voltageDrops) - 1]
      i += 1
    self.voltageDrops = voltageDrops
    self.currents = currents
    self.powers = [a * b for a,b in zip(voltageDrops, currents)]

def main():
  x = circuitBoard()
  x.setVoltage(36.0)
  x.setCurrent(1.1)
  for r in [('s',4),('p',3),('ps',4),('p',6),('s',3)]:
    x.addResistor(r);
  print 'Voltage: ', x.voltage
  print 'Current:', x.current
  x.calculateVoltage()
  print 'Voltages after resistors: ', x.voltageDrops
  print 'Currents after resistors: ', x.currents
  print 'Powers after resistors: ', x.powers

main()
