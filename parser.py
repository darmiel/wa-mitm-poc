import json
import db

from mitmproxy import ctx
from obj import PresenceInfo

def handle_presence(content: str) -> None:
  # get message between '[' and ']'
  data = content[content.index("[") + 1:content.index("]")].strip()
  data = data[data.index("{"):].strip()

  # warn: "Presence",{"id":"4915124224192@c.us","type":"unavailable","t":1623667301,"deny":false}
  info = PresenceInfo(data)
  ctx.log.warn(info.get_number() + " -> " + info.type)
  db.add_presence(info)