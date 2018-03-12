#include <stdio.h>
#include <sys/ioctl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>


// $ gcc mmc_exit_bootloader.c -o mmc_exit_bootloader^C
// https://github.com/m-labs/sinara/issues/462

int main()
{
  int fd;
  int RTS_flag;

    fd = open("/dev/ttyUSB1", O_RDWR | O_NOCTTY);
    RTS_flag = TIOCM_RTS;
    ioctl(fd,TIOCMBIC,&RTS_flag);
    close(fd);

    fd = open("/dev/ttyUSB2", O_RDWR | O_NOCTTY);
    RTS_flag = TIOCM_RTS;
    ioctl(fd,TIOCMBIC,&RTS_flag);
    close(fd);

    fd = open("/dev/ttyUSB3", O_RDWR | O_NOCTTY);
    RTS_flag = TIOCM_RTS;
    ioctl(fd,TIOCMBIC,&RTS_flag);
    close(fd);


    fd = open("/dev/ttyUSB4", O_RDWR | O_NOCTTY);
    RTS_flag = TIOCM_RTS;
    ioctl(fd,TIOCMBIC,&RTS_flag);
    close(fd);

    return 0;
}