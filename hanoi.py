from re import S


def move_disk(disk_num: int, start_peg: int, end_peg: int) -> None:
    """print movement of disks

    Parameters
    ----------
    disk_num : int
        id number of disk
    start_peg : int
        start point
    end_peg : int
        end point
    """
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))
    return

def hanoi(num_disks: int, start_peg: int, end_peg: int) -> None:
    """implementation of hanoi top problem (only 3 pegs case)
    
    Hanoi top problem
     - {num_disks} disks move from {start_peg} to {end_peg}
     - number of disk represent the size of disk
     - bigger disk must be always below of smaller disk

    Parameters
    ----------
    num_disks : int
        which of disk
    start_peg : int
        start point
    end_peg : int
        end point
    """
    
    ## base case
    if num_disks == 1:
        move_disk(num_disks, start_peg, end_peg)
        return
    
    ## recursive case
    temp_peg = ({1, 2, 3} - {start_peg, end_peg}).pop()
    hanoi(num_disks - 1, start_peg, temp_peg)  ## firstly, move {num_disks} - 1 disks from start to temp
    move_disk(num_disks, start_peg, end_peg)  ## move the biggest disk to end
    hanoi(num_disks - 1, temp_peg, end_peg)  ## move {num_disks} - 1 disks from temp to end

    return

# 테스트 코드 (포함하여 제출해주세요)
if __name__ == '__main__':
    hanoi(3, 1, 3)