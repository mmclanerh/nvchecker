# MIT licensed
# Copyright (c) 2013-2017 lilydjwg <lilydjwg@gmail.com>, et al.

async def get_version(name, conf):
  return name, conf.get('manual')
