import os
import ssl
import json
import time
import asyncio
import random
import base64
import aiohttp
import certifi
from datetime import datetime
from pystyle import Colorate, Colors

ssl._create_default_https_context = ssl._create_unverified_context

MAX_RETRIES = 3
SMART_RETRY = 2
REQUEST_TIMEOUT = 12


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"
]

def get_terminal_size():
    try:
        return os.get_terminal_size().columns
    except:
        return 80

size = get_terminal_size()

THEME_COLORS = [
    Colors.yellow_to_green,
    Colors.yellow_to_red,
    Colors.red_to_yellow,
    Colors.red_to_green,
    Colors.red_to_blue,
    Colors.red_to_purple,
    Colors.red_to_white,
    Colors.green_to_yellow,
    Colors.green_to_red,
    Colors.green_to_blue,
    Colors.green_to_cyan,
    Colors.green_to_white,
    Colors.blue_to_red,
    Colors.blue_to_green,
    Colors.blue_to_cyan,
    Colors.blue_to_purple,
    Colors.blue_to_white,
    Colors.cyan_to_green,
    Colors.cyan_to_blue,
    Colors.purple_to_red,
    Colors.purple_to_blue,
    Colors.white_to_red,
    Colors.white_to_green,
    Colors.white_to_blue,
    Colors.rainbow
]

THEME_COLOR = random.choice(THEME_COLORS)

def banner():
    current_time = datetime.now().strftime("%H:%M:%S")
    text = r"""
     ███╗   ██╗ ██████╗ ██╗   ██╗
████╗  ██║██╔════╝ ██║   ██║
██╔██╗ ██║██║  ███╗██║   ██║
██║╚██╗██║██║   ██║██║   ██║
██║ ╚████║╚██████╔╝╚██████╔╝
╚═╝  ╚═══╝ ╚═════╝  ╚═════╝
          
 TOOL SPAMER DISCORD
 CODER: CHATGPT
 DIS : nombending
    """
    print(Colorate.Horizontal(THEME_COLOR, text))
    print(Colorate.Horizontal(THEME_COLOR, f"YamateKudasai"))
    print(Colorate.Horizontal(THEME_COLOR, f"Time: {current_time}"))
    print()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

class A:
    def __init__(self, files):
        self.messages = []
        for file_path in files:
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if content:
                        self.messages.append(content)

    def get_random(self):
        return random.choice(self.messages) if self.messages else "Hoang Minh Khang Ne Con"

