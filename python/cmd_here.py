import _winreg

def InstallSelf():
  rootkey = _winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT, "AllFilesystemObjects")
  shellkey = _winreg.CreateKey(rootkey, "shell")
  peskey = _winreg.CreateKey(shellkey, "Command Prompt Here")
  cmdkey = _winreg.CreateKey(peskey, "command")
  _winreg.SetValue(cmdkey, "", _winreg.REG_SZ, "cmd.exe /k cd \"%L\"")

if __name__ == "__main__":
  InstallSelf()
