import _winreg
import sys
import os

def InstallSelf():
  rootkey = _winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT, "*")
  shellkey = _winreg.CreateKey(rootkey, "shell")

  peskey = _winreg.CreateKey(shellkey, "Open with IDA")
  cmdkey = _winreg.CreateKey(peskey, "command")
  _winreg.SetValue(cmdkey, "", _winreg.REG_SZ, os.path.join(sys.argv[1], 'idaq.exe') + ' "%L"')

  peskey64 = _winreg.CreateKey(shellkey, "Open with IDA64")
  cmdkey64 = _winreg.CreateKey(peskey64, "command")
  _winreg.SetValue(cmdkey64, "", _winreg.REG_SZ, os.path.join(sys.argv[1], 'idaq64.exe') + ' "%L"')

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print 'USAGE: idahere.py IDA_DIR'
  InstallSelf()
