from taipy.gui import Gui, navigate

show_pane=False

page="""
# ringAR

<|layout|columns = 1 1 1 1

<|card card-bg|
<|{content}|image|content=sapphireRing.png|width=275px|height=275px|on_action={lambda s: s.assign("show_pane", True)}|>
{: .p0 .m0 }
|>

<|card card-bg|
<|{content}|image|content=twistedRing.png|width=275px|height=275px|on_action={lambda s: s.assign("show_pane", True)}|>
{: .p0 .m0 }
|>

<|card card-bg|
<|{content}|image|content=pinkRing.png|width=275px|height=275px|on_action={lambda s: s.assign("show_pane", True)}|>
{: .p0 .m0 }
|>

<|card card-bg|
<|{content}|image|content=doubleRing.png|width=275px|height=275px|on_action={lambda s: s.assign("show_pane", True)}|>
{: .p0 .m0 }
|>

<|d-inline|
<|{show_pane}|pane|persistent|anchor=bottom|
information appears here
|>
|>
|>



"""
stylekit = {
  "color_primary": "#FFFFFF",
  "color_secondary": "#5DADE2",
  "color_error": "#F8C471", 
  "color_warning": "#BA4A00", 
  "color_success": "#2E4053", 
  "color_background_light": "#76448A", 
  "color_background_dark": "#E74C3C", 
  "color_paper_light": "#ABEBC6", 
  "color_paper_dark": "#D7BDE2", 
  "font_family": "#5F6A6A", 
 

}
# Gui.run(stylekit=stylekit)
Gui(page=page).run(stylekit=stylekit)

# {: .p2 .mb1 }
# #