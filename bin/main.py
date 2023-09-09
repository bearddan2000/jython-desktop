from javax.swing import *
from java.awt import *

class JythonDesktop:
  def __init__(self):
    self.data = ('red','green','blue')
    self.createFrame()

  def createFrame(self):
    frame = JFrame("Jython Desktop")
    frame.setSize(300, 75)
    frame.setLayout(FlowLayout())

    self.createCombo(frame)
    self.createLabel(frame)

    frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
    frame.setVisible(True)

  def createCombo(self, frame):
      self.cb = JComboBox(self.data, itemStateChanged=self.cbSelect)
      frame.add(self.cb)

  def createLabel(self, frame):
      self.label = JLabel(self.data[0])
      self.label.setForeground(Color.red)
      frame.add(self.label)

  def cbSelect(self,event):
    selected = self.cb.selectedIndex
    data = self.data[selected]
    c = Color.black
    if selected == 0:
        c = Color.red
    elif selected == 1:
        c = Color.green
    else:
        c = Color.blue

    self.label.setForeground(c)
    self.label.text = data


if __name__ == '__main__':
        JythonDesktop()
