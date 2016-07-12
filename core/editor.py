# -*- coding: UTF-8 -*-

from os import path

import json

import  wx
import  wx.stc  as  stc

CWD = path.abspath(path.dirname('__main__'))


class Editor(stc.StyledTextCtrl):
    """Editeurs
    """
    def __init__(self, parent, ID, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
        stc.StyledTextCtrl.__init__(self, parent, ID, pos, size, style)

        self.prnt = parent

        self.SetLexer(stc.STC_LEX_HTML)
        self.SetEdgeMode(stc.STC_EDGE_BACKGROUND)
        self.SetEdgeColumn(78)
        self.SetEdgeColour("#990000")
        self.SetWrapMode(1)
        self.SetWrapVisualFlags(1)

        self.CmdKeyAssign(ord('B'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMIN)
        self.CmdKeyAssign(ord('N'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMOUT)
        self.CmdKeyAssign(ord('W'), stc.STC_SCMOD_CTRL, stc.STC_CMD_WORDRIGHT)
        self.CmdKeyAssign(ord('W'), stc.STC_SCMOD_CTRL | stc.STC_SCMOD_SHIFT, stc.STC_CMD_WORDLEFT)

        self.SetProperty("fold", "1")
        self.SetProperty("fold.html", "1")
        self.SetMargins(0, 0)
        self.SetMarginType(1, wx.stc.STC_MARGIN_NUMBER)
        self.SetMarginMask(2, stc.STC_MASK_FOLDERS)
        self.SetMarginSensitive(2, True)
        self.SetMarginWidth(2, 12)

        self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPEN,    stc.STC_MARK_BOXMINUS,           "white", "#808080")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDER,        stc.STC_MARK_BOXPLUS,            "white", "#808080")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDERSUB,     stc.STC_MARK_VLINE,              "white", "#808080")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDERTAIL,    stc.STC_MARK_LCORNER,            "white", "#808080")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDEREND,     stc.STC_MARK_BOXPLUSCONNECTED,   "white", "#808080")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_BOXMINUSCONNECTED,  "white", "#808080")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_TCORNER,            "white", "#808080")

        #INDENTATION
        self.SetIndent(4)
        self.SetIndentationGuides(True)
        self.SetBackSpaceUnIndents(True)
        self.SetTabIndents(True)
        self.SetTabWidth(4)
        self.SetUseTabs(True)
        self.SetHighlightGuide(0)

        self.SetStyleBits(7)
        self.SetViewWhiteSpace(False)
        self.SetCaretWidth(1)
        #self.SetControlCharSymbol(0)
        self.SetCaretLineVisible(True)
        self.SetCaretLineBack(wx.Colour(250, 254, 255))
        self.SetCaretForeground("#1A1A1A")


        datas_path = CWD + path.sep + 'datas'
        php_lex = datas_path + path.sep + 'lex_php.json'
        #php_funx = datas_path + '/funx_php.json'

        fo = open(php_lex, 'r')
        fr = fo.read()
        fo.close()
        datas = json.loads(fr)

        for i in datas['styles']:
            self.StyleSetSpec(eval(i['id']), str(i['val']))

        for i in datas['keywords']:
            self.SetKeyWords(int(i['index']), str(i['value']))

