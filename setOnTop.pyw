# -*- coding: cp936 -*-


import win32gui, win32con
import wx

class myApp( wx.App ):

    def onExit( self ):
        win32gui.SetWindowPos( self.hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, 
                  win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
        print 'Closed'
        
class OnTopFrame( wx.Frame ):
    def __init__( self ):
        wx.Frame.__init__( self, None, -1, '�����ö�',
                           size = (250, 180) )
        self.Centre( True )
        panel = wx.Panel(self , -1)
        self.TipsLabal = wx.StaticText( panel, -1, pos = ( 15, 10 ),
                                        label= u'�������ƶ���Ҫ�ö����ں��»س�' )
        self.SecTipsLabal = wx.StaticText( panel, -1, pos = ( 40, 30 ),
                                        label= u'ע�Ᵽ�ֱ����ڴ��ڼ���״̬' )
        self.InputText = wx.TextCtrl(panel, -1, pos = (62, 55),
                                     style = wx.TE_PROCESS_ENTER | wx.TE_CENTER )
        self.Bind(wx.EVT_TEXT_ENTER, self.onEnter, self.InputText)
        self.CancelButton = wx.Button( panel, -1, '���ȡ���ö�',
                                        pos = (70, 90) )
        self.Bind( wx.EVT_BUTTON, self.OnClick, self.CancelButton )
        self.ToggleWindowStyle(wx.STAY_ON_TOP)
        



    def onEnter( self, event ):
        point = win32gui.GetCursorPos()
        self.hwnd = win32gui.WindowFromPoint( point )
        while win32gui.GetParent( self.hwnd ) != 0:            
            self.hwnd = win32gui.GetParent( self.hwnd )             
        win32gui.SetWindowPos( self.hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, 
                                win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        
    def OnClick( self, event ):
        win32gui.SetWindowPos( self.hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, 
                  win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
        self.Close( True )

if __name__ == '__main__':
    app = myApp()
    frame = OnTopFrame()
    frame.Show()
    app.MainLoop()
        


##import win32gui, win32con
##p = lambda x: x if win32gui.GetParent(x) == 0 else p(win32gui.GetParent(x))
##win32gui.SetWindowPos(p(win32gui.WindowFromPoint(win32gui.GetCursorPos())),
##    win32con.HWND_TOPMOST, 0, 0, 0, 0,
##                      win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
