class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        # 1. 分別抽出開始與結束時間，並各自排序
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        
        rooms = 0
        end_ptr = 0 # 指向 ends 陣列的指標
        
        # 2. 遍歷所有的開始時間
        for start in starts:
            # 如果當前會議開始時，最早結束的會議還沒結束 -> 需要新房間
            if start < ends[end_ptr]:
                rooms += 1
            # 如果已經有會議結束了 -> 重複利用房間 (不增加房間數)，把指標推向下一個結束時間
            else:
                end_ptr += 1
                
        return rooms