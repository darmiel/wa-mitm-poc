import json
from mitmproxy import http, ctx, websocket

def format_number(id: str) -> str:
  return "+{}".format(id[:id.index("@")])

def handle_presence(content: str) -> None:
  # get message between '[' and ']'
  data = content[content.index("[") + 1:content.index("]")].strip()
  data = data[data.index("{"):].strip()
  ctx.log.info("unmarshal: " + data)

  # warn: "Presence",{"id":"4915124224192@c.us","type":"unavailable","t":1623667301,"deny":false}
  resp = json.loads(data)

  # data
  num = format_number(resp['id'])
  typ = resp.get('type') or ""
  dny = resp.get('deny') or False
  #

class WA:
    def websocket_message(self, flow: websocket.WebSocketFlow):
        msg = flow.messages[-1]  # get latest message
        if msg.from_client:
          return
        if isinstance(msg.content, str):
          smsg = str(msg.content)
          if 'Presence' in smsg:
            handle_presence(smsg)

addons = [
    WA()
]
