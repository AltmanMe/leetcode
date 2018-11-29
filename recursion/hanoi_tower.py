from basic.stack import Stack

def move_tower(height, from_tower, with_tower, to_tower):
    if height >= 1:
        move_tower(height-1, from_tower, to_tower, with_tower)
        move_disk(from_tower, to_tower)
        move_tower(height-1, with_tower, from_tower, to_tower)

def move_tower_stack(height, from_tower, with_tower, to_tower, cnt):
    if height >= 1:
        #cnt = cnt + 1
        move_tower_stack(height-1, from_tower, to_tower, with_tower, cnt)
        disk = from_tower.pop()
#        if disk == 2:
#            print('2')
        to_tower.push(disk)
#        print_stack(from_tower, with_tower, to_tower, cnt)
        print_stack(ft, wt, tt, cnt)
        cnt = cnt + 1
        move_tower_stack(height-1, with_tower, from_tower, to_tower, cnt)


def move_disk(fp, tp):
    print('Moving Disk from {} to {}'.format(fp,tp))

def print_stack(fp, wp, tp, cnt):
    print('{}th From Tower:{}'.format(cnt, fp.traverse()))
    print('{}th With Tower:{}'.format(cnt, wp.traverse()))
    print('{}th To Tower:{}'.format(cnt, tt.traverse()))

ft = Stack()
wt = Stack()
tt = Stack()
n = 3
cnt = 0

# initialize
for i in range(n,0,-1):
    ft.push(i) # 1 to n, from small to big

#move_tower(n, 'A', 'B', 'C')
move_tower_stack(n, ft, wt, tt, cnt)
