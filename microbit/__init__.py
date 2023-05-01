# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from typing import (
    Any,
    List,
    NewType,
    Optional,
    Union,
    Tuple,
)

_UARTParity = NewType("_UARTParity", int)


def panic() -> None:
    """
    Put micro:bit in panic() mode and display an unhappy face.
    Press the reset button to exit panic() mode.
    """
    pass


def sleep(time: int) -> None:
    """
    Put micro:bit to sleep for some milliseconds (1 second = 1000 ms) of time.
    sleep(2000) gives micro:bit a 2 second nap.
    """
    """
    These pins are aranged on the bottom of the board and have holes through
    them
    """
    def is_touched(self) -> bool:
        """
        Returns if the pin is being physically touched on the hardware
        """
        pass


pin0 = _GiantPin()
pin1 = _GiantPin()
pin2 = _GiantPin()
pin3 = _AnaloguePin()
pin4 = _AnaloguePin()
pin5 = _Pin()
pin6 = _Pin()
pin7 = _Pin()
pin8 = _Pin()
pin9 = _Pin()
pin10 = _AnaloguePin()
pin11 = _Pin()
pin12 = _Pin()
pin13 = _Pin()
pin14 = _Pin()
pin15 = _Pin()
pin16 = _Pin()
# Pin17 = 3v3
# Pin18 = 3v3
pin19 = _Pin()
pin20 = _Pin()
# pin21 = gnd
# pin22 = gnd
# V2
pin_logo = _GiantPin()
pin_speaker = _AnaloguePin()


# I2C
class _I2C(object):
    def read(self, address: int, n: int, repeat: bool = False) -> bytes:
        """
        Use read(address, n) to read 'n' bytes from the device with the 7-bit
        address.
        If repeat is True, no stop bit will be sent.
        """
        pass

    def write(self, adress: int, buffer: bytes, repeat: bool = False) -> None:
        """
        Use write(address, buffer) to write to the 'buffer' of the device at
        the 7-bit 'address'.
        If repeat is True, no stop bit will be sent.
        """
        pass

    def init(self, frequency: int, scl: _Pin, sda: _Pin) -> None:
        """
        Use init(frequency, scl, sda) to set the bus frequency and pins.
        """
        pass


i2c = _I2C()


