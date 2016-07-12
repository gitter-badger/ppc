#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx
import wx.aui
from core import editor

from os import path

WAI = path.abspath(path.dirname(__file__))


class PhPyCli(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.statusbar = self.CreateStatusBar(2, 0)

        self.__set_properties()

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.nb = wx.aui.AuiNotebook(self)
        #page = wx.TextCtrl(self.nb, -1, '<?php\n\n?>\n', style=wx.TE_MULTILINE)
        page = editor.Editor(self, -1)
        page.SetText("<?php\n\n?>\n")
        self.nb.AddPage(page, "sans titre")

        rightctl = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE)

        top_sizer.Add(self.nb, 2, wx.EXPAND)
        top_sizer.Add(rightctl, 1, wx.EXPAND)

        bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)

        txtctl = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE)
        bottom_sizer.Add(txtctl, 1, wx.EXPAND)

        main_sizer.Add(top_sizer, 3, wx.EXPAND)
        main_sizer.Add(bottom_sizer, 1, wx.EXPAND)

        self.SetSizer(main_sizer)
        self.Layout()

    def __set_properties(self):
        self.SetTitle("PhPyCli")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap(WAI + "/icons/ppc-32x32.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((1024, 780))
        self.statusbar.SetStatusWidths([-1, -1])
        statusbar_fields = ["infos", "timer"]
        for i in range(len(statusbar_fields)):
            self.statusbar.SetStatusText(statusbar_fields[i], i)


def main():
    app = wx.App(False)
    main_window = PhPyCli(None, -1, "")
    app.SetTopWindow(main_window)
    main_window.Show()
    app.MainLoop()

if __name__ == '__main__':
	main()
