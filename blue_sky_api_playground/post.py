import os
import sys

from argparse import ArgumentParser
from atproto import Client
from dotenv import load_dotenv

load_dotenv()


def run(message):
  if message == '':
    return False
  client = create_bluesky_client()
  result = client.send_post(text=message)

  return result


def create_bluesky_client():
  client = Client()
  username = os.getenv('BLUESKY_IDENTIFIER')
  password = os.getenv('BLUESKY_PASSWORD')
  client.login(username, password)

  return client


def get_options():
  argparser = ArgumentParser()
  argparser.add_argument('-t', '--text', type=str,
                         default='',
                         help='Post Message')

  return argparser.parse_args()


if __name__ == '__main__':
  args = get_options()
  print(f'args: {args}')

  message = str(args.text)
  print(f'message: [{message}]')
  
  if message is None or message == '':
    print('please specify post message. --text <Post Message>')
    sys.exit()

  print('start send message to bluesky')
  result = run(message=message)
  print(f'result: {result}')
