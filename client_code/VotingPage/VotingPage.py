
from ._anvil_designer import VotingPageTemplate
from anvil import *

from ..VoteForm import VoteForm

class VotingPage(VotingPageTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.voting_data = [
      {
        "title": "Candidate A",
        "image": "https://via.placeholder.com/300x150",
        "deadline": "2025-06-01",
        "details": ["Platform Summary", "Manifesto Highlights"]
      },
      {
        "title": "Candidate B",
        "image": "https://via.placeholder.com/300x150",
        "deadline": "2025-06-15",
        "details": ["Initiatives", "Goals"]
      }
    ]
    self.load_cards()

  def load_cards(self):
    self.cards_container.clear()
    for item in self.voting_data:
      self.cards_container.add_component(VoteForm(data=item))
