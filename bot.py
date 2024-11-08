import requests
import json
import os
import urllib.parse
from colorama import *
from datetime import datetime, timedelta
import time
import pytz

wib = pytz.timezone('Asia/Jakarta')

class WigwamDrum:
    def __init__(self) -> None:
        self.session = requests.Session()
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
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
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
        query_params = urllib.parse.parse_qs(query)
        query = query_params.get('user', [None])[0]

        if query:
            user_data_json = urllib.parse.unquote(query)
            user_data = json.loads(user_data_json)
            user_id = user_data['id']
            return user_id
        else:
            raise ValueError("User data not found in query.")

    def get_user_info(self, query: str, user_id: str):
        url = 'https://drumapi.wigwam.app/api/getUserInfo'
        data = json.dumps({"authData":query, "data":{}, "devAuthData":user_id, "platfrom":"tdesktop"})
        self.headers.update({
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        response.raise_for_status()
        status = response.json()
        if status['status']:
            return status['data']
        else:
            return None
        
    def start_farm(self, query: str, user_id: str):
        url = 'https://drumapi.wigwam.app/api/gameplay/startFarm'
        data = json.dumps({"authData":query, "data":{}, "devAuthData":user_id})
        self.headers.update({
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        status = response.json()
        if status['status'] == 'error':
            return None
        else:
            return status['data']
        
    def claim_farm(self, query: str, user_id: str):
        url = 'https://drumapi.wigwam.app/api/gameplay/claimFarm'
        data = json.dumps({"authData":query, "data":{}, "devAuthData":user_id})
        self.headers.update({
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        status = response.json()
        if status['status'] == 'error':
            reason = status['data']['reason']
            if reason in ['Farm is not started', 'Mining era is not over']:
                return None
        else:
            return status['data']
        
    def claim_children(self, query: str, user_id: str):
        url = 'https://drumapi.wigwam.app/api/claimFromChildren'
        data = json.dumps({"authData":query, "data":{}, "devAuthData":user_id})
        self.headers.update({
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        status = response.json()
        if response.status_code == 200:
            if status['status']:
                return status['data']
            else:
                return None
        else:
            return None
        
    def claim_taps(self, query: str, user_id: str, taps: int, amount: int):
        url = 'https://drumapi.wigwam.app/api/claimTaps'
        data = json.dumps({"authData":query, "data":{"taps":taps, "amount":amount}, "devAuthData":user_id})
        self.headers.update({
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        status = response.json()
        if response.status_code == 200:
            if status['status'] == 'ok':
                return status['data']
            else:
                return None
        else:
            return None
        
    def start_tasks(self, query: str, user_id: str, task_id: str):
        url = 'https://drumapi.wigwam.app/api/startTask'
        data = json.dumps({"authData":query, "data":{"taskId":task_id}, "devAuthData":user_id})
        self.headers.update({
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        status = response.json()
        if response.status_code == 200:
            if status['status'] == 'ok':
                return status['data']
            else:
                return None
        else:
            return None
        
    def check_tasks(self, query: str, user_id: str, task_id: str):
        url = 'https://drumapi.wigwam.app/api/checkTask'
        data = json.dumps({"authData":query, "data":{"taskId":task_id}, "devAuthData":user_id})
        self.headers.update({
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        status = response.json()
        if response.status_code == 200:
            if status['status'] == 'ok':
                return status['data']
            else:
                return None
        else:
            return None
        
    def claim_tasks(self, query: str, user_id: str, task_id: str):
        url = 'https://drumapi.wigwam.app/api/claimTask'
        data = json.dumps({"authData":query, "data":{"taskId":task_id}, "devAuthData":user_id})
        self.headers.update({
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        status = response.json()
        if response.status_code == 200:
            if status['status'] == 'ok':
                return status['data']
            else:
                return None
        else:
            return None
    
    def process_query(self, query: str):

        user_id = self.load_data(query)

        user_info = self.get_user_info(query, user_id)
        if user_info:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {user_info['first_name']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {user_info['balance']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            time.sleep(1)

            farm_started_at = user_info.get("farmStartedAt", None)
    
            if not farm_started_at:
                start_farm = self.start_farm(query, user_id)
                if start_farm:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Next Claim at{Style.RESET_ALL} N/A {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Failed to Start {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                return

            farm_started_time_utc = datetime.fromisoformat(farm_started_at[:-1])
            farm_started_time_wib = farm_started_time_utc.replace(tzinfo=pytz.utc).astimezone(wib)
            next_claim_time_wib = farm_started_time_wib + timedelta(hours=4)
            next_claim_formatted = next_claim_time_wib.strftime('%m/%d/%y %H:%M:%S WIB')

            claim_farm = self.claim_farm(query, user_id)
            if claim_farm:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                    f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {claim_farm['claimedBalance']} Points {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                    f"{Fore.YELLOW+Style.BRIGHT} Not Time to Claim {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

            start_farm = self.start_farm(query, user_id)
            if start_farm:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                    f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Next Claim at{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {next_claim_formatted} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                    f"{Fore.YELLOW+Style.BRIGHT} Is Already Started {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Next Claim at{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {next_claim_formatted} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

            claim_children = self.claim_children(query, user_id)
            if claim_children:
                rewards = float(claim_children['claimedBalance'])
                if rewards > 0:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                        f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {rewards} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}Points ]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} No Available Rewards to Claim {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT} You Don't Have Any Refferal {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

            tap_interval = user_info['tapIntervalMinutes']
            available_taps = user_info['availableTaps']

            if available_taps > 0:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Tap Tap{Style.RESET_ALL}"
                    f"{Fore.GREEN + Style.BRIGHT} Is Started {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}] [ Wait{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} {available_taps} Seconds... {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )

                total_amount = 0

                while available_taps > 0:
                    taps = min(tap_interval, available_taps)
                    amount = available_taps

                    tap_tap = self.claim_taps(query, user_id, taps, amount)

                    if tap_tap:
                        total_amount += amount
                        available_taps -= taps
                    else:
                        break

                if available_taps == 0:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Tap Tap{Style.RESET_ALL}"
                        f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {total_amount} Points {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Tap Tap{Style.RESET_ALL}"
                    f"{Fore.YELLOW+Style.BRIGHT} Is Already Claimed {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

            tasks = user_info['tasks']
            if tasks:
                for task_id, task_info in tasks.items():
                    status_task = task_info['state']

                    if task_id == "watch_adsgram":
                        continue

                    if status_task == "NONE":
                        start = self.start_tasks(query, user_id, task_id)
                        if start and start['state'] == "ReadyToCheck":
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {start['title']} {Style.RESET_ALL}"
                                f"{Fore.GREEN + Style.BRIGHT}Is Started{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                            )

                            check = self.check_tasks(query, user_id, task_id)
                            if check and check['state'] == "ReadyToClaim":
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {check['title']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN + Style.BRIGHT}Is Checked{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                            
                                claim = self.claim_tasks(query, user_id, task_id)
                                if claim and claim['task']['state'] == "Claimed":
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {claim['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {claim['task']['reward']} {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {claim['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.YELLOW + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {check['title']} {Style.RESET_ALL}"
                                    f"{Fore.YELLOW + Style.BRIGHT}Isn't Checked{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {start['title']} {Style.RESET_ALL}"
                                f"{Fore.YELLOW + Style.BRIGHT}Isn't Started{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                            )

                    elif status_task == "ReadyToCheck":
                        check = self.check_tasks(query, user_id, task_id)
                        if check and check['state'] == "ReadyToClaim":
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {check['title']} {Style.RESET_ALL}"
                                f"{Fore.GREEN + Style.BRIGHT}Is Checked{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                            
                            claim = self.claim_tasks(query, user_id, task_id)
                            if claim and claim['task']['state'] == "Claimed":
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {claim['task']['title']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {claim['task']['reward']} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {claim['task']['title']} {Style.RESET_ALL}"
                                    f"{Fore.YELLOW + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {check['title']} {Style.RESET_ALL}"
                                f"{Fore.YELLOW + Style.BRIGHT}Isn't Checked{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                            )

                    elif status_task == "ReadyToClaim":
                        claim = self.claim_tasks(query, user_id, task_id)
                        if claim and claim['task']['state'] == "Claimed":
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {claim['task']['title']} {Style.RESET_ALL}"
                                f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {claim['task']['reward']} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {claim['task']['title']} {Style.RESET_ALL}"
                                f"{Fore.YELLOW + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                            )

            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
        else:
            self.log(
                f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} ID {user_id} {Style.RESET_ALL}"
                f"{Fore.RED + Style.BRIGHT}Data Is None{Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
            )

    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

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
                        self.process_query(query)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        time.sleep(3)

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Wigwam Drum - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    wigwam = WigwamDrum()
    wigwam.main()