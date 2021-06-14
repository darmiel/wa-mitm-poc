import json

class PresenceInfo:
  def __init__(self, raw: str):
    self.raw = raw
    self.data = json.loads(raw)
    
    self.id = self.data.get('id') or ""
    self.type = self.data.get('type') or ""
    self.unix = self.data.get('t') or -1
    self.deny = self.data.get('deny') or False
  
  def get_number(self) -> str:
    return "+{}".format(self.id[:self.id.index('@')])