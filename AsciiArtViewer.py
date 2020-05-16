import wx
import os
import copy
import pathlib
import wx.adv
from wx.lib.wordwrap import wordwrap

class logger(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, pos=(1100, 50), size=(500, 800))
        self.SetBackgroundColour("#FFFFFF")

        self.log = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP)

    def addText(self, text):
        self.log.AppendText(" > " + text + "\n")

class viewer(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, pos=(50, 50), size=(980, 620))

        self.x_offset = 0
        self.y_offset = 0
        self.SetBackgroundColour("#FFFFFF")

        self.font_size = 1

        self.font = wx.Font(self.font_size, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        self.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)

        self.logger = logger(self, "Log")
        self.logger.Show()
        self.logger.addText("Press [H] for help!")
        self.logger.addText("No file has been opened! Use [o] to open a file!")

    def onOpen(self):
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(),
            defaultFile="",
            style=wx.FD_OPEN |
                  wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST |
                  wx.FD_PREVIEW
            )

        answer = dlg.ShowModal()

        if answer == wx.ID_OK:
            self.paths = dlg.GetPaths()
        else:
            return
        dlg.Destroy()

        self.logger.addText("Loading... please wait and do not switch off this window")

        f = open(self.paths[0], "r", encoding="utf8")
        self.fileContents = f.read()

        if chr(27) + "[" in self.fileContents:
            self.loadColorData()
            self.Bind(wx.EVT_PAINT, self.OnPaintANSI)
        else:
            self.Bind(wx.EVT_PAINT, self.OnPaint)

    def loadCache(self):
        dlg = wx.DirDialog(self, "Choose a directory:", style=wx.DD_DIR_MUST_EXIST | wx.DD_CHANGE_DIR)
        answer = dlg.ShowModal()

        if answer == wx.ID_OK:
            cache_path = dlg.GetPath()
        else:
            return
        dlg.Destroy()

        self.logger.addText("Loading Cache... please wait and do not switch off this window")

        try:
            f = open(cache_path + "\\rgb_cache", "r", encoding="utf8")
            self.rgb = eval(f.read())
            f.close()
            f = open(cache_path + "\\characters_cache", "r", encoding="utf8")
            self.characters = eval(f.read())
            f.close()
        except Exception as err:
            dlg = wx.MessageDialog(self, 'The path you picked does not contain both cache files!\n' + str(err),
                               'Error',
                               wx.OK | wx.ICON_ERROR
                               )
            dlg.ShowModal()
            dlg.Destroy()
            return

        self.Bind(wx.EVT_PAINT, self.OnPaintANSI)
        self.logger.addText("Finished Loading Cache")

    def createCache(self):
        dlg = wx.DirDialog(self, "Choose a destination:", style=wx.DD_DIR_MUST_EXIST | wx.DD_CHANGE_DIR)
        answer = dlg.ShowModal()

        if answer == wx.ID_OK:
            destination_path = dlg.GetPath()
        else:
            return
        dlg.Destroy()

        self.logger.addText("Creating Cache")
        try:
            if len(self.rgb) != 0:
                f = open(destination_path + "\\rgb_cache", "w", encoding="utf8")
                f.write(str(self.rgb))
                f.close()
                f = open(destination_path + "\\characters_cache", "w", encoding="utf8")
                f.write(str(self.characters))
                f.close()
        except Exception as err:
            dlg = wx.MessageDialog(self, 'Cannot create cache for non-ANSI colored text!\n' + str(err),
                                'Error',
                                wx.OK | wx.ICON_ERROR
                                )
            dlg.ShowModal()
            dlg.Destroy()
            return
        dlg1 = wx.MessageDialog(self, 'Cache successfully written',
                               'Information',
                               wx.OK | wx.ICON_INFORMATION
                               )
        dlg1.ShowModal()
        dlg1.Destroy()

    def onKeyPress(self, event):
        right_arrow = 316
        down_arrow = 317
        left_arrow = 314
        up_arrow = 315
        escape = 27

        increment = 50
        if event.GetKeyCode() == ord("f") or event.GetKeyCode() == ord("F"):
            if self.IsMaximized() == False:
                self.Maximize(True)
            else:
                self.Maximize(False)
            return
        elif event.GetKeyCode() == ord("h") or event.GetKeyCode() == ord("H"):
            info = wx.adv.AboutDialogInfo()
            info.Name = "ASCII Art Viewer Usage"
            info.Version = "0.1"
            info.Description = wordwrap(
                "Usage:\n[Arrow Keys]: Pan\n[=]: Zoom in\n[-]: Zoom out\n[H]: Show Help\n[F]: Toggle Fullscreen\n[O]: Open File\n[C]: Create cache (Only for ANSI colored text)\n[L]: Load cache (Only for ANSI colored text)\n[ESC]: Quit",
                350, wx.ClientDC(self))
            wx.adv.AboutBox(info)
            return
        elif event.GetKeyCode() == ord("l") or event.GetKeyCode() == ord("L"):
            self.loadCache()
        elif event.GetKeyCode() == ord("c") or event.GetKeyCode() == ord("C"):
            self.createCache()
            return
        elif event.GetKeyCode() == ord("o") or event.GetKeyCode() == ord("O"):
            self.onOpen()
        elif event.GetKeyCode() == escape:
            self.Destroy()
            return
        elif event.GetKeyCode() == ord("="):
            self.font_size += 1
            self.font.SetPointSize(self.font_size)
        elif event.GetKeyCode() == ord("-"):
            if self.font.GetPointSize() != 1:
                self.font_size -= 1
                self.font.SetPointSize(self.font_size)
            else:
                return
        elif event.GetKeyCode() == right_arrow:
            self.x_offset += increment
        elif event.GetKeyCode() == left_arrow:
            if self.x_offset != 0:
                self.x_offset += -increment
            else:
                return
        elif event.GetKeyCode() == up_arrow:
            if self.y_offset != 0:
                self.y_offset += -increment
            else:
                return
        elif event.GetKeyCode() == down_arrow:
            self.y_offset += increment
        else:
            return

        self.Refresh()
        self.Update()

    def renderLines(self):
        textLines = []
        previousLineY = 0
        for line in self.fileContents.split("\n"):
            previousLineY += self.font_size * 2
            textLines.append(wx.StaticText(self, -1, line, (0, previousLineY)).SetFont(self.font))

    def loadColorData(self):
        rgb_old = []
        characters_old = []

        self.rgb = [[]]
        self.characters = [[]]

        ls = self.fileContents.split(chr(27) + "[")
        for thing, i in zip(ls, range(len(ls))):
            if thing == "":
                ls.pop(i)
            if thing == "0m":
                ls.pop(i)

        for value, i in zip(ls, range(len(ls))):
            if "\n" in value:
                rgb_old.append("\n")
                characters_old.append("\n")
                continue
            rgb_old.append([])
            value = value.replace("38;2;", "")
            value = value.split(";")
            characters_old.append(value[2][-1])
            rgb_old[i].append(value[0])
            rgb_old[i].append(value[1])
            rgb_old[i].append(value[2][0:-1].replace("m", ""))
            ls[i] = value

        for rgb_val, char_val, i in zip(rgb_old, characters_old, range(len(characters_old))):
            if char_val == "\n":
                if i != len(characters_old) - 1:
                    self.rgb.append([])
                    self.characters.append([])
                continue
            self.rgb[-1].append(rgb_val)
            self.characters[-1].append(char_val)

    def OnPaint(self, event):
        self.dc = wx.PaintDC(self)
        self.dc.SetFont(self.font)

        previousLineY = 0
        for line in self.fileContents.split("\n")[self.y_offset:self.GetSize()[1] + self.y_offset]:
            previousLineY += self.font_size * 2
            self.dc.DrawText(line[self.x_offset:self.GetSize()[0] + self.x_offset], 0, previousLineY)

    def OnPaintANSI(self, event):
        self.dc = wx.PaintDC(self)
        self.dc.SetFont(self.font)

        characters = copy.deepcopy(self.characters)
        rgb = copy.deepcopy(self.rgb)

        previousLineY = 0
        self.logger.addText("Rendering Lines... please wait and do not switch off this window")
        for line_val, rgb_line_val, i in zip(characters[self.y_offset:self.GetSize()[1] + self.y_offset][self.x_offset:self.GetSize()[0] + self.x_offset], rgb[self.y_offset:self.GetSize()[1] + self.y_offset][self.x_offset:self.GetSize()[0] + self.x_offset], range(len(characters))):
            line = line_val
            rgb_line = rgb_line_val
            previousCharX = 0
            breakNested = False
            while True:
                currentRGB = rgb_line[0]
                currentString = line[0]
                line.pop(0)
                rgb_line.pop(0)
                while True:
                    if len(rgb_line) == 0:
                        self.dc.SetTextForeground(wx.Colour(int(currentRGB[0]), int(currentRGB[1]), int(currentRGB[2]), alpha=wx.ALPHA_OPAQUE))
                        self.dc.DrawText(currentString, previousCharX, previousLineY)
                        breakNested = True
                        break
                    if currentRGB == rgb_line[0]:
                        rgb_line.pop(0)
                        currentString += line[0]
                        line.pop(0)
                    else:
                        self.dc.SetTextForeground(wx.Colour(int(currentRGB[0]), int(currentRGB[1]), int(currentRGB[2]), alpha=wx.ALPHA_OPAQUE))
                        self.dc.DrawText(currentString, previousCharX, previousLineY)
                        previousCharX += len(currentString) * self.font_size
                        break
                if breakNested == True:
                    break
            previousLineY += self.font_size
        self.logger.addText("Finished Rendering Lines")

app = wx.App(False)
frame = viewer("ASCII Art Viewer")
frame.Show(True)
app.MainLoop()