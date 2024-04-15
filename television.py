
class Television():

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:

        """
        Method to set default values of power, mute, volume, channel variables
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to set the power
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Method to mute
        """
        if self.__status:
            if not self.__muted:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self) -> None:
        """
        Method to increase the tv channel
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the tv channel
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the tv volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Method to decrease the tv volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        Method to show the tv power, channel, volume
        :return: tv power, channel, volume
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"












