from mitmproxy import http, ctx, websocket
from parser import handle_presence

class WA:
    def websocket_message(self, flow: websocket.WebSocketFlow):
        msg = flow.messages[-1]  # get latest message
        if msg.from_client:
          return
        if isinstance(msg.content, str):
          smsg = str(msg.content)
          if 'Presence' in smsg:
            handle_presence(smsg)