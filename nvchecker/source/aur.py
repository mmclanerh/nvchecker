# MIT licensed
# Copyright (c) 2013-2017 lilydjwg <lilydjwg@gmail.com>, et al.

import logging
from . import session

AUR_URL = 'https://aur.archlinux.org/rpc/?v=5&type=info&arg[]='

logger = logging.getLogger(__name__)

async def get_version(name, conf):
  aurname = conf.get('aur') or name
  strip_release = conf.getboolean('strip-release', False)
  async with session.get(AUR_URL, params={"v": 5, "type": "info", "arg[]": aurname}) as res:
    data = await res.json()

  if not data['results']:
    logger.error('AUR upstream not found for %s', name)
    return name, None

  version = data['results'][0]['Version']
  if strip_release and '-' in version:
    version = version.rsplit('-', 1)[0]
  return name, version
