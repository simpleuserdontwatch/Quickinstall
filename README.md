# Quickinstall
The most useful thing to quickly install windows to a harddrive

# Requirements
- Python 3 (or use a portable version)
- 7z
- A empty hard drive or flash drive (Make sure its formatted into FAT32 format)

# FAQ (generated by ai lol)
- Q: What does this program do?

- A: This Python program creates a GUI application using the Tkinter library. It allows users to install Windows partitions without having to boot from a CD. It prompts the user for the path of the Windows installation file (install.wim), the drive letter on which to install Windows, and the path to the 7-Zip executable. It then validates the inputs, formats the specified drive, extracts the install.wim file using 7-Zip, and applies the install.wim using the bcdboot command. Finally, it displays a message box indicating that the installation is complete.

- Q: How do I run this program?

- A: To run this program, you need to have Python installed on your system. You also need to have the tkinter and ttk libraries installed. Once you have these dependencies installed, you can simply execute the Python script, and the GUI application will launch.

- Q: What are the dependencies for this program?

- A: This program relies on the following dependencies:

Python: This program requires Python to be installed on your system.
Tkinter: This program uses the Tkinter library to create the GUI application.
ttk: This program uses the ttk module from the Tkinter library to create themed widgets.
- Q: How can I install the required dependencies?

- A: To install Python, you can visit the official Python website (python.org) and download the latest version for your operating system. Once Python is installed, you can use the pip package manager to install the required dependencies. Open a terminal or command prompt and run the following commands:
```
pip install tkinter
pip install ttk
```
- Q: How do I specify the path of the install.wim file?

- A: In the GUI application, there is an entry field labeled "File". You can click on this entry field and enter the path of the install.wim file. The install.wim file is typically found on a Windows installation CD or can be extracted from a Windows ISO file using 7-Zip.

- Q: What should I specify for the "Drive" field?

- A: In the "Drive" field, you should specify the drive letter on which you want to install Windows. For example, if you want to install Windows on drive C, you should enter "C" in the "Drive" field.

- Q: How do I specify the path to the 7-Zip executable?

- A: In the GUI application, there is an entry field labeled "7z executable path". You can click on this entry field and enter the path to the 7-Zip executable. If you don't have 7-Zip installed, you can download it from the official 7-Zip website (7-zip.org/download.html). Once you have 7-Zip installed, you can copy the files of the 7-Zip program to a location on your system and specify the path to the 7z.exe file in the "7z executable path" field.

- Q: How can I format the drive and apply the install.wim using this program?

- A: To format the specified drive and apply the install.wim file, you can click on the "Install!" button in the GUI application. It will prompt you with a confirmation message box asking if you are sure. If you click "Yes", it will then display another confirmation message box asking if you are actually sure, as the data on the drive will be formatted. If you click "Yes" again, the program will format the drive, extract the install.wim file using 7-Zip, and apply the install.wim using the bcdboot command. Finally, it will display a message box indicating that the installation is complete.
