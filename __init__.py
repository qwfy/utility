from datetime import datetime
from datetime import timezone

import tabulate

import logging
logger = logging.getLogger(__name__)


def unzip(ts):
  xs, ys = [], []
  for x, y in ts:
    xs.append(x)
    ys.append(y)
  return xs, ys


def unzip3(ts):
  xs, ys, zs = [], [], []
  for x, y, z in ts:
    xs.append(x)
    ys.append(y)
    zs.append(z)
  return xs, ys, zs


def unzip4(ts):
  xs, ys, zs, us = [], [], [], []
  for x, y, z, u in ts:
    xs.append(x)
    ys.append(y)
    zs.append(z)
    us.append(u)
  return xs, ys, zs, us


def unzip5(ts):
  xs, ys, zs, us, vs = [], [], [], [], []
  for x, y, z, u, v in ts:
    xs.append(x)
    ys.append(y)
    zs.append(z)
    us.append(u)
    vs.append(v)
  return xs, ys, zs, us, vs


def tablize_alist(alist, headers=('key', 'value'), table_format='grid'):
  table = tabulate.tabulate(alist, headers=headers, tablefmt=table_format)
  return table


def utc_now_string():
  x = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S_%Z')
  return x