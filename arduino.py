#!/usr/bin/env python3
from   dataclasses import dataclass, field
from   typing      import Final
from   time        import sleep
import asyncio


HIGH   : Final = 1 # set 'bit' values
LOW    : Final = 0
OUTPUT : Final = 1 # mode
INPUT  : Final = 0


IO_PORT_LIMIT     : Final = 14
ANALOG_PORT_LIMIT : Final = 6
STARTING_CONFIG = [0, 0]


@dataclass(kw_only=False, init=True, frozen=False, match_args=True, slots=True)
class Arduino:
  io     : field(default_factory=list)
  analog : field(default_factory=list)
  power  : field(default=False)


def setup(a : Arduino) -> Arduino:


  start_io     = list()
  start_analog = list()


  while len(start_io) < IO_PORT_LIMIT:
    start_io.append([0, 0])
  

  while len(start_analog) < ANALOG_PORT_LIMIT:
    start_analog.append([0, 0])


  a.io     = start_io
  a.analog = start_analog
  

  # TODO: Your code goes here.
  # Example code is provided.

  
  a.io[0][0] = OUTPUT
  a.io[0][1] = LOW
  

  return a


def toggle(integer : int) -> int:
  if integer == 0:
    return 1
  else:
    return 0


def turn_on(a : Arduino) -> Arduino:
  a.power = True


def turn_off(a : Arduino) -> Arduino:
  a.power = False


def reset(a : Arduino) -> Arduino:
  turn_off(a)
  turn_on(a)
  setup(a)
  return a


async def loop(a : Arduino) -> None:


  while a.power:


    print(a.io[0][1])


    a.io[0][1] = toggle(a.io[0][1])


    # a = reset(a)


    sleep(1.0)


async def main():


  a = Arduino(io=list[14], analog=list[6], power=True)
  a = setup  (a)
  asyncio.run(await loop(a))


if __name__ == '__main__':
  asyncio.run(main())