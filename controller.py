import wx
from wx.lib.pubsub import Publisher as pub

from model import Model
from view import View
from view import ChangerWidget

class Controller:
    def __init__(self, app):
        self.model = Model()

        #set up the first frame which displays the current Model value
        self.view1 = View(None)
        self.view1.SetMoney(self.model.myMoney)

        #set up the second frame which allows the user to modify the Model's value
        self.view2 = ChangerWidget(self.view1)
        self.view2.add.Bind(wx.EVT_BUTTON, self.AddMoney)
        self.view2.remove.Bind(wx.EVT_BUTTON, self.RemoveMoney)
        #subscribe to all "MONEY CHANGED" messages from the Model
        #to subscribe to ALL messages (topics), omit the second argument below
        pub.subscribe(self.MoneyChanged, "MONEY CHANGED")

        self.view1.Show()
        self.view2.Show()

    def AddMoney(self, evt):
        self.model.addMoney(10)

    def RemoveMoney(self, evt):
        self.model.removeMoney(10)

    def MoneyChanged(self, message):
        """
        This method is the handler for "MONEY CHANGED" messages,
        which pubsub will call as messages are sent from the model.

        We already know the topic is "MONEY CHANGED", but if we
        didn't, message.topic would tell us.
        """
        self.view1.SetMoney(message.data)
