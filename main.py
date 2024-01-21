from taipy.gui import Gui, navigate

show_pane=False

page="""
# **ringAR**{: .color-success}

<|layout|columns = 1 1 1 1

<|card card-bg|
<|{content}|image|content=sapphireRing.png|width=275px|height=275px|on_action={lambda s: s.assign("show_pane", True)}|>
<|d-inline|
<|Try This|button|class_name=success|>
<|Try This|button|class_name=success|>
{: .ml3 .mr3}
|>
{: .p0 .m-auto }
|>


<|card card-bg|
<|{content}|image|content=twistedRing.png|width=275px|height=275px|on_action={lambda s: s.assign("show_pane", True)}|>
<|d-inline|
<|Try This|button|class_name=success|>
<|Try This|button|class_name=success|>
{: .ml3 .mr3}
|>
{: .p0 .m-auto }
|>


<|card card-bg|
<|{content}|image|content=pinkRing.png|width=275px|height=275px|on_action={lambda s: s.assign("show_pane", True)}|>
<|d-inline|
<|Try This|button|class_name=success|>
<|Try This|button|class_name=success|>
{: .ml3 .mr3}
|>
{: .p0 .m-auto }
|>


<|card card-bg|
<|{content}|image|content=doubleRing.png|width=275px|height=275px|on_action={lambda s: s.assign("show_pane", True)}|>
<|d-inline|
<|Try This|button|class_name=success|>
<|Try This|button|class_name=success|>
{: .ml3 .mr3}
|>
{: .p0 .m-auto }
|>


<|d-inline|
<|{show_pane}|pane|persistent|anchor=bottom|
**INFO HERE**{: .color-success}
|>
|>
|>



"""
stylekit = {
  "color_primary": "#FFFFFF",
  "color_secondary": "#5DADE2",
  "color_error": "##1C2833", 
  "color_warning": "#BA4A00", 
  "color_success": "#2E4053", 
  "color_background_light": "#D8EFF9", 
  "color_background_dark": "#D8EFF9", 
  "color_paper_light": "#FDFEFE", 
  "color_paper_dark": "#F6FEFF" 
}
Gui(page=page).run(stylekit=stylekit)
