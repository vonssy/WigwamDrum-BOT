from aiohttp import (
    ClientResponseError,
    ClientSession,
    ClientTimeout
)
from colorama import *
from urllib.parse import parse_qs, unquote
from datetime import datetime, timedelta, timezone
from fake_useragent import FakeUserAgent
import asyncio, os, json, pytz

wib = pytz.timezone('Asia/Jakarta')

class WigwamDrum:
    def __init__(self) -> None:
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Host': 'drumapi.wigwam.app',
            'Origin': 'https://drum.wigwam.app',
            'Pragma': 'no-cache',
            'Referer': 'https://drum.wigwam.app/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': FakeUserAgent().random
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Wigwam Drum - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def load_data(self, query: str):
        query_params = parse_qs(query)
        query = query_params.get('user', [None])[0]

        if query:
            user_data_json = unquote(query)
            user_data = json.loads(user_data_json)
            user_id = user_data['id']
            return user_id
        else:
            raise ValueError("User data not found in query.")
        
    async def user_data(self, query: str, user_id: int, retries=5):
        url = 'https://drumapi.wigwam.app/api/getUserInfo'
        data = json.dumps({"authData":query, "data":{}, "devAuthData":user_id, "platfrom":"android"})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        result = await response.json()
                        return result['data']
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def claim_checkin(self, query: str, user_id: int, retries=5):
        url = 'https://drumapi.wigwam.app/api/gameplay/claimDailyBonus'
        data = json.dumps({"authData":query, "data":{}, "devAuthData":user_id})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        if response.status == 500:
                              return None
                        response.raise_for_status()
                        result = await response.json()
                        return result['data']
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def tribe_data(self, query: str, user_id: int, retries=5):
        url = 'https://drumapi.wigwam.app/api/getChildren'
        data = json.dumps({"authData":query, "data":{}, "devAuthData":user_id})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        result = await response.json()
                        return result['data']
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def claim_tribe(self, query: str, user_id: int, retries=5):
        url = 'https://drumapi.wigwam.app/api/claimFromChildren'
        data = json.dumps({"authData":query, "data":{}, "devAuthData":user_id})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        result = await response.json()
                        return result['data']
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def start_farm(self, query: str, user_id: int, retries=5):
        url = 'https://drumapi.wigwam.app/api/gameplay/startFarm'
        data = json.dumps({"authData":query, "data":{}, "devAuthData":user_id})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        result = await response.json()
                        return result['data']
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def claim_farm(self, query: str, user_id: int, retries=5):
        url = 'https://drumapi.wigwam.app/api/gameplay/claimFarm'
        data = json.dumps({"authData":query, "data":{}, "devAuthData":user_id})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        result = await response.json()
                        return result['data']
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def claim_taps(self, query: str, user_id: int, taps: int, amount: int, retries=5):
        url = 'https://drumapi.wigwam.app/api/claimTaps'
        data = json.dumps({"authData":query, "data":{"taps":taps, "amount":amount}, "devAuthData":user_id})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        result = await response.json()
                        return result['data']
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def upgrade_skills(self, query: str, user_id: int, skill_id: str, retries=5):
        url = 'https://drumapi.wigwam.app/api/gameplay/upgradeSkill'
        data = json.dumps({"authData":query, "data":{"skillId":skill_id}, "devAuthData":user_id})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def upgrade_game_levels(self, query: str, user_id: int, retries=5):
        url = 'https://drumapi.wigwam.app/api/gameplay/upgradeGameLevel'
        data = json.dumps({"authData":query, "data":{}, "devAuthData":user_id})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        if response.status == 500:
                            return
                        
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def start_tasks(self, query: str, user_id: int, task_id: str, retries=5):
        url = 'https://drumapi.wigwam.app/api/startTask'
        data = json.dumps({"authData":query, "data":{"taskId":task_id}, "devAuthData":user_id})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        result = await response.json()
                        return result['data']
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def check_tasks(self, query: str, user_id: int, task_id: str, retries=5):
        url = 'https://drumapi.wigwam.app/api/checkTask'
        data = json.dumps({"authData":query, "data":{"taskId":task_id}, "devAuthData":user_id})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        result = await response.json()
                        return result['data']
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def claim_tasks(self, query: str, user_id: int, task_id: str, retries=5):
        url = 'https://drumapi.wigwam.app/api/claimTask'
        data = json.dumps({"authData":query, "data":{"taskId":task_id}, "devAuthData":user_id})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        result = await response.json()
                        return result['data']
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    def question(self):
        while True:
            upgrade_level = input("Upgrade Skill and Display Game Level? [y/n] -> ").strip().lower()
            if upgrade_level in ["y", "n"]:
                upgrade_level = upgrade_level == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to upgrade or 'n' to skip.{Style.RESET_ALL}")

        return upgrade_level
        
    async def process_query(self, query: str, upgrade_level: bool):
        user_id = self.load_data(query)
        user = await self.user_data(query, user_id)
        if not user:
            self.log(
                f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED + Style.BRIGHT} Query Id Isn't Valid {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return

        if user:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {user['first_name']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {user['balance']} DRUM {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            await asyncio.sleep(1)

            check_in = await self.claim_checkin(query, user_id)
            if check_in:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                    f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Balane{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {check_in['balance']} DRUM {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                    f"{Fore.YELLOW+Style.BRIGHT} Is Already Claimed {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            await asyncio.sleep(1)

            tribe = await self.tribe_data(query, user_id)
            if tribe:
                rewards = float(tribe['totalRewardsToClaim'])
                if rewards > 0:
                    claim = await self.claim_tribe(query, user_id)
                    if claim:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Tribe{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {rewards} DRUM {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Tribe{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Tribe{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} No Available Reward to Claim {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Tribe{Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            await asyncio.sleep(1)

            is_started = user.get('farmStartedAt', None)
            if is_started is None:
                start = await self.start_farm(query, user_id)
                if start:
                    start_time = datetime.strptime(start['farmStartedAt'], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
                    end_time_utc = start_time + timedelta(hours=4)
                    end_time_wib = end_time_utc.astimezone(wib).strftime('%x %X %Z')

                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {end_time_wib} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                await asyncio.sleep(1)

            else:
                now = datetime.utcnow().replace(tzinfo=timezone.utc)
                start_time = datetime.strptime(is_started, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
                end_time_utc = start_time + timedelta(hours=4)
                end_time_wib = end_time_utc.astimezone(wib).strftime('%x %X %Z')

                if now >= end_time_utc:
                    claim = await self.claim_farm(query, user_id)
                    if claim:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {claim['claimedBalance']} DRUM {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                        await asyncio.sleep(1)

                        start = await self.start_farm(query, user_id)
                        if start:
                            start_time = datetime.strptime(start['farmStartedAt'], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
                            end_time_utc = start_time + timedelta(hours=4)
                            end_time_wib = end_time_utc.astimezone(wib).strftime('%x %X %Z')

                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {end_time_wib} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    await asyncio.sleep(1)

                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Not Time to CLaim {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {end_time_wib} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                await asyncio.sleep(1)

            amount = user['availableTaps']
            if amount > 0:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Tap Tap{Style.RESET_ALL}"
                    f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
                await asyncio.sleep(1)

                taps = 1
                rewards = 0
                while amount >= taps:
                    tap_tap = await self.claim_taps(query, user_id, taps, amount)
                    if tap_tap:
                        amount -= taps
                        rewards += amount
                        print(
                            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                            f"{Fore.YELLOW + Style.BRIGHT} {amount} {Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT}Seconds to Claim Reward{Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}   ",
                            end="\r",
                            flush=True
                        )
                    else:
                        break

                    await asyncio.sleep(1.5)

                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Tap Tap{Style.RESET_ALL}"
                    f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {rewards} DRUM {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}          "
                )

            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Tap Tap{Style.RESET_ALL}"
                    f"{Fore.YELLOW+Style.BRIGHT} No Available Now {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            await asyncio.sleep(1)

            if upgrade_level:
                user = await self.user_data(query, user_id)
                if not user:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Skill Display{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Failed to Retrieve User Balance {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                    return
                
                skills = user["displaySkills"]
                if skills:
                    balance = float(user["balance"])
                    for skill_id, details in skills.items():
                        cost = details["nextLevelUpgradeCost"]
                        level = details["level"] + 1

                        if balance >= cost:
                            upgrade_skill = await self.upgrade_skills(query, user_id, skill_id)
                            if upgrade_skill and upgrade_skill["message"] == "Skill upgraded":
                                balance -= cost
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Skill Display{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {details['name']} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} Level {level} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Status{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Is Upgraded {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Cost{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {cost} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Skill Display{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {details['name']} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} Level {level} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Status{Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT} Isn't Upgarded {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )

                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Skill Display{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {details['name']} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} Level {level} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Status{Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT} Balance Not Enough {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                            
                    display_game = user["displayGameLevel"]
                    list_display = user['displayGameLevels']
                    if display_game:
                        upgrade_game = await self.upgrade_game_levels(query, user_id)
                        if upgrade_game and upgrade_game['message'] == 'Game level upgraded':
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Game Display{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {upgrade_game['toUpdate']['displayGameLevel']['name']} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} Level {upgrade_game['toUpdate']['displayGameLevel']['level']} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Status{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Upgraded {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            current_index = next((index for (index, d) in enumerate(list_display) if d["level"] == display_game["level"]), None)
                            if current_index is not None and current_index + 1 < len(list_display):
                                next_level = list_display[current_index + 1]
                                next_name = next_level["name"]
                                next_level_num = next_level["level"]
                            else:
                                next_name = display_game["name"]
                                next_level_num = display_game["level"]

                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Game Display{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {next_name} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} Level {next_level_num} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Status{Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT} Not Eligible {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )

                    else:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Game Display{Style.RESET_ALL}"
                            f"{Fore.RED + Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )

                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Skill Display{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Skill Display{Style.RESET_ALL}"
                    f"{Fore.YELLOW + Style.BRIGHT} Upgrade Skipped {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
            await asyncio.sleep(1)

            tasks = user['tasks']
            if tasks:
                completed = False
                for task_id, task_info in tasks.items():
                    status_task = task_info['state']
                    title = task_info['title']
                    reward = task_info['reward']

                    if task_id == "watch_adsgram":
                        continue

                    if status_task == "NONE":
                        start = await self.start_tasks(query, user_id, task_id)
                        if start and start['state'] == "ReadyToCheck":
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                f"{Fore.GREEN + Style.BRIGHT}Is Started{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                            await asyncio.sleep(1)

                            check = await self.check_tasks(query, user_id, task_id)
                            if check and check['state'] == "ReadyToClaim":
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                    f"{Fore.GREEN + Style.BRIGHT}Is Checked{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                                await asyncio.sleep(1)
                            
                                claim = await self.claim_tasks(query, user_id, task_id)
                                if claim and claim['task']['state'] == "Claimed":
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {reward} {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                        f"{Fore.RED + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )

                            else:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                    f"{Fore.RED + Style.BRIGHT}Isn't Checked{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                                
                        else:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                f"{Fore.RED + Style.BRIGHT}Isn't Started{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                        await asyncio.sleep(1)

                    elif status_task == "ReadyToCheck":
                        check = await self.check_tasks(query, user_id, task_id)
                        if check and check['state'] == "ReadyToClaim":
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                f"{Fore.GREEN + Style.BRIGHT}Is Checked{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                            await asyncio.sleep(1)
                            
                            claim = await self.claim_tasks(query, user_id, task_id)
                            if claim and claim['task']['state'] == "Claimed":
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                    f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {reward} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                    f"{Fore.RED + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                )

                        else:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                f"{Fore.RED + Style.BRIGHT}Isn't Checked{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                        await asyncio.sleep(1)

                    elif status_task == "ReadyToClaim":
                        claim = await self.claim_tasks(query, user_id, task_id)
                        if claim and claim['task']['state'] == "Claimed":
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {reward} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                f"{Fore.RED + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                        await asyncio.sleep(1)

                    else:
                        completed = True

                if completed:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                        f"{Fore.GREEN + Style.BRIGHT} Is Completed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )

            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
        
    async def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            upgrade_level = self.question()

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)

                for query in queries:
                    query = query.strip()
                    if query:
                        await self.process_query(query, upgrade_level)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        await asyncio.sleep(3)
                        

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    await asyncio.sleep(1)
                    seconds -= 1

        except FileNotFoundError:
            self.log(f"{Fore.RED}File 'query.txt' tidak ditemukan.{Style.RESET_ALL}")
            return
        except Exception as e:
            self.log(f"{Fore.RED+Style.BRIGHT}Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        bot = WigwamDrum()
        asyncio.run(bot.main())
    except KeyboardInterrupt:
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
            f"{Fore.RED + Style.BRIGHT}[ EXIT ] Wigwam Drum - BOT{Style.RESET_ALL}",                                       
        )