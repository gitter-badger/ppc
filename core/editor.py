import json

import  wx
import  wx.stc  as  stc

from os import path

CWD = path.abspath(path.dirname('__main__'))


class Editor(stc.StyledTextCtrl):
    """Editeurs
    """
    def __init__(self, parent, ID, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
        stc.StyledTextCtrl.__init__(self, parent, ID, pos, size, style)

        self.prnt = parent

        #Editor
        self.SetEdgeMode(stc.STC_EDGE_BACKGROUND)
        self.SetEdgeColumn(78)
        self.SetWrapMode(1)
        self.SetWrapVisualFlags(1)

        #ZOOM & autres
        self.CmdKeyAssign(ord('B'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMIN)
        self.CmdKeyAssign(ord('N'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMOUT)
        self.CmdKeyAssign(ord('W'), stc.STC_SCMOD_CTRL, stc.STC_CMD_WORDRIGHT)
        self.CmdKeyAssign(ord('W'), stc.STC_SCMOD_CTRL | stc.STC_SCMOD_SHIFT, stc.STC_CMD_WORDLEFT)

        #FOLDING & Margin
        #self.SetKeyWords(4, " ".join(PHPKEYWORDS))
        self.SetMarginType(1, wx.stc.STC_MARGIN_NUMBER)
        self.SetMarginMask(2, stc.STC_MASK_FOLDERS)
        self.SetProperty("fold", "1")
        self.SetProperty("fold.html", "1")
        self.SetMargins(2,2)
        self.SetMarginSensitive(2, True)
        self.SetMarginWidth(1, 15)
        self.SetMarginWidth(2, 12)

        self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPEN,   stc.STC_MARK_BOXMINUS,        "white", "#808080")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDER,       stc.STC_MARK_BOXPLUS,          "white", "#808080")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDERSUB,     stc.STC_MARK_VLINE,             "white", "#808080")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDERTAIL,   stc.STC_MARK_LCORNER,          "white", "#808080")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDEREND,     stc.STC_MARK_BOXPLUSCONNECTED,  "white", "#808080")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_BOXMINUSCONNECTED, "white", "#808080")
        self.MarkerDefine(stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_TCORNER,         "white", "#808080")

        #INDENTATION
        self.SetIndent(4)
        self.SetIndentationGuides(True)
        self.SetBackSpaceUnIndents(True)
        self.SetTabIndents(True)
        self.SetTabWidth(4)
        self.SetUseTabs(True)
        self.SetHighlightGuide(0)

        #HIGHLIGHT & others
        self.SetStyleBits(7)
        self.SetViewWhiteSpace(False)
        self.SetCaretWidth(1)
        #self.SetControlCharSymbol(0)
        self.SetCaretLineVisible(True)
        self.SetCaretLineBack(wx.Colour(250, 254, 255))
        self.SetCaretForeground("#1A1A1A")

        self.SetLexer(stc.STC_LEX_HTML)

        datas_path = CWD + '/datas'
        php_lex = datas_path + '/lex_php.json'
        #php_funx = datas_path + '/funx_php.json'

        fo = open(php_lex, 'r')
        fr = fo.read()
        fo.close()
        datas = json.loads(fr)

        for i in datas['styles']:
            self.StyleSetSpec(eval(i['id']), str(i['val']))

        for i in datas['keywords']:
            self.SetKeyWords(int(i['index']), str(i['value']))