class B:
    def __init__(self, tokens, channel, message_loader, delays, token_indices):
        self.tokens = tokens
        self.channel = channel
        self.message_loader = message_loader
        self.delays = delays
        self.token_indices = token_indices
        self.running = True
        self.channel_name = None
        self.ssl_context = self._ssl()

    def _ssl(self):
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        return ssl_context

    async def check_token(self, session, token):
        headers = {
            "Authorization": token.strip(),
            "User-Agent": random.choice(USER_AGENTS),
        }
        try:
            async with session.get(
                "https://discord.com/api/v10/users/@me",
                headers=headers,
                ssl=self.ssl_context,
                timeout=aiohttp.ClientTimeout(total=REQUEST_TIMEOUT)
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return 'id' in data and 'username' in data
                elif resp.status in [401, 403]:
                    return resp.status == 403
                return False
        except:
            return False

    async def _loc(self):
        print(Colorate.Horizontal(THEME_COLOR, f"Dang kiem tra {len(self.tokens)} token..."))
        
        connector = aiohttp.TCPConnector(ssl=self.ssl_context)
        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = [self.check_token(session, token) for token in self.tokens]
            results = await asyncio.gather(*tasks)
        
        valid = [t for t, r in zip(self.tokens, results) if r]
        print(Colorate.Horizontal(THEME_COLOR, f"Token hop le: {len(valid)}/{len(self.tokens)}"))
        return valid

    async def _get_name(self, session, channel_id, token):
        if self.channel_name:
            return self.channel_name
        
        headers = {"Authorization": token, "User-Agent": random.choice(USER_AGENTS)}
        try:
            async with session.get(
                f"https://discord.com/api/v10/channels/{channel_id}",
                headers=headers,
                ssl=self.ssl_context,
                timeout=aiohttp.ClientTimeout(total=5)
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    name = data.get('name', 'Unknown')
                    self.channel_name = name
                    return name
        except:
            pass
        return 'Unknown'

    def _hd(self, token):
        build_number = random.randint(240000, 250000)
        dev = {
            "os": "Windows",
            "browser": "Chrome",
            "device": "",
            "system_locale": random.choice(["en-US", "en-GB"]),
            "browser_user_agent": random.choice(USER_AGENTS),
            "browser_version": "120.0.0.0",
            "os_version": "10",
            "referrer": "https://discord.com/",
            "referring_domain": "discord.com",
            "release_channel": "stable",
            "client_build_number": build_number,
            "client_event_source": None
        }

        return {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": dev['browser_user_agent'],
            "X-Super-Properties": base64.b64encode(json.dumps(dev, separators=(',', ':')).encode()).decode(),
            "Origin": "https://discord.com",
            "Referer": "https://discord.com/channels/@me"
        }

    async def _send(self, session, token, channel, message, token_idx):
        nonce = str(int(time.time() * 1000) + random.randint(1000, 9999))
        data = json.dumps({
            "content": message,
            "tts": False,
            "nonce": nonce,
            "flags": 0
        })

        headers = self._hd(token)
        url = f"https://discord.com/api/v10/channels/{channel}/messages"

        for attempt in range(SMART_RETRY):
            try:
                async with session.post(
                    url,
                    data=data,
                    headers=headers,
                    ssl=self.ssl_context,
                    timeout=aiohttp.ClientTimeout(total=REQUEST_TIMEOUT)
                ) as resp:
                    if resp.status == 429:
                        retry_after = (await resp.json()).get('retry_after', 1.5)
                        await asyncio.sleep(retry_after)
                        continue

                    if resp.status == 401:
                        return False, None

                    if resp.status == 403:
                        return False, None

                    channel_name = await self._get_name(session, channel, token)
                    
                    if 200 <= resp.status < 300:
                        print(f"Success > Token [{token_idx}/{len(self.tokens)}] > {channel_name}")
                        return True, None
                    else:
                        print(f"403 > Token [{token_idx}/{len(self.tokens)}]")
                        return False, None

            except asyncio.TimeoutError:
                await asyncio.sleep(random.uniform(0.8, 1.2))
            except Exception:
                await asyncio.sleep(random.uniform(0.8, 1.2))

        return False, None

    async def _sp(self, token, token_idx):
        connector = aiohttp.TCPConnector(ssl=self.ssl_context)
        async with aiohttp.ClientSession(connector=connector) as session:
            while self.running:
                try:
                    for _ in range(2):
                        message = self.message_loader.get_random()
                        await self._send(session, token, self.channel, message, token_idx)
                        await asyncio.sleep(0.2) 
                    
                    await asyncio.sleep(self.delays[token])

                except Exception:
                    await asyncio.sleep(1)

    async def _name_k(self, token):
        print(Colorate.Horizontal(THEME_COLOR, "Da Spam Vao Kenh"))
        
        connector = aiohttp.TCPConnector(ssl=self.ssl_context)
        async with aiohttp.ClientSession(connector=connector) as session:
            channel_name = await self._get_name(session, self.channel, token)
            print(Colorate.Horizontal(THEME_COLOR, f"Id: {self.channel} - Ten: {channel_name}"))
        print()

    async def run(self):
        tasks = [self._sp(token, idx) for idx, token in enumerate(self.tokens, 1)]
        try:
            await asyncio.gather(*tasks)
        except KeyboardInterrupt:
            self.running = False

async def main():
    cls()
    banner()

    token_file = input(Colorate.Horizontal(THEME_COLOR, "Nhap file chua token: ")).strip()
    if not token_file:
        print(Colorate.Horizontal(THEME_COLOR, "Nhap cai lon gi vay ?"))
        return

    try:
        with open(token_file, 'r', encoding='utf-8') as f:
            all_tokens = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(Colorate.Horizontal(THEME_COLOR, f"Khong tim thay file '{token_file}'"))
        return

    if not all_tokens:
        print(Colorate.Horizontal(THEME_COLOR, f"Khong co token nao trong file {token_file}"))
        return

    spammer = B(all_tokens, None, None, {}, all_tokens)
    tokens = await spammer._loc()

    if not tokens:
        print(Colorate.Horizontal(THEME_COLOR, "Khong co token hop le nao"))
        return

    channel = input(Colorate.Horizontal(THEME_COLOR, "Nhap id kenh chat: ")).strip()
    if not channel:
        print(Colorate.Horizontal(THEME_COLOR, "Deo nhap id an lon a ?"))
        return

    files = []
    print(Colorate.Horizontal(THEME_COLOR, "Nhap file Text:"))
    while True:
        file_path = input(Colorate.Horizontal(THEME_COLOR, "Nhap file hoac (done): ")).strip()
        if file_path.lower() == 'done':
            break
        if file_path and os.path.exists(file_path):
            files.append(file_path)

    if not files:
        print(Colorate.Horizontal(THEME_COLOR, "Khong tim thay file chua noi dung"))
        return

    message_loader = A(files)

    print(Colorate.Horizontal(THEME_COLOR, "Chon che do delay:"))
    print(Colorate.Horizontal(THEME_COLOR, "Mode 1 > Set delay"))
    print(Colorate.Horizontal(THEME_COLOR, "Mode 2 > Random delay"))
    
    mode = input(Colorate.Horizontal(THEME_COLOR, "Mode (1-2): ")).strip()
    
    delays = {}
    if mode == '1':
        for idx, token in enumerate(tokens, 1):
            while True:
                try:
                    delay_input = input(Colorate.Horizontal(THEME_COLOR, f"Token [{idx}/{len(tokens)}]: "))
                    delay = float(delay_input)
                    delays[token] = delay
                    break
                except ValueError:
                    print(Colorate.Horizontal(THEME_COLOR, "Vui long chon mode hop le"))
    elif mode == '2':
        delays = {token: random.uniform(1, 8) for token in tokens}
    else:
        delays = {token: random.uniform(1, 8) for token in tokens}

    print(Colorate.Horizontal(THEME_COLOR, 'Dang khoi dong'))
    time.sleep(2)
    cls()
    banner()

    spammer = B(tokens, channel, message_loader, delays, tokens)
    await spammer._name_k(tokens[0])

    try:
        await spammer.run()
    except KeyboardInterrupt:
        print(Colorate.Horizontal(THEME_COLOR, "Dang dung ..."))
        spammer.running = False

if __name__ == "__main__":
    asyncio.run(main())