# Image
class Image(object):
    def __init__(self, *args: Any) -> None:
        """
        There are three ways to construct an image
        First, with a string:
            Image(
                '09090:'
                '99999:'
                '99999:'
                '09990:'
                '00900:'
            )
            This would create a 5x5 heart shaped image.
            Numbers go from 0 (off) to 9 (brightest).
            Note the colon ':' to set the end of a row. You can also use \\n
        Second with a width/height:
            Image(5, 5)
            This creates a blank 5x5 image, which you can manipulate
        Lastly you can pass a buffer with a width and a height
            Image(5, 5, [
                0, 9, 0, 9, 0,
                9, 9, 9, 9, 9,
                9, 9, 9, 9, 9,
                0, 9, 9, 9, 0,
                0, 0, 9, 0, 0,
            ])
            This would create the heart image from the first method.
        """

    def width(self) -> int:
        """
        Return the width of the image in pixels.
        """
        pass

    def height(self) -> int:
        """
        Return the height of the image in pixels.
        """
        pass

    def get_pixel(self, x: int, y: int) -> int:
        """
        Use get_pixel(x, y) to return the image's brightness at LED pixel
        (x,y).
        Brightness can be from 0 (LED is off) to 9 (maximum LED brightness).
        """
        pass

    def set_pixel(self, x: int, y: int, b: int) -> None:
        """
        Use set_pixel(x, y, b) to set the LED pixel (x,y) in the image to
        brightness 'b' which can be set between 0 (off) to 9 (full brightness).
        """
        pass

    def shift_left(self, n: int) -> 'Image':
        """
        Use shift_left(n) to make a copy of the image but moved 'n' pixels to
        the left.
        """
        pass

    def shift_right(self, n: int) -> 'Image':
        """
        Use shift_right(n) to make a copy of the image but moved 'n' pixels to
        the right.
        """
        pass

    def shift_up(self, n: int) -> 'Image':
        """
        Use shift_up(n) to make a copy of the image but moved 'n' pixels up.
        """
        pass

    def shift_down(self, n: int) -> 'Image':
        """
        Use shift_down(n) to make a copy of the image but moved 'n' pixels
        down.
        """
        pass

    def copy(self) -> 'Image':
        """
        Use copy() to make a new exact copy of the image.
        """
        pass

    def crop(self, x1: int, y1: int, x2: int, y2: int) -> 'Image':
        """
        Use crop(x1, y1, x2, y2) to make a cut-out copy of the image where
        coordinate (x1,y1) is the top left corner of the cut-out area and
        coordinate (x2,y2) is the bottom right corner.
        """
        pass

    def invert(self) -> 'Image':
        """
        Use invert() to make a negative copy of the image. Where a pixel was
        bright or on in the original, it is dim or off in the negative copy.
        """
        pass

    HEART = None  # type: Image
    HEART_SMALL = None  # type: Image
    HAPPY = None  # type: Image
    SMILE = None  # type: Image
    SAD = None  # type: Image
    CONFUSED = None  # type: Image
    ANGRY = None  # type: Image
    ASLEEP = None  # type: Image
    SURPRISED = None  # type: Image
    SILLY = None  # type: Image
    FABULOUS = None  # type: Image
    MEH = None  # type: Image
    YES = None  # type: Image
    NO = None  # type: Image
    CLOCK12 = None  # type: Image
    CLOCK11 = None  # type: Image
    CLOCK10 = None  # type: Image
    CLOCK9 = None  # type: Image
    CLOCK8 = None  # type: Image
    CLOCK7 = None  # type: Image
    CLOCK6 = None  # type: Image
    CLOCK5 = None  # type: Image
    CLOCK4 = None  # type: Image
    CLOCK3 = None  # type: Image
    CLOCK2 = None  # type: Image
    CLOCK1 = None  # type: Image
    ARROW_N = None  # type: Image
    ARROW_NE = None  # type: Image
    ARROW_E = None  # type: Image
    ARROW_SE = None  # type: Image
    ARROW_S = None  # type: Image
    ARROW_SW = None  # type: Image
    ARROW_W = None  # type: Image
    ARROW_NW = None  # type: Image
    TRIANGLE = None  # type: Image
    TRIANGLE_LEFT = None  # type: Image
    CHESSBOARD = None  # type: Image
    DIAMOND = None  # type: Image
    DIAMOND_SMALL = None  # type: Image
    SQUARE = None  # type: Image
    SQUARE_SMALL = None  # type: Image
    RABBIT = None  # type: Image
    COW = None  # type: Image
    MUSIC_CROTCHET = None  # type: Image
    MUSIC_QUAVER = None  # type: Image
    MUSIC_QUAVERS = None  # type: Image
    PITCHFORK = None  # type: Image
    XMAS = None  # type: Image
    PACMAN = None  # type: Image
    TARGET = None  # type: Image
    TSHIRT = None  # type: Image
    ROLLERSKATE = None  # type: Image
    DUCK = None  # type: Image
    HOUSE = None  # type: Image
    TORTOISE = None  # type: Image
    BUTTERFLY = None  # type: Image
    STICKFIGURE = None  # type: Image
    GHOST = None  # type: Image
    SWORD = None  # type: Image
    GIRAFFE = None  # type: Image
    SKULL = None  # type: Image
    UMBRELLA = None  # type: Image
    SNAKE = None  # type: Image
    ALL_CLOCKS = None  # type: List[Image]
    ALL_ARROWS = None  # type: List[Image]


