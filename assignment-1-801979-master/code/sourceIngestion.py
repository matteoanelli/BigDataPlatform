# script that ingest data inside the dms

class sourceIngestion:
    def __init__(self, part_id, ts_date, ts_time, room):
        self.part_id = part_id
        self.ts_date = ts_date
        self.ts_time = ts_time
        self.room = room

    def map(self):
        data = {
            'part_id': self.part_id,
            'ts_date': self.ts_date,
            'ts_time': self.ts_time,
            'room': self.room
        }
        return data


