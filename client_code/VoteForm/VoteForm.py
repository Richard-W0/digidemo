
from ._anvil_designer import VoteFormTemplate
from anvil import *

class VoteForm(VoteFormTemplate):
  def __init__(self, data={}, **properties):
    self.init_components(**properties)
    self.label_title.text = data.get('title', '')
    self.image.source = data.get('image', '')
    self.progress_bar.value = self.days_remaining(data.get('deadline'))
    self.details_panel.visible = False
    for detail in data.get('details', []):
      self.details_panel.add_component(Label(text=detail))

  def toggle_details(self, **event_args):
    self.details_panel.visible = not self.details_panel.visible
    self.button_toggle.text = "Hide Options" if self.details_panel.visible else "Show Options"

  def days_remaining(self, deadline_str):
    from datetime import date, datetime
    if not deadline_str:
      return 0
    deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
    return max(0, (deadline - date.today()).days)
