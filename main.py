import wx

# Create the App window and Panel
app = wx.App()
window = wx.Frame(None, title = "Math Worksheet Generator", size = (1885, 1010))
window.Show()
bkg = wx.Panel(window, style = wx.WANTS_CHARS)


# Define 4 basic sizers: three horizontal sizers and a vertical one. Set the vertical sizer as base
base_vertical_sizer = wx.BoxSizer(wx.VERTICAL)
top_horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)
middle_horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)
bottom_horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)
bkg.SetSizer(base_vertical_sizer)



# Nest the three horizontal sizers within the vertical one
base_vertical_sizer.Add(top_horizontal_sizer, proportion = 1, flag = wx.TOP | wx.EXPAND, border = 10)
base_vertical_sizer.Add(middle_horizontal_sizer, proportion = 1, border = 10)
base_vertical_sizer.Add(bottom_horizontal_sizer, proportion = 1, flag = wx.BOTTOM | wx.EXPAND, border = 10)



# Construct the top horizontal box sizer, with one horizontal bar and the "run" button.
text_bar_label = wx.StaticText(bkg, label="Enter the message you wish the math problems to spell: ")
text_bar = wx.TextCtrl(bkg, pos = (0, 35), size = (210, 25), style = wx.WANTS_CHARS)
run_button = wx.Button(bkg, label = "RUN", pos = (500, 30), size = (120, 25))
top_horizontal_sizer.Add(text_bar_label, proportion = 0, flag = wx.LEFT, border = 5)
top_horizontal_sizer.Add(text_bar, proportion = 1, border = 5)
top_horizontal_sizer.Add(run_button, proportion = 0, flag = wx.RIGHT, border = 5)



# Construct the radio-button portion of the middle horizontal sizer
language_buttons_vertical_sizer = wx.BoxSizer(wx.VERTICAL)
french_button = wx.RadioButton(bkg,11, label = 'French', pos = (10,10), style = wx.RB_GROUP) 
english_button = wx.RadioButton(bkg,22, label = 'English',pos = (10,40)) 
language_buttons_vertical_sizer.Add(french_button, proportion = 1, border = 5)
language_buttons_vertical_sizer.Add(english_button, proportion = 1, border = 5)
middle_horizontal_sizer.Add(language_buttons_vertical_sizer, proportion = 1, border = 5, flag = wx.TOP | wx.LEFT)



# Construct the checkbox portion of the middle horizontal sizer. It contains two horizontal sizers nested within a vertical one, which is added to the middle horizontal sizer
operator_buttons_vertical_sizer = wx.BoxSizer(wx.VERTICAL)

operator_buttons_horizontal_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
addition_button = wx.CheckBox(bkg, label = '+ ',pos = (10,10)) 
subtraction_button = wx.CheckBox(bkg, label = '- ',pos = (10,10)) 
operator_buttons_horizontal_sizer_1.Add(addition_button, proportion = 1, border = 5, flag = wx.LEFT)
operator_buttons_horizontal_sizer_1.Add(subtraction_button, proportion = 1, border = 5, flag = wx.RIGHT)

operator_buttons_horizontal_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
multiplication_button = wx.CheckBox(bkg, label = '× ',pos = (10,10))  
division_button = wx.CheckBox(bkg, label = '÷ ',pos = (10,10))
operator_buttons_horizontal_sizer_2.Add(multiplication_button, proportion = 1, border = 5, flag = wx.LEFT)
operator_buttons_horizontal_sizer_2.Add(division_button, proportion = 1, border = 5, flag = wx.RIGHT)


operator_buttons_vertical_sizer.Add(operator_buttons_horizontal_sizer_1, proportion = 1, border = 5, flag = wx.TOP)
operator_buttons_vertical_sizer.Add(operator_buttons_horizontal_sizer_2, proportion = 1, border = 5, flag = wx.BOTTOM)
middle_horizontal_sizer.Add(operator_buttons_vertical_sizer, proportion = 1, border = 5, flag = wx.RIGHT)



# Construct the lower horizontal box
text_box = wx.TextCtrl(bkg, pos = (10, 35), size = (50, 550), style = wx.TE_MULTILINE | wx.HSCROLL | wx.WANTS_CHARS | wx.VSCROLL)
bottom_horizontal_sizer.Add(text_box, proportion = 1, border = 5)



'https://www.tutorialspoint.com/wxpython/wxpython_buttons.htm'

'https://www.tutorialspoint.com/wxpython/wx_checkbox_class.htm'




### GO! ###
app.MainLoop()


















# outputbox = wx.TextCtrl(bkg, pos = (0, 35), size = (500, 400), style = wx.TE_MULTILINE | wx.HSCROLL | wx.WANTS_CHARS)
# contents.SetWindowStyle(contents.GetWindowStyle() & ~ wx.TAB_TRAVERSAL)
# outputbox.SetWindowStyle(outputbox.GetWindowStyle() & ~ wx.TAB_TRAVERSAL)

# loadButton = wx.Button(bkg, label = "import", pos = (500, 30), size = (120, 25))

# # Create the error box
# errorbox = wx.TextCtrl(bkg, pos = (10, 35), size = (50, 750), style = wx.TE_MULTILINE | wx.HSCROLL | wx.WANTS_CHARS | wx.VSCROLL)
# # And add them to a vertical box sizer
# buttonBox = wx.BoxSizer(wx.VERTICAL)
# buttonBox.Add(loadButton, proportion = 1, flag = wx.BOTTOM, border = 5)



# #Add the two text boxes and the button box to a new, horizontal box sizer representing all of the window below the command line
# lowerhbox = wx.BoxSizer(wx.HORIZONTAL)
# lowerhbox.Add(contents, proportion = 1, flag = wx.EXPAND | wx.BOTTOM | wx.LEFT, border = 5)
# lowerhbox.Add(outputbox, proportion = 1, flag = wx.EXPAND | wx.BOTTOM | wx.RIGHT, border = 5)
# lowerhbox.Add(buttonBox, proportion = 0, flag = wx.RIGHT, border = 10)


# # Add the command bar and the lower box to a vertical sizer, and set that as the main sizer
# command = wx.TextCtrl(bkg, pos = (5, 5), size = (210, 25))
# vbox = wx.BoxSizer(wx.VERTICAL)
# vbox.Add(command, proportion = 0, flag = wx.EXPAND | wx.TOP, border = 10)
# vbox.Add(lowerhbox, proportion = 1, flag = wx.EXPAND | wx.BOTTOM, border = 10)



# def openFunct(var):
#     pass
  
# contents.SetValue("None")
# loadButton.Bind(wx.EVT_BUTTON, openFunct)




# command.SetValue("[Type commands here]")
# errorbox.SetValue("\n*****Status*****")





