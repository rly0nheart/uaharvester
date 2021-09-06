#!/usr/bin/env python3

from assets.__main__ import *
from assets.colors import red,green,white,reset
			
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description=f"{white}UA{green}Harvestr{white}: {red}A tool that harvests information on a User-Agent. Developed by {white}rly0nheart{red}. https://github.com/{white}rlyonheart{reset}")
	parser.add_argument("ua", metavar="TARGET USER-AGENT", help="target user-agent")
	parser.add_argument("--is-crawler", dest="crawler", help="check if target is a crawler", action="store_true")
	args = parser.parse_args()
	while True:
		try:
			UAHarvestr(args).on_connection(args)
			break
			
		except KeyboardInterrupt:
			print(f"{white}An error occured: {red}{e}{reset}")
			print(f"{white}Retrying...{reset}")