# uart
class _UARTSerial(object):
    ODD = _UARTParity(1)
    EVEN = _UARTParity(0)

    def init(
        self,
        baudrate: int = 9600,
        bits: int = 8,
        parity: Optional[_UARTParity] = None,
        stop: int = 1,
        tx: Optional[_Pin] = None,
        rx: Optional[_Pin] = None,
    ) -> None:
        """
        Use init() to set up communication using the default values.
        Otherwise override the defaults as named arguments.
        """
        pass

    def any(self) -> bool:
        """
        If there are incoming characters waiting to be read, any() will return
        True.
        Otherwise, returns False.
        """
        pass

    def read(self, n: int) -> bytes:
        """
        Use read() to read characters.
        Use read(n) to read, at most, 'n' bytes of data.
        """
        pass

    def readall(self) -> bytes:
        """
        Use readall() to read as much data as possible.
        """
        pass

    def readline(self) -> bytes:
        """
        Use readline() to read a line that ends with a newline character.
        """
        pass

    def readinto(self, buf: bytes, n: int) -> int:
        """
        Use readinto(buf) to read bytes into the buffer 'buf'.
        Use readinto(buff, n) to read, at most, 'n' number of bytes into 'buf'.
        """
        pass

    def write(self, buf: bytes) -> int:
        """
        Use write(buf) to write the bytes in buffer 'buf' to the connected
        device.
        """
        pass


uart = _UARTSerial()


# SPI
class _SPISerial(object):
    def init(
        self,
        baudrate: int = 1000000,
        bits: int = 8,
        mode: int = 0,
        sclk: _Pin = pin13,
        mosi: _Pin = pin15,
        miso: _Pin = pin14,
    ) -> None:
        """
        Set up communication. Override the defaults for baudrate, mode,
        SCLK, MOSI and MISO. The default connections are pin13 for SCLK, pin15
        for MOSI and pin14 for MISO.
        """
        pass

    def write(self, buf: bytes) -> None:
        """
        Use write(buf) to write bytes in buffer 'buf' to the connected device.
        """
        pass

    def read(self, n: int) -> bytes:
        """
        Use read(n) to read 'n' bytes of data.
        """
        pass

    def write_readinto(self, outbuf: bytes, inbuf: bytes) -> None:
        """
        Use write_readinto(outbuf, inbuf) to write the 'outbuf' buffer to the
        connected device and read any response into the 'inbuf' buffer. The
        length of the buffers should be the same. The buffers can be the same
        object.
        """
        pass


spi = _SPISerial()


# V2

# Built-in speaker
class _Speaker(object):
    def off(self) -> bool:
        """
        Use off() to turn off the speaker. This does not disable sound output 
        to an edge connector pin.
        """
        pass

    def on(self) -> bool:
        """
        Use on() to turn on the speaker.
        """
        pass


speaker = _Speaker()


# Built-in microphone
class _Microphone(object):
    def current_event(self) -> str:
        """
        Returns the name of the last recorded sound event, SoundEvent('loud') 
        or SoundEvent('quiet').
        """
        pass

    def was_event(self, event: str) -> bool:
        """
        Event is a sound event such as SoundEvent.LOUD or SoundEvent.QUIET. 
        Returns true if sound was heard at least once since the last call, 
        otherwise false.
        The function also clears the sound event history 
        before returning.
        """
        pass

    def is_event(self, event: str) -> bool:
        """
        Event is a sound event such as SoundEvent.LOUD or SoundEvent.QUIET. 
        Returns true if sound event is the most recent since the last call, 
        otherwise false.
        The function does not clear the sound event history.
        """
        pass

    def get_events(self) -> Tuple[str, str]:
        """
        Returns a tuple of the event history. The most recent is listed 
        last.
        The function also clears the sound event history before returning.
        """
        pass

    def set_threshold(
            self,
            event: str,
            value: int,
        ) -> Tuple[str, str]:
        """
        An event is a sound event, such as SoundEvent.LOUD or SoundEvent.QUIET.
        Value is the threshold level in the range 0-255. For example, 
        set_threshold(SoundEvent.LOUD, 250) will only trigger if the sound is 
        very loud (>= 250).
        """
        pass

    def sound_level(self) -> int:
        """
        Returns a representation of the sound pressure level in the range 0 
        to 255.
        """
        pass

microphone = _Microphone()
