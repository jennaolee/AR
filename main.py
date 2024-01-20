# from taipy.gui import Gui

# text = "Original text"

# page = """
# # Getting started with Taipy GUI

# My text: <|{text}|>

# <|{text}|input|>

# <|layout|columns=1 1 1|
# Button in first column <|Press|button|> <|{show}|pane|anchor=left|>

# Second column

# Third column
# |>

# """

# Gui(page).run()


from taipy.gui import Gui

show_pane=True

page="""
# ringAR

<|layout|columns = 1 1 1 1

<|card card-bg|
Inside the card
<|{content}|image|content=ring.jpg|>
{: .p1 .mb1 }
|>

<|card card-bg|
Inside the card
<|{content}|image|content=ring.jpg|>
{: .p1 .mb1 }
|>

<|card card-bg|
Inside the card
<|{content}|image|content=ring.jpg|>
{: .p1 .mb1 }
|>

<|card card-bg|
Inside the card
<|{content}|image|content=ring.jpg|>
{: .p1 .mb1 }
|>

<|d-flex|
<|{show_pane}|pane|persistent|width=100px|
Pane content
|>
This button can be pressed to open the persistent pane:
<|Open|button|on_action={lambda s: s.assign("show_pane", True)}|>
|>

"""

Gui(page=page).run